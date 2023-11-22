import zipfile

zip_file_path="sample.zip"

# zipファイルの読み込み

    

# 奇数のファイル名から数字を取得して合計を計算
total_sum = 0
# zipファイルの読み込み
with zipfile.ZipFile(zip_file_path, 'r') as zip_file:
    zipfiles=zip_file.namelist()
    for filename in zipfiles:
        if filename.startswith('sample/kitamura_') and filename.endswith('_kgu.txt'):
            file_number = int(filename.split('_')[1])
            if file_number % 2 == 1:#奇数名のみ
                with zip_file.open(filename, 'r') as file:
                    numbers = [int(line.strip()) for line in file]
                    total_sum += sum(numbers)

# 結果を表示
print(f'Total sum of numbers in files with odd filenames: {total_sum}')

