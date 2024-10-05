import pandas as pd

def forming_csv(input_file, output_file):
    # CSVファイルをDataFrameに読み込む
    df = pd.read_csv(input_file)

    # 無駄な空白の行を削除
    df_cleaned = df.dropna(how='all')  # すべてのカラムがNaNである行を削除

    # 出力CSVファイルに保存
    df_cleaned.to_csv(output_file, index=False)

    print(f"無駄な空白の行を削除したファイルが {output_file} に保存されました。")

forming_csv(input_file="output_csv/Table1_1.csv", output_file="output_csv/Table1_1_cleaned.csv")