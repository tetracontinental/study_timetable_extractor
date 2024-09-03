import os
from spire.pdf import PdfDocument, PdfTableExtractor
import csv

# 入力ディレクトリのパス
input_pdf_dir = "input_pdf/☆時間割変更-20240903T072808Z-001/☆時間割変更/"

# 出力ディレクトリのパス
output_csv_dir = "output_csv"

# 入力ディレクトリ内のPDFファイルを処理
for filename in os.listdir(input_pdf_dir):
    if filename.endswith(".pdf"):
        # PDFファイルのパス
        pdf_file_path = os.path.join(input_pdf_dir, filename)

        # PdfDocumentのインスタンスを作成
        pdf = PdfDocument()

        # PDFドキュメントをロード
        pdf.LoadFromFile(pdf_file_path)

        # PdfTableExtractorのインスタンスを作成
        extractor = PdfTableExtractor(pdf)

        # PDFドキュメントのページを反復処理
        for j in range(pdf.Pages.Count):
            # 現在のページからテーブルを抽出
            tables = extractor.ExtractTable(j)
            # テーブルを反復処理
            for k, table in enumerate(tables):
                tableData = []
                # 行数と列数を取得
                rowCount = table.GetRowCount()
                colCount = table.GetColumnCount()
                # 行と列を反復処理
                for row in range(rowCount):
                    rowData = []
                    for col in range(colCount):
                        # セルのテキストを取得
                        text = table.GetText(row, col)
                        text = text.replace("/n", "").replace("/r", "")
                        rowData.append(text)
                    tableData.append(rowData)
                # テーブルデータをCSVファイルに保存
                csv_file_path = f"{output_csv_dir}/Table{j+1}_{k+1}.csv"
                with open(csv_file_path, "w", newline="", encoding="utf-8") as csvFile:
                    writer = csv.writer(csvFile)
                    writer.writerows(tableData)

        # リソースを解放
        pdf.Dispose()
