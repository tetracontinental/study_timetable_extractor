import pandas as pd

def clean_csv(input_file, output_file):
    # CSVファイルを読み込む
    df = pd.read_csv(input_file, header=None)
    
    # 1列目を取得（1行目の処理をするため）
    col1 = df.iloc[:, 0]
    
    # 2列目以降のデータを取得
    data = df.iloc[:, 1:]
    
    # 1つしか項目がない行を処理
    for i in range(1, len(col1)):
        if pd.isna(col1[i]) and pd.notna(col1[i - 1]):
            col1[i - 1] = f"{col1[i - 1]} {data.iloc[i, 0]}"
            df.iloc[i, 0] = None  # 処理済みの行を削除するためにNoneを設定
    
    # NaN値を持つ行を削除
    df = df.dropna(how='all')
    
    # 2行目以降が月に関するデータで、月が異なるたびに区切りを作る
    new_rows = []
    month = ""
    for i in range(len(df)):
        if pd.notna(df.iloc[i, 0]) and any(char.isdigit() for char in df.iloc[i, 0]):
            if month:
                new_rows.append([month])
            month = df.iloc[i, 0]
        else:
            if new_rows:
                new_rows[-1].append(df.iloc[i, 0])
    
    if month:
        new_rows.append([month])
    
    # データフレームに変換して出力
    clean_df = pd.DataFrame(new_rows)
    clean_df.to_csv(output_file, index=False, header=False)

# 入力ファイルと出力ファイルのパスを指定
input_file = 'output_csv/Table1_1_cleaned.csv'
output_file = 'output_csv/Table1_1_cleaned.csv'

# CSVクリーニング関数を呼び出す
clean_csv(input_file, output_file)
