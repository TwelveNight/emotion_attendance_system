import pandas as pd
import os
from deepface import DeepFace
from emotion_recognition import recognize_emotion
from user_registration import capture_face


def find_user(face_image):
    # 假设我们的人脸数据保存在 "data/users/" 目录下，每个用户一个文件夹，文件夹名为用户ID
    user_id = None
    for user_folder in os.listdir("data/users/"):
        user_face_path = f"data/users/{user_folder}/face.jpg"
        result = DeepFace.find(img_path=face_image, db_path=user_face_path, enforce_detection=False)
        if len(result) > 0:
            user_id = user_folder
            break
    return user_id


def check_in(model_type='pkl'):
    face_image = capture_face()
    user_id = find_user(face_image)
    if user_id:
        emotion = recognize_emotion(face_image, model_type)
        if emotion == "Happy":
            save_attendance(user_id, "check-in")
            return "Check-in successful."
        else:
            return "Check-in failed. Please be happy!"
    return "User not recognized."


def check_out(model_type='pkl'):
    face_image = capture_face()
    user_id = find_user(face_image)
    if user_id:
        emotion = recognize_emotion(face_image, model_type)
        if emotion == "Happy":
            save_attendance(user_id, "check-out")
            return "Check-out successful."
        else:
            return "Check-out failed. Please be happy!"
    return "User not recognized."


def save_attendance(user_id, status):
    df = pd.DataFrame(columns=["user_id", "time", "status"])
    df.loc[len(df)] = [user_id, pd.Timestamp.now(), status]
    df.to_csv("data/attendance.csv", mode='a', header=False, index=False)


def view_attendance():
    df = pd.read_csv("data/attendance.csv")
    return df
