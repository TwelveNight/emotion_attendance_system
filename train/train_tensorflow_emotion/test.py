import numpy as np
import cv2
import os
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Flatten, Conv2D, MaxPooling2D
from ultralytics import YOLO

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

base_dir = os.path.dirname(os.path.abspath(__file__))
model_dir = os.path.join(base_dir, '../../models')
model_path = os.path.join(model_dir, 'model.h5')
yolo_model_path = os.path.join(model_dir, 'yolov8n-face.pt')

# Load emotion recognition model
emotion_model = Sequential()
emotion_model.add(Conv2D(32, kernel_size=(3, 3), activation='relu', input_shape=(48, 48, 1)))
emotion_model.add(Conv2D(64, kernel_size=(3, 3), activation='relu'))
emotion_model.add(MaxPooling2D(pool_size=(2, 2)))
emotion_model.add(Dropout(0.25))
emotion_model.add(Conv2D(128, kernel_size=(3, 3), activation='relu'))
emotion_model.add(MaxPooling2D(pool_size=(2, 2)))
emotion_model.add(Conv2D(128, kernel_size=(3, 3), activation='relu'))
emotion_model.add(MaxPooling2D(pool_size=(2, 2)))
emotion_model.add(Dropout(0.25))
emotion_model.add(Flatten())
emotion_model.add(Dense(1024, activation='relu'))
emotion_model.add(Dropout(0.5))
emotion_model.add(Dense(3, activation='softmax'))
emotion_model.load_weights(model_path)

# Load YOLO model
yolo_model = YOLO(yolo_model_path)

# Dictionary which assigns each label an emotion (alphabetical order)
emotion_dict = {0: "Happy", 1: "Sad", 2: "Surprised"}

# Start the webcam feed
cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Use YOLO to detect faces
    results = yolo_model(frame)[0]
    threshold = 0.5

    for result in results.boxes.data.tolist():
        x1, y1, x2, y2, score, class_id = result
        if score > threshold:
            # Draw bounding box
            cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 4)

            # Emotion recognition
            roi_gray = cv2.cvtColor(frame[int(y1):int(y2), int(x1):int(x2)], cv2.COLOR_BGR2GRAY)
            cropped_img = np.expand_dims(np.expand_dims(cv2.resize(roi_gray, (48, 48)), -1), 0)
            prediction = emotion_model.predict(cropped_img)
            maxindex = int(np.argmax(prediction))
            cv2.putText(frame, emotion_dict[maxindex], (int(x1), int(y1) - 10), cv2.FONT_HERSHEY_SIMPLEX, 1.3,
                        (255, 255, 255), 3, cv2.LINE_AA)

    cv2.imshow('Video', frame)

    # Check for 'q' key press to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
