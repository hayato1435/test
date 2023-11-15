import json

# JSONファイルからデータを読み込む
#file_name = "catalog.json"  # JSONファイル名を指定

with open('catalog.json','r') as file:
    data = json.load(file)

# "jacket" の個数
jacket_count = sum(1 for item in data if item['name']=='jacket')
print("jacketの個数:", jacket_count)

jacket_items=[item for item in data if item['name']=='jacket']
# 最高価格と最低価格
max_price_item = max(jacket_items,key=lambda x: x['price'])
min_price_item = min(jacket_items,key=lambda x: x['price'])

max_price=max_price_item['price']
min_price=min_price_item['price']


print(f"jacketの最高価格: {max_price}")
print(f"jacketの最低価格: {min_price}")
