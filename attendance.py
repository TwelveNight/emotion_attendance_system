import pandas as pd
import os
from deepface import DeepFace


def find_user(face_image):
    # 假设我们的人脸数据保存在 "data/users/" 目录下，每个用户一个文件夹，文件夹名为用户ID
    user_id = None
    for user_folder in os.listdir("data/users/"):
        user_face_path = f"data/users/{user_folder}"
        result = DeepFace.find(img_path=face_image, db_path=user_face_path, enforce_detection=False)
        if len(result[0]['identity']) > 0:
            user_id = user_folder
            break
    return user_id


def save_attendance(user_id, status, emotion):
    df = pd.DataFrame(columns=["user_id", "time", "status", "emotion"])
    df.loc[len(df)] = [user_id, pd.Timestamp.now(), status, emotion]
    print("Saving data: ", df)
    df.to_csv("data/attendance.csv", mode='a', header=False, index=False)


def view_attendance():
    if os.path.exists("data/attendance.csv"):
        df = pd.read_csv("data/attendance.csv", names=["user_id", "time", "status", "emotion"])
        print("Loaded data: ", df)
        return df
    else:
        print("attendance.csv not found")
        return pd.DataFrame(columns=["user_id", "time", "status", "emotion"])
