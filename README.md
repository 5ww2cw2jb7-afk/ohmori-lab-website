# Ohmori Lab

**Informatics × Molecular Genetics & Breeding**

情報科学と分子遺伝学・育種学を基盤として、イネを中心にゲノム・マルチオミクス研究を進めています。得られた知見と解析手法を、多様な植物の遺伝研究や育種へ応用することを目指しています。

Our research integrates informatics, molecular genetics, and multi-omics approaches to advance plant science. We primarily study rice, with the goal of extending our insights and analytical methods to diverse plant species.

## Website / ホームページ

https://5ww2cw2jb7-afk.github.io/ohmori-lab-website/

## Research Areas / 研究分野

- Rice Molecular Genetics & Genomics
- Informatics & Multi-Omics
- Applications Across Plant Species

## Publications / 研究業績

Publication records are retrieved periodically from publicly available researchmap data using GitHub Actions.

研究業績はresearchmapの公開データから定期的に自動取得しています。

Researchmap: https://researchmap.jp/Y_Ohmori

## Research Tools / 研究ツール

- [Rice QTL / GWAS Genome Browser](https://5ww2cw2jb7-afk.github.io/ohmori-lab-website/rice_browser.html)
- [GCIC — Gene-centered Identification of Cis-regulatory Islands](https://github.com/5ww2cw2jb7-afk/gcic_dockerized_package)
- [CSV Data Visualization App (R / Shiny)](https://yoshihiro-ohmori.shinyapps.io/session4/)
  - R5年度データサイエンス講習会の課題として開発したWebアプリケーション。
  - CSVファイルからヒストグラム、散布図、箱ひげ図を作成できます。
  - [JBIC データサイエンス講習会](https://www.jbic.or.jp/stream)
  
- [Rice Signature Explorer v1.3](https://5ww2cw2jb7-afk.github.io/ohmori-lab-website/rice_signature_explorer.html)
  - イネの遺伝子IDとlog2FCを入力し、RED 2.0（328比較）とRiceXPro（54比較）の計382シグニチャーとの類似性をSpearman順位相関で検索するオフライン対応のブラウザツールです。時系列・モジュール解析、ヒートマップ、CSV出力を利用できます。
  - Enter rice gene IDs and log2 fold changes to search 382 reference signatures using Spearman correlation. Supports module/time-series analysis, heatmaps, and CSV export.
  - [データの出典・引用・利用条件 / Data sources & citations](https://5ww2cw2jb7-afk.github.io/ohmori-lab-website/rice_signature_sources.html)
  - Reference datasets: [RED 2.0](https://ngdc.cncb.ac.cn/red/) and [RiceXPro](https://ricexpro.dna.affrc.go.jp/); GEO [GSE39429](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE39429). Please cite the original studies and review their respective data terms before reuse.
  - Reference gene set: 24,061 AGIS↔RAP-DB one-to-one mapped genes; database release v1.1. The similarity tool is v1.3.

## Data Sources, Attribution and Usage / データの出典・権利・利用条件

Rice Signature Explorer v1.3 uses a processed reference signature dataset (database v1.1) derived from publicly available rice gene-expression resources. The integrated reference includes **328 RED 2.0 comparisons** and **54 RiceXPro comparisons (GEO: GSE39429)**, aligned to **24,061 one-to-one AGIS–RAP-DB gene correspondences**. The Ohmori Lab processing includes comparison curation, log2 fold-change calculation, quality-control annotations, gene-ID mapping, and integration. These derived analyses should be distinguished from the original datasets and publications.

Rice Signature Explorer v1.3は、公開されているイネ遺伝子発現データから整備した参照シグニチャーデータセット（データベースv1.1）を使用しています。**RED 2.0由来328比較**と**RiceXPro（GEO: GSE39429）由来54比較**を、**AGIS–RAP-DBの1対1対応24,061遺伝子**で統合しています。比較条件の整理、log2FC計算、QC注記、遺伝子ID対応付け、データ統合は本ツールのための派生的な処理であり、元データや原著論文そのものとは区別されます。

### Original sources and citations / 原データと引用

- **RED 2.0:** Wang et al. (2026), *Rice Expression Database (RED) 2.0*, *Nucleic Acids Research*. [DOI: 10.1093/nar/gkag1064](https://doi.org/10.1093/nar/gkag1064); [RED website](https://ngdc.cncb.ac.cn/red/).
- **RiceXPro:** Sato et al. (2013), *RiceXPro version 3.0*, *Nucleic Acids Research*. [DOI: 10.1093/nar/gks1125](https://doi.org/10.1093/nar/gks1125); [RiceXPro website](https://ricexpro.dna.affrc.go.jp/).
- **Source experiment:** [NCBI GEO GSE39429](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE39429).

For research use, please cite the relevant original datasets/publications as well as this tool when appropriate. 研究発表・論文等では、該当する原データと原著論文を適切に引用してください。

### Rights and redistribution / 権利と再配布

- **Original-data rights remain with the applicable providers and rights holders.** The publication licenses, database terms, source-data redistribution permissions, and software license are not necessarily identical. This repository does **not** grant additional rights to third-party datasets.
- **元データや原著論文の権利と適用される利用条件は各提供元・権利者に従います。** 論文のライセンス、データベースの規約、データの再配布条件、ソフトウェアのライセンスは必ずしも同一ではありません。このリポジトリの公開によって第三者データの権利が変更されるものではありません。
- Before redistribution, commercial reuse, or incorporation of the derived reference matrix into another product, **check the current source-specific conditions** and provide attribution. The full scope of redistribution rights for all upstream data has **not been independently confirmed here**.
- 再配布、商用利用、他のサービスへの組込みを行う場合は、**各原データの最新の利用条件を確認**し、出典を明記してください。元データ全件の再配布に関する権利確認が完了したと主張するものではありません。

For methods, caveats, and source links, see [Rice Signature Explorer — Data Sources & Citations](rice_signature_sources.html). The reference correlations describe expression-pattern similarity, not evidence of causation. / 解析方法・注意事項・出典リンクは[出典と引用のページ](rice_signature_sources.html)をご参照ください。相関は発現変動パターンの類似性であり、因果関係を示すものではありません。

## Website Management / サイト管理

Website content is maintained in this GitHub repository. The site is published using GitHub Pages.

文章の編集方法や導入手順は `docs/` フォルダ内の管理用マニュアルを参照してください。
