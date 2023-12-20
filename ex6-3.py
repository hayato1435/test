import json
import zipfile
import os
import tkinter as tk

zip_file_path="kabeposter.zip"

datas = []  # dataリスト

# zipファイルの読み込み
with zipfile.ZipFile(zip_file_path, 'r') as zipfile:
    zipfiles=zipfile.namelist()
    for filename in zipfiles:
        if filename.endswith('keypoints.json'):
        
            with zipfile.open(filename, 'r') as file:
                data = json.load(file)
                datas.append(data)

# ウィンドウの作成
window = tk.Tk()
window.title("Animation Example")

# キャンバスの作成
canvas = tk.Canvas(window, width=400, height=400)
canvas.pack()



 



def draw(frame):

    # すべてのデータを描画すれば終了

    if frame >= len(datas):

        return

 

    # 前のフレームの削除

    canvas.delete("all")

 

    # 骨格座標の描画

    for i in range(2):

        for j in range(25):

            # ドットを描く

            X = datas[frame]["people"][i]["pose_keypoints_2d"][j * 3] /7

            Y = datas[frame]["people"][i]["pose_keypoints_2d"][j * 3 + 1] /7

            # X座標が0の場合は何も表示しない。

            if X != 0:

                canvas.create_oval(

                    X - 3,

                    Y - 3,

                    X + 3,

                    Y + 3,

                    fill="black",

                    tag="all",

                )

 

        # 線で結ばれた頂点の集合

        connects = [

            (0, 1),

            (0, 15),

            (0, 16),

            (1, 2),

            (1, 5),

            (1, 8),

            (2, 3),

            (3, 4),

            (5, 6),

            (6, 7),

            (8, 9),

            (8, 12),

            (9, 10),

            (10, 11),

            (11, 22),

            (11, 24),

            (12, 13),

            (13, 14),

            (14, 19),

            (14, 21),

            (15, 17),

            (16, 18),

            (19, 20),

            (22, 23),

        ]

 

        # 線を描く

        for s, e in connects:

            X1 = datas[frame]["people"][i]["pose_keypoints_2d"][s * 3] /7

            Y1 = datas[frame]["people"][i]["pose_keypoints_2d"][s * 3 + 1] /7

            X2 = datas[frame]["people"][i]["pose_keypoints_2d"][e * 3] /7

            Y2 = datas[frame]["people"][i]["pose_keypoints_2d"][e * 3 + 1] /7

 

            # X座標が0の場合は何も表示しない。

            if X1 != 0 and X2 != 0:

                canvas.create_line(X1, Y1, X2, Y2, tag="all")

 

    window.after(50, draw, frame + 1)

 

# 関数

draw(0)

 

# ウィンドウの表示

window.mainloop()

 