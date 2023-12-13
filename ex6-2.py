import json
import zipfile
import os
import tkinter as tk

zip_file_path="kabeposter.zip"

# zipファイルの読み込み
with zipfile.ZipFile(zip_file_path, 'r') as zipfile:
    zipfiles=zipfile.namelist()
    for filename in zipfiles:
        if filename.endswith('00_keypoints.json'):
        
            with zipfile.open(filename, 'r') as file:
                data = json.load(file)
# 0フレーム目の肩の座標（例として左肩、右肩のX座標を使用）
# 2人の人に対する鼻と首の情報を表示

def draw_shoulder_line(canvas, coordinates1, coordinates2):
    # 肩のラインを描画する関数
    canvas.create_line(coordinates1[0], coordinates1[1], coordinates2[0], coordinates2[1], fill="red", width=2)

# ウィンドウの作成
window = tk.Tk()
window.title("Shoulder Line")

# キャンバスの作成
canvas = tk.Canvas(window, width=400, height=400)
canvas.pack()

# 2人の人の0フレーム目における肩の座標（仮のデータ）
for person_id in range(2):
    left_x_shoulder_keypoint = data["people"][person_id]["pose_keypoints_2d"][5*3]/7
    right_x_shoulder_keypoint = data["people"][person_id]["pose_keypoints_2d"][2*3]/7
    left_y_shoulder_keypoint = data["people"][person_id]["pose_keypoints_2d"][5*3+1]/7
    right_y_shoulder_keypoint = data["people"][person_id]["pose_keypoints_2d"][2*3+1]/7

# 肩のラインを描画
    canvas.create_oval(right_x_shoulder_keypoint-2, right_y_shoulder_keypoint-2, right_x_shoulder_keypoint+2, right_y_shoulder_keypoint+2, outline="black", width=2)
    canvas.create_oval(left_x_shoulder_keypoint-2, left_y_shoulder_keypoint-2, left_x_shoulder_keypoint+2, left_y_shoulder_keypoint+2, outline="black", width=2)
    canvas.create_line(left_x_shoulder_keypoint, left_y_shoulder_keypoint, right_x_shoulder_keypoint, right_y_shoulder_keypoint, fill="black", width=2)

# ウィンドウの表示
window.mainloop()
"""
for person_id in range(1,2):
    left_shoulder_keypoint = data["people"][person_id]["pose_keypoints_2d"][0:2]
    right_shoulder_keypoint = data["people"][person_id]["pose_keypoints_2d"][3:5]

    # 左肩の座標
    left_shoulder_x, left_shoulder_y= left_shoulder_keypoint
    #print(f"Person {person_id + 1} - Nose: X={left_shoulder_x}, Y={left_shoulder_y}")
    # 右肩の座標
    right_shoulder_x, right_shoulder_y = right_shoulder_keypoint
    #print(f"Person {person_id + 1} - Neck: X={right_shoulder_x}, Y={right_shoulder_y}")
    plt.plot([left_shoulder_x,right_shoulder_x],[left_shoulder_y,right_shoulder_y])
    plt.show()
    
#plt.plot([])

# ウィンドウを生成して肩のラインを描画
image = np.zeros((500, 500, 3), dtype=np.uint8)  # 仮の画像サイズ
cv2.line(image, (shoulder_x_person1, shoulder_y_person1), (shoulder_x_person2, shoulder_y_person2), (255, 255, 255), 2)

# ウィンドウに画像を表示
cv2.imshow('Shoulder Line', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
"""