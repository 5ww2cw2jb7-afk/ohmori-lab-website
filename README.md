# Ohmori Lab

**Informatics × Molecular Genetics & Breeding**

情報科学、分子遺伝学、育種学を基盤に、イネを中心としたゲノム・マルチオミクス研究に取り組んでいます。得られた知見と解析手法を、多様な植物の遺伝研究と育種へ応用することを目指しています。

Our research integrates informatics, molecular genetics, breeding, and multi-omics approaches, primarily using rice as a model system. We aim to extend the resulting knowledge and methods to diverse plant species.

**[研究室ホームページ / Lab website](https://5ww2cw2jb7-afk.github.io/ohmori-lab-website/)**

## Research / 研究分野

- Rice Molecular Genetics & Genomics / イネ分子遺伝学・ゲノミクス
- Informatics & Multi-Omics / 情報科学・マルチオミクス
- Applications Across Plant Species / 多様な植物への展開

## Research Tools / 公開ツール

| Tool | Description | Links |
| --- | --- | --- |
| **Rice QTL / GWAS Genome Browser V2** | イネQTL/GWAS、RAP遺伝子、PlantRegMap由来の保存領域（CE）の探索 / Rice QTL/GWAS, RAP genes and conserved elements | [Open](https://5ww2cw2jb7-afk.github.io/ohmori-lab-website/rice_browser_v2.html) · [Sources & caveats](https://5ww2cw2jb7-afk.github.io/ohmori-lab-website/rice_browser_v2_sources.html) |
| **Rice Signature Explorer** | イネの発現変動パターンをSpearman順位相関で比較 / Rice expression-signature similarity analysis | [Open current public version (v1.3; 382 comparisons)](https://5ww2cw2jb7-afk.github.io/ohmori-lab-website/rice_signature_explorer.html) · [Sources & methods](https://5ww2cw2jb7-afk.github.io/ohmori-lab-website/rice_signature_sources.html) |
| **GCIC** | 遺伝子周辺のcis制御モチーフ分布の探索 / Gene-centered cis-regulatory motif analysis | [GitHub](https://github.com/5ww2cw2jb7-afk/gcic_dockerized_package) |
| **CSV Data Visualization App** | CSVのヒストグラム・散布図・箱ひげ図 / R/Shiny visualization app | [Open](https://yoshihiro-ohmori.shinyapps.io/session4/) |

### Rice Signature Explorer: release status / 公開状況

- **Currently public / 現在公開中:** v1.3, **382 comparisons** (RED 2.0: 328; RiceXPro: 54). The link above continues to open this version.
- **In preparation / 公開準備中:** extended v2.2-based Explorer, **3,009 comparisons**, **37,537 RAP-DB gene IDs** across five sources: RED 2.0 (328), RiceXPro (54), GEO microarrays (1,805), UGA/RGAP MSU7 (7), and PlantRNA DB-derived FPKM (815).
- The 815 FPKM-derived comparisons have been **technically integrated**, but their biological comparison metadata have **not been individually audited**. The extended version is **not yet available from the public Explorer link**.

原データ、FC算出法、遺伝子ID対応、解釈上の注意、および引用・利用条件は[出典・方法ページ](https://5ww2cw2jb7-afk.github.io/ohmori-lab-website/rice_signature_sources.html)にまとめています。第三者データの権利や再配布条件は各提供元の規約に従います。

For data provenance, fold-change definitions, gene-ID mapping, scientific limitations, citations, and usage terms, see the [source and methods page](https://5ww2cw2jb7-afk.github.io/ohmori-lab-website/rice_signature_sources.html). Third-party data remain subject to their respective providers' terms.

## Publications / 研究業績

研究業績はresearchmapの公開情報を基に掲載し、GitHub Actionsを通じて定期取得しています。 / Publication records are periodically retrieved from public researchmap data using GitHub Actions.

[researchmap](https://researchmap.jp/Y_Ohmori)

## Website management / サイト管理

- The website is hosted on **GitHub Pages**.
- Main-page text and multilingual labels are maintained in **`editable_text.js`**; page layouts remain in their respective HTML files.
- Source/method pages, including **`rice_signature_sources.html`**, are maintained as separate HTML files.
- For editing and maintenance instructions, see **`docs/`**.

**Note:** Changes to this README do not change the website's on-page text or replace the currently published Explorer. / READMEの更新だけでは、ホームページの表示文や公開中のExplorer本体は変わりません。
