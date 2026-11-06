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

- [Rice QTL / GWAS Genome Browser V2](https://5ww2cw2jb7-afk.github.io/ohmori-lab-website/rice_browser_v2.html)
  - **日本語：** GWAS Atlas、Q-TARO、EURoot RiceのQTL/GWAS情報、RAP遺伝子とPlantRegMap由来の進化的保存領域（CE）を同じゲノム座標上で閲覧するブラウザです。CEはChr1–Chr12の**371,544区間**を表示し、拡大・密度表示、区間一覧、CSV出力に対応します。座標の互換性には未検証の部分があるため、重なりの解釈には注意が必要です。
  - **English:** Explore GWAS/QTL data, RAP genes, and **371,544 PlantRegMap conserved elements (CEs)** on chromosomes 1–12, with interval/density views, regional lists, and CSV export. Some coordinate compatibility remains unvalidated; interpret overlaps cautiously.
  - [データの出典・引用・利用条件 / Sources, citations & usage](https://5ww2cw2jb7-afk.github.io/ohmori-lab-website/rice_browser_v2_sources.html)
- [GCIC — Gene-centered Identification of Cis-regulatory Islands](https://github.com/5ww2cw2jb7-afk/gcic_dockerized_package)
- [CSV Data Visualization App (R / Shiny)](https://yoshihiro-ohmori.shinyapps.io/session4/)
  - R5年度データサイエンス講習会の課題として開発したWebアプリケーション。
  - CSVファイルからヒストグラム、散布図、箱ひげ図を作成できます。
  - [JBIC データサイエンス講習会](https://www.jbic.or.jp/stream)
  
- [Rice Signature Explorer v1.3](https://5ww2cw2jb7-afk.github.io/ohmori-lab-website/rice_signature_explorer.html)
  - イネの遺伝子IDとlog2FCを入力し、RED 2.0（328比較）とRiceXPro（54比較）の計382シグニチャーとの類似性をSpearman順位相関で検索するオフライン対応のブラウザツールです。入力データには任意でモジュール名（`module`）や時間情報（`time_h`）を付与できます。複数時点の入力では時点別の相関をヒートマップで比較でき、CSV出力にも対応しています。
  - Enter rice gene IDs and log2 fold changes to compare against 382 reference signatures from RED 2.0 (328 comparisons) and RiceXPro (54 comparisons) using Spearman rank correlation. Input data may optionally include module labels (`module`) and time information (`time_h`). For multiple input time points, correlations can be compared in a heatmap. CSV export is also supported.
  - [データの出典・引用・利用条件 / Data sources & citations](https://5ww2cw2jb7-afk.github.io/ohmori-lab-website/rice_signature_sources.html)
  - Reference datasets: [RED 2.0](https://ngdc.cncb.ac.cn/red/) and [RiceXPro](https://ricexpro.dna.affrc.go.jp/); GEO [GSE39429](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE39429). Please cite the original studies and review their respective data terms before reuse.
  - Reference gene set: 24,061 AGIS↔RAP-DB one-to-one mapped genes; database release v1.1. The similarity tool is v1.3.

## Rice Signature Explorer — Data Sources, Citations and Usage / データの出典・引用・利用条件

Rice Signature Explorer v1.3 uses a processed reference signature dataset (database v1.1) derived from publicly available rice gene-expression resources. It contains **328 RED 2.0 comparisons across 89 BioProjects** and **54 RiceXPro hormone-treatment comparisons (GEO: GSE39429)**, aligned to **24,061 one-to-one AGIS–RAP-DB gene correspondences**. RED 2.0 includes genotype/genetic perturbations, nutrition/water conditions, abiotic stress, chemical treatments, hormone/signaling conditions, biotic responses, light/photoperiod, and other experiments—not only plant hormone treatments. The Ohmori Lab processing includes comparison curation, log2 fold-change calculation, quality-control annotations, gene-ID mapping, and integration. These derived analyses are distinct from the original datasets and publications.

Rice Signature Explorer v1.3は、公開イネ遺伝子発現データを基に整備した参照シグニチャーデータセット（データベースv1.1）を使用しています。**RED 2.0由来328比較（89 BioProjects）**と**RiceXPro（GEO: GSE39429）のホルモン処理由来54比較**を、**AGIS–RAP-DBの1対1対応24,061遺伝子**で統合しています。RED 2.0由来の比較はホルモン処理だけでなく、遺伝子型・遺伝子操作、栄養・水分条件、非生物的ストレス、化学物質、生物的応答、光条件など多様です。比較条件の整理、log2FC計算、QC注記、遺伝子ID対応付け、データ統合は本ツール向けの派生的な処理であり、元データや原著論文そのものとは区別されます。

### Reference comparison categories / 収録比較の主分類

**RED 2.0由来328比較**は、元の比較計画に付与されていた29種類の `treatment_class` を基に、次の8主分類に集約しました（各比較を一度だけ計上）：**遺伝子型・遺伝子操作（89比較）、栄養・水分条件（複合条件含む）（58比較）、非生物的ストレス（57比較）、化学物質・複合処理（34比較）、ホルモン・シグナル（31比較）、生物的応答・プライミング（16比較）、光・日長（8比較）、その他・未分類（35比較）**。**合計328比較**です。

**RED 2.0: 328 reference comparisons** are assigned to eight non-overlapping *primary metadata categories*, consolidated from 29 existing `treatment_class` labels (one category per comparison): Genotype & genetic perturbation (89), Nutrition & water factorial (58), Abiotic stress (57), Chemicals & combined treatments (34), Hormones & signaling (31), Biotic response & priming (16), Light & photoperiod (8), Other & unspecified (35). **Total: 328.**

**RiceXProの54比較**は、この328比較とは別で、6種類の植物ホルモン（ABA、オーキシン、サイトカイニン、ジベレリン、ブラシノステロイド、ジャスモン酸）の処理比較が**各9比較**、合計54比較です。

**RiceXPro's 54 additional comparisons** are hormone-treatment comparisons: ABA (9), auxin (9), cytokinin (9), gibberellin (9), brassinosteroid (9), and jasmonic acid (9).

**分類上の注意 / Classification caveat:** 上記は既存メタデータラベルの集計であり、各比較について論文・実験条件を全面的に再査読して得た生物学的な排他分類ではありません。例えば「Other / unspecified」にBLなどホルモン関連処理が含まれる可能性があり、遺伝子型×ストレスなど複合実験も主分類を1つだけ割り当てています。**したがって「ホルモン・シグナル（31比較）」は、RED 2.0に含まれるホルモン関連実験の完全な件数を意味しません。** / These categories reflect the original metadata labels; they are not a fully re-curated, biologically exhaustive classification. A hormone-related experiment may appear in an original "Other / unspecified" class, and multi-factor experiments have one primary category only.

- [**RED 2.0全328比較：分類別の検索可能なHTML一覧 / Searchable 328-comparison list**](https://5ww2cw2jb7-afk.github.io/ohmori-lab-website/rice_signature_RED2_328_classification.html)
- [**全328比較の分類・処理・対照・BioProject・QC付きCSV / Detailed 328-comparison CSV**](https://github.com/5ww2cw2jb7-afk/ohmori-lab-website/blob/main/rice_signature_RED2_328_treatment_classification.csv)
- [**分類件数と元の29ラベルの対応表 / Category summary CSV**](https://github.com/5ww2cw2jb7-afk/ohmori-lab-website/blob/main/rice_signature_RED2_328_category_summary.csv)

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

For methods, caveats, and source links, see [Rice Signature Explorer — Data Sources & Citations](https://5ww2cw2jb7-afk.github.io/ohmori-lab-website/rice_signature_sources.html). The reference correlations describe expression-pattern similarity, not evidence of causation. / 解析方法・注意事項・出典リンクは[出典と引用のページ](https://5ww2cw2jb7-afk.github.io/ohmori-lab-website/rice_signature_sources.html)をご参照ください。相関は発現変動パターンの類似性であり、因果関係を示すものではありません。

## Rice QTL / GWAS Genome Browser V2 — Data Sources, Citations and Usage / データの出典・引用・利用条件

**収録データ / Data:** GWAS Atlas、Q-TARO、EURoot RiceのQTL/GWAS情報とRAP-DB / IRGSP-1.0の遺伝子情報に加え、PlantRegMapの進化的保存領域（CE）を統合表示します。元GTFの**372,065区間**のうち**Chr1–Chr12の371,544区間**を表示し、**ChrSy・ChrUnの521区間**は再現用データにのみ保持します。CEの表示切替、拡大時の区間表示、広域での密度表示、区間一覧、CSV出力が可能です。

**Data (English):** V2 combines QTL/GWAS information (GWAS Atlas, Q-TARO, EURoot Rice), RAP-DB / IRGSP-1.0 genes, and PlantRegMap conserved elements (CEs). Of **372,065** input intervals, **371,544** on chromosomes 1–12 are displayed; **521** ChrSy/ChrUn intervals remain in the reproducibility data. CE track toggling, interval/density views, regional lists, and CSV export are supported.

**出典 / Citation:** Tian F. et al. (2020), *PlantRegMap: charting functional regulatory maps in plants*, *Nucleic Acids Research* 48(D1):D1104–D1113. [DOI: 10.1093/nar/gkz1020](https://doi.org/10.1093/nar/gkz1020). そのほかのデータ提供元は[**V2出典ページ / V2 sources**](https://5ww2cw2jb7-afk.github.io/ohmori-lab-website/rice_browser_v2_sources.html)にまとめています。

**科学的注意 / Scientific limitations:** CEとIRGSP-1.0の座標一致は配列レベルで未検証です。Q-TAROのアセンブリも未確認で、EURootの一部座標は表示用の暫定換算です。GWAS SNPの全座標も独立検証済みではありません。**位置の重なりや進化的保存だけで、同一QTL、TF結合、cis制御機能、因果変異は証明されません。** / CE assembly compatibility has not been sequence-validated; Q-TARO assembly identity is unknown, some EURoot positions are provisional display conversions, and not all GWAS coordinates have been independently validated. Positional overlap or conservation alone does not establish a shared QTL, regulatory function, or causality.

**権利・利用条件 / Rights:** 論文のライセンスと各データセットの再配布許諾は必ずしも同一ではありません。CEを含む第三者データの公開・再配布前に、提供元ごとの最新条件や必要な許諾を確認してください。 / Article licenses do not necessarily authorize redistribution of source datasets or derived files. Verify dataset-specific rights and permissions before publication or reuse.

**再現性 / Reproducibility:** 再現可能フルパックには元のブラウザ、`CE_Osj.gtf`、`build_v2.py`、生成用ファイルと検証情報を収録しています。解凍先で `python3 build_v2.py` を実行して再生成できます。実画面での最終動作確認は公開前に実施してください。 / The full reproducibility pack includes the original browser, source GTF, generator and validation files. Rebuild with `python3 build_v2.py`; perform browser-level checks before deployment.

[**V2ブラウザを開く / Open V2**](https://5ww2cw2jb7-afk.github.io/ohmori-lab-website/rice_browser_v2.html) · [**出典・引用・利用条件 / Sources & terms**](https://5ww2cw2jb7-afk.github.io/ohmori-lab-website/rice_browser_v2_sources.html)

## Website Management / サイト管理

Website content is maintained in this GitHub repository. The site is published using GitHub Pages.

文章の編集方法や導入手順は `docs/` フォルダ内の管理用マニュアルを参照してください。
