#!/usr/bin/env python3
"""Synchronize public researchmap achievements; fail closed on incomplete API responses."""
import datetime as dt
import json
import os
from pathlib import Path
import re
import time
import urllib.parse
import urllib.request

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / 'publications.json'
PERMALINK = os.environ.get('RESEARCHMAP_PERMALINK', 'Y_Ohmori')
TYPES = {'published_papers': 'papers', 'misc': 'misc', 'books_etc': 'books', 'presentations': 'presentations'}


def request(url):
    for attempt in range(3):
        try:
            req = urllib.request.Request(url, headers={'User-Agent': 'OhmoriLab-publications-sync/1.0', 'Accept': 'application/json'})
            with urllib.request.urlopen(req, timeout=35) as r:
                return json.load(r)
        except Exception:
            if attempt == 2:
                raise
            time.sleep(2 ** attempt)


def value(item):
    if isinstance(item, str):
        return item.strip()
    if isinstance(item, dict):
        for key in ('en', 'ja', 'value', 'name', 'text'):
            if key in item:
                result = value(item[key])
                if result:
                    return result
    if isinstance(item, list):
        return ', '.join(filter(None, map(value, item)))
    return str(item) if isinstance(item, (int, float)) else ''


def name_list(record):
    for key in ('authors', 'author', 'presenters', 'publisher'):
        data = record.get(key)
        if data:
            if isinstance(data, list):
                names = []
                for p in data:
                    if isinstance(p, dict):
                        names.append(value(p.get('name')) or value(p.get('researcher_name')) or value(p.get('family_name')) + ' ' + value(p.get('given_name')))
                    else:
                        names.append(value(p))
                return ', '.join(x.strip() for x in names if x.strip())
            return value(data)
    return ''


def extract_items(body):
    if isinstance(body, list):
        return body, len(body)
    if not isinstance(body, dict):
        raise ValueError('Unexpected API response')
    records = next((body[k] for k in ('items', 'results', '@graph', 'data') if isinstance(body.get(k), list)), None)
    if records is None:
        raise ValueError('No recognized items list in researchmap response: ' + ', '.join(body.keys()))
    total = body.get('total_items', body.get('totalItems', body.get('total', None)))
    return records, int(total) if total is not None else None


def category_records(source, label):
    records = []
    start = 1
    limit = 100
    for page in range(30):
        query = urllib.parse.urlencode({'start': start, 'limit': limit, 'format': 'json'})
        url = f'https://api.researchmap.jp/{urllib.parse.quote(PERMALINK)}/{source}?{query}'
        batch, total = extract_items(request(url))
        if not batch:
            if start == 1:
                raise ValueError(f'No {source} records (API response may be incomplete)')
            break
        records.extend(batch)
        if total is not None and len(records) >= total:
            break
        if len(batch) < limit:
            if total is not None and len(records) < total:
                raise ValueError(f'Truncated {source}: {len(records)} of {total}')
            break
        start += len(batch)
    else:
        raise ValueError(f'Pagination cap reached for {source}')
    if total is not None and len(records) < total:
        raise ValueError(f'Incomplete {source}: {len(records)} of {total}')
    items = []
    for x in records:
        if not isinstance(x, dict):
            raise ValueError(f'Unexpected non-object {source} item')
        title = value(x.get('paper_title') or x.get('title') or x.get('book_title') or x.get('presentation_title'))
        date = value(x.get('publication_date') or x.get('presentation_date') or x.get('event_date') or x.get('date') or x.get('published_date'))
        year_match = re.search(r'(19|20)\d{2}', date)
        ident = x.get('identifiers') or {}
        doi = value(ident.get('doi')) if isinstance(ident, dict) else ''
        if not doi:
            doi = value(x.get('doi'))
        link = value(x.get('url') or x.get('external_link') or x.get('researchmap_url'))
        if not link.startswith('https://'):
            link = 'https://doi.org/' + doi.removeprefix('https://doi.org/') if doi else 'https://researchmap.jp/' + PERMALINK
        venue = value(x.get('publication_name') or x.get('journal') or x.get('event') or x.get('conference_name') or x.get('publisher'))
        if title:
            items.append({'type': label, 'year': year_match.group(0) if year_match else '', 'title': title,
                          'authors': name_list(x), 'venue': venue, 'url': link})
    if len(items) != len(records):
        raise ValueError(f'{source}: {len(records)-len(items)} records lacked titles; refusing incomplete sync')
    return items


def main():
    all_items = []
    counts = {}
    for source, label in TYPES.items():
        items = category_records(source, label)
        counts[label] = len(items)
        all_items.extend(items)
        print(f'{source}: {len(items)} records')
    if len(all_items) < 120:
        raise ValueError(f'Only {len(all_items)} records; not replacing the existing 154-record list')
    if OUTPUT.exists():
        old = json.loads(OUTPUT.read_text(encoding='utf-8'))
        previous = len(old.get('items', []))
        if previous and len(all_items) < int(previous * 0.85):
            raise ValueError(f'New list ({len(all_items)}) is less than 85% of previous ({previous})')
    all_items.sort(key=lambda x: x['year'], reverse=True)
    result = {'source': 'researchmap public API', 'permalink': PERMALINK,
              'updatedAt': dt.datetime.now(dt.timezone.utc).isoformat(timespec='seconds'),
              'counts': counts, 'items': all_items}
    # Avoid unnecessary commits if only timestamp changed.
    if OUTPUT.exists():
        old = json.loads(OUTPUT.read_text(encoding='utf-8'))
        if old.get('items') == result['items'] and old.get('counts') == result['counts']:
            print('No changes detected')
            return
    OUTPUT.write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(f'Wrote {len(all_items)} entries to {OUTPUT}')


if __name__ == '__main__':
    main()
