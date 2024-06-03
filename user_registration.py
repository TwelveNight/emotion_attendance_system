import cv2
import os


def capture_face_from_frame(frame):
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    for (x, y, w, h) in faces:
        face_image = frame[y:y + h, x:x + w]
        return face_image
    return None


def register_user(user_id, frame):
    face_image = capture_face_from_frame(frame)
    if face_image is not None:
        os.makedirs(f"data/users/{user_id}", exist_ok=True)
        cv2.imwrite(f"data/users/{user_id}/face.jpg", face_image)
        print("User registered successfully.")
        return True
    else:
        print("No face detected. Registration failed.")
        return False
