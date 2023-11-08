# ファイル名
file_name = 'data1.txt'

# 合計を保持する変数
total = 0

# ファイルを開いて行ごとに処理
with open(file_name, 'r') as file:
    for line in file:
        # 行から不要な空白文字を取り除く
        #line = line.strip()
        line.replace(" ","")
        # 行が空でない場合
        if line:
            try:
                # 行を整数に変換し、合計に加える
                total += int(line)
            except ValueError:
                # 整数に変換できない場合は無視
                pass

# 合計を出力
print('合計:', total)
