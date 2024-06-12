import os
import cv2
import numpy as np
from sklearn.preprocessing import LabelEncoder
import pickle
from keras_facenet import FaceNet
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Flatten, Conv2D, MaxPooling2D
from ultralytics import YOLO

# Suppress TensorFlow logs
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

# Load FaceNet model
facenet = FaceNet()
faces_embeddings = np.load("models/facenet/faces_embeddings_done_4classes.npz")
Y = faces_embeddings['arr_1']
encoder = LabelEncoder()
encoder.fit(Y)
svm_model = pickle.load(open("models/facenet/svm_model.pkl", 'rb'))

# Load emotion recognition model
emotion_model = Sequential([
    Conv2D(32, kernel_size=(3, 3), activation='relu', input_shape=(48, 48, 1)),
    Conv2D(64, kernel_size=(3, 3), activation='relu'),
    MaxPooling2D(pool_size=(2, 2)),
    Dropout(0.25),
    Conv2D(128, kernel_size=(3, 3), activation='relu'),
    MaxPooling2D(pool_size=(2, 2)),
    Conv2D(128, kernel_size=(3, 3), activation='relu'),
    MaxPooling2D(pool_size=(2, 2)),
    Dropout(0.25),
    Flatten(),
    Dense(1024, activation='relu'),
    Dropout(0.5),
    Dense(3, activation='softmax')
])
emotion_model.load_weights(os.path.join('models', 'model.h5'))

# Load YOLO model
yolo_model = YOLO(os.path.join('models', 'yolov8n-face.pt'))

# Emotion dictionary
emotion_dict = {0: "Happy", 1: "Sad", 2: "Surprised"}

# Start webcam feed
cap = cv2.VideoCapture(0)
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Use YOLO to detect faces
    results = yolo_model(frame)[0]
    for result in results.boxes.data.tolist():
        x1, y1, x2, y2, score, class_id = result
        if score > 0.5 and results.names[int(class_id)] == 'face':
            face_img = frame[int(y1):int(y2), int(x1):int(x2)]

            # Use FaceNet and SVM for face recognition
            face_img_resized = cv2.resize(face_img, (160, 160))
            face_img_expanded = np.expand_dims(face_img_resized, axis=0)
            face_embedding = facenet.embeddings(face_img_expanded)
            face_name = svm_model.predict(face_embedding)
            final_name = encoder.inverse_transform(face_name)[0]

            # Use emotion recognition model
            roi_gray = cv2.cvtColor(face_img, cv2.COLOR_BGR2GRAY)
            roi_resized = cv2.resize(roi_gray, (48, 48))
            cropped_img = np.expand_dims(np.expand_dims(roi_resized, -1), 0)
            prediction = emotion_model.predict(cropped_img)
            maxindex = int(np.argmax(prediction))
            emotion = emotion_dict[maxindex]

            # Draw bounding box and labels
            cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (255, 0, 255), 2)
            cv2.putText(frame, f"{final_name}: {emotion}", (int(x1), int(y1) - 10), cv2.FONT_HERSHEY_SIMPLEX,
                        1, (0, 0, 255), 2, cv2.LINE_AA)

    cv2.imshow("Face Recognition and Emotion Detection", frame)

    # Check for 'q' key press to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
