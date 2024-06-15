import cv2
import numpy as np
import os
from sklearn.preprocessing import LabelEncoder
import pickle
from keras_facenet import FaceNet
from ultralytics import YOLO

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'  # tensorflow log level
facenet = FaceNet()
# faces_embeddings = np.load("../../models/facenet/faces_embeddings_done_4classes.npz")
faces_embeddings = np.load("faces_embeddings_done_4classes.npz")
Y = faces_embeddings['arr_1']  # labels
encoder = LabelEncoder()
encoder.fit(Y)
# model = pickle.load(open("../../models/facenet/svm_model.pkl", 'rb'))
model = pickle.load(open("svm_model_test.pkl", 'rb'))

model_path = os.path.join('..', '..', 'models', 'yolov8n-face.pt')
yolo_model = YOLO(model_path)

cap = cv2.VideoCapture(0)
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # 使用YOLO检测人脸
    results = yolo_model(frame)[0]
    for result in results.boxes.data.tolist():
        x1, y1, x2, y2, score, class_id = result
        if score > 0.5 and results.names[int(class_id)] == 'face':
            face_img = frame[int(y1):int(y2), int(x1):int(x2)]

            # 使用FaceNet和SVM进行人脸识别
            face_img = cv2.resize(face_img, (160, 160))
            face_img = np.expand_dims(face_img, axis=0)
            face_embedding = facenet.embeddings(face_img)  # 512D
            face_name = model.predict(face_embedding)
            final_name = encoder.inverse_transform(face_name)[0]

            cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (255, 0, 255), 2)
            cv2.putText(frame, str(final_name), (int(x1), int(y1 - 10)), cv2.FONT_HERSHEY_SIMPLEX,
                        1, (0, 0, 255), 2, cv2.LINE_AA)

    cv2.imshow("Face Recognition", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
