import cv2
import os


def capture_face():
    cap = cv2.VideoCapture(0)
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    while True:
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

        cv2.imshow('Capture Face', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            if len(faces) > 0:
                x, y, w, h = faces[0]
                face_image = frame[y:y + h, x:x + w]
                break

    cap.release()
    cv2.destroyAllWindows()
    return face_image


def register_user(user_id):
    face_image = capture_face()
    os.makedirs(f"data/users/{user_id}", exist_ok=True)
    cv2.imwrite(f"data/users/{user_id}/face.jpg", face_image)
    print("User registered successfully.")
