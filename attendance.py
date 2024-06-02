import pandas as pd
import cv2
from emotion_recognition import recognize_emotion


def check_in(user_id, model_type='pkl'):
    face_image = cv2.imread(f"data/users/{user_id}/face.jpg")
    emotion = recognize_emotion(face_image, model_type)
    if emotion == "Happy":
        save_attendance(user_id, "check-in")
        print("Check-in successful.")
    else:
        print("Check-in failed. Please be happy!")


def check_out(user_id, model_type='pkl'):
    face_image = cv2.imread(f"data/users/{user_id}/face.jpg")
    emotion = recognize_emotion(face_image, model_type)
    if emotion == "Happy":
        save_attendance(user_id, "check-out")
        print("Check-out successful.")
    else:
        print("Check-out failed. Please be happy!")


def save_attendance(user_id, status):
    df = pd.DataFrame(columns=["user_id", "time", "status"])
    df.loc[len(df)] = [user_id, pd.Timestamp.now(), status]
    df.to_csv("data/attendance.csv", mode='a', header=False, index=False)


def view_attendance():
    df = pd.read_csv("data/attendance.csv")
    return df.to_html()
