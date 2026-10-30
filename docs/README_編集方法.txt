Ohmori Lab 全ページ編集可能版（2026年10月30日）

1. ZIPを展開し、フォルダ内の index.html を Chrome で開いてください。
2. 文章・見出し・メニューを変更するときは editable_text.js をテキストエディタで開きます。
3. window.OHMORI_EDITABLE の中で、ページ名（index, research, profile, publications, members, news, contact, rice_browser）を探します。
4. ja（日本語）/en（英語）の引用符内の文字列を変更し保存します。\n は改行、 \" は引用符です。
5. リロードで確認してください。旧サイトと混在しないよう、ZIPに含む一式を同じフォルダに置いてください。

研究業績の個別データは editable_text.js 内の publications > PUBLICATION_RECORDS 配列で編集できます。
著者・題名・リンクなどを変えられます。検索・種類・年フィルタの仕組みはそのままです。
お知らせの追加は news_data.js で管理してください。
Googleフォームのリンクは元ページに埋込済みです。Googleフォームの設問文はGoogleフォーム管理画面で編集します。
ゲノムブラウザの研究データは原データを維持し、画面に固定表示される文言を編集対象にしています。

注意：元のHTML内にも初期表示用の文字が残っていますが、Chromeでは editable_text.js の文字が優先されます。
JavaScriptが実行されないiPadのファイルプレビューでは、旧初期表示のままになる場合があります。
