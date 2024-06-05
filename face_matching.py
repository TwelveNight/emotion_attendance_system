import cv2 as cv
import numpy as np
import os
import face_detection
from sklearn.preprocessing import LabelEncoder
import pickle
from keras_facenet import FaceNet
import torch

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'


def recognize_faces(frame):
    facenet = FaceNet()
    faces_embeddings = np.load("models/facenet/faces_embeddings_done_4classes.npz")
    Y = faces_embeddings['arr_1']
    encoder = LabelEncoder()
    encoder.fit(Y)
    model = pickle.load(open("models/facenet/svm_model.pkl", 'rb'))

    face_img = face_detection.capture_face_from_frame(frame)
    torch.cuda.empty_cache()
    if face_img is not None:
        img = cv.resize(face_img, (160, 160))  # 1x160x160x3
        img = np.expand_dims(img, axis=0)
        ypred = facenet.embeddings(img)
        face_name = model.predict(ypred)
        final_name = encoder.inverse_transform(face_name)[0]

        # release
        del facenet
        del model

        return final_name
    else:
        print("No face detected or recognition failed.")
        return None
