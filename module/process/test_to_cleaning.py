import pandas as pd

def clean_csv(input_file, output_file):
    # CSVファイルを読み込む
    df = pd.read_csv(input_file, header=None)
    
    # 行をループして処理
    for i in range(1, len(df)):
        # 行が1つだけ項目を持つ場合
        if df.iloc[i].isnull().sum() == len(df.columns) - 1:
            # 上の行の同じ列に追加
            for j in range(len(df.columns)):
                if pd.notna(df.iloc[i, j]):
                    df.iloc[i - 1, j] = str(df.iloc[i - 1, j]) + str(df.iloc[i, j])
                    break  # 1つの項目が見つかったら処理を終える
            df.drop(i, inplace=True)  # 現在の行を削除

    # CSVファイルとして保存
    df.to_csv(output_file, index=False, header=False)

# 使用例
input_file = 'input.csv'  # 入力CSVファイル名
output_file = 'output.csv'  # 出力CSVファイル名
clean_csv(input_file, output_file)
