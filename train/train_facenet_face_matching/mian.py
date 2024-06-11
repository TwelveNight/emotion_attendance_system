import cv2
import numpy as np
import os
from sklearn.preprocessing import LabelEncoder
import pickle
from keras_facenet import FaceNet

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

facenet = FaceNet()
faces_embeddings = np.load("../../models/facenet/faces_embeddings_done_4classes.npz")
Y = faces_embeddings['arr_1']
encoder = LabelEncoder()
encoder.fit(Y)
faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_alt2.xml")
model = pickle.load(open("../../models/facenet/svm_model.pkl", 'rb'))

cap = cv2.VideoCapture(0)

while cap.isOpened():
    _, frame = cap.read()
    rgb_img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    gray_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(gray_img, 1.3, 5)
    for x, y, w, h in faces:
        img = rgb_img[y:y + h, x:x + w]
        img = cv2.resize(img, (160, 160))  # 1x160x160x3
        img = np.expand_dims(img, axis=0)
        ypred = facenet.embeddings(img)
        face_name = model.predict(ypred)
        final_name = encoder.inverse_transform(face_name)[0]
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 255), 10)
        cv2.putText(frame, str(final_name), (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX,
                   1, (0, 0, 255), 3, cv2.LINE_AA)

    cv2.imshow("Face Recognition:", frame)
    if cv2.waitKey(1) & ord('q') == 27:
        break

cap.release()

cv2.destroyAllWindows()
