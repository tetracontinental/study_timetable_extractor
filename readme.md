# リポジトリ名

このリポジトリは、ブラウザからGoogle Driveにアクセスし、PDFファイルをCSV形式に変換するツールです。また、変換されたCSVファイルをGoogle Calendarに自動的に追加する機能も備えています。



## インストール

以下の手順に従って、このツールをインストールしてください。

1. リポジトリをクローンします。

```bash
git clone https://github.com/your-username/your-repo.git
```

2. 必要なパッケージをインストールします。

```bash
pip install -r requirements.txt
```

## 使い方

1. ブラウザでGoogle Driveにアクセスし、変換したいPDFファイルをアップロードします。

2. ターミナルで以下のコマンドを実行します。

```bash
python convert.py --input /path/to/pdf/file.pdf --output /path/to/csv/file.csv
```

3. 変換されたCSVファイルが指定した出力パスに保存されます。

4. Google CalendarにCSVファイルを自動的に追加するために、以下のコマンドを実行します。

```bash
python add-to-calendar.py --csv /path/to/csv/file.csv
```

これにより、CSVファイルの内容がGoogle Calendarにイベントとして追加されます。

## ライセンス

このプロジェクトはMITライセンスのもとで公開されています。詳細については、[LICENSE](LICENSE)ファイルを参照してください。
