import json
import zipfile
import os

zip_file_path="kabeposter.zip"

# zipファイルの読み込み
with zipfile.ZipFile(zip_file_path, 'r') as zipfile:
    zipfiles=zipfile.namelist()
    for filename in zipfiles:
        if filename.endswith('00_keypoints.json'):
        
            with zipfile.open(filename, 'r') as file:
                data = json.load(file)
                
# 2人の人に対する鼻と首の情報を表示
for person_id in range(2):
    nose_keypoint = data["people"][person_id]["pose_keypoints_2d"][0:3]
    neck_keypoint = data["people"][person_id]["pose_keypoints_2d"][3:6]

    # 鼻の座標と信頼度
    nose_x, nose_y, nose_confidence = nose_keypoint
    print(f"Person {person_id + 1} - Nose: X={nose_x}, Y={nose_y}, Confidence={nose_confidence}")

    # 首の座標と信頼度
    neck_x, neck_y, neck_confidence = neck_keypoint
    print(f"Person {person_id + 1} - Neck: X={neck_x}, Y={neck_y}, Confidence={neck_confidence}")

    print("\n")