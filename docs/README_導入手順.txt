Ohmori Lab | researchmap → GitHub Actions 自動更新

【目的】
毎週月曜10:37（日本時間）に researchmap の公開APIから論文・MISC・書籍等・講演発表を取得し、publications.json を更新します。
既存 publications.html 内の154件はそのまま残ります。APIに失敗した場合はJSONを書き換えず、公開済み一覧を維持します。

【GitHubに追加する3ファイル】
1. publications.html → 既存の publications.html と置き換える
2. scripts/sync_researchmap.py → 新規追加
3. .github/workflows/researchmap-sync.yml → 新規追加

【重要】
ZIPをそのままアップロードしないでください。内部のファイルをGitHubの所定のパスに入れます。
ルートに scripts/ フォルダと .github/workflows/ フォルダを作ってください。GitHubの Add file > Create new file で `scripts/sync_researchmap.py` と打つと作成できます。内容はファイルからコピーしてください。

【実行】
GitHub > Actions > Sync researchmap publications > Run workflow > main > Run workflow
成功すると、ルートに publications.json が生成されます。GitHub Pagesの publications.html はこのJSONを優先して読み込みます。

【確認】
Actions の実行ログでカテゴリ別件数を確認してください。researchmap 側のAPIレスポンス形式や公開設定が想定と違う場合、Actionは失敗して変更を行いません。
本環境からresearchmap APIへの直接アクセスを検証できていないため、最初の実行で動作確認が必要です。

【権限】
workflow では contents: write を指定しています。リポジトリの Settings > Actions > General > Workflow permissions で Read and write permissions が必要な場合があります。

【注意】
JSONの内容は公開情報です。レコード数が120件未満、または前回比85%未満なら保存を停止します。researchmapの登録方法に依存し、最初の実行でフィールド変換を調整する可能性があります。
