import os
import cv2
import numpy as np
import pickle
from mtcnn import MTCNN
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from keras_facenet import FaceNet


class FaceRecognizer:
    def __init__(self, model_path='svm_model.pkl', embeddings_path='faces_embeddings_done.npz'):
        self.detector = MTCNN()
        self.embedder = FaceNet()
        self.model_path = model_path
        self.embeddings_path = embeddings_path
        self.target_size = (160, 160)
        self.model = None
        self.encoder = None

    def extract_face(self, img):
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        x, y, w, h = self.detector.detect_faces(img_rgb)[0]['box']
        x, y = abs(x), abs(y)
        face = img_rgb[y:y + h, x:x + w]
        face_arr = cv2.resize(face, self.target_size)
        return face_arr

    def load_faces(self, dir):
        faces = []
        for im_name in os.listdir(dir):
            try:
                path = os.path.join(dir, im_name)
                img = cv2.imread(path)
                face = self.extract_face(img)
                faces.append(face)
            except Exception as e:
                print(f"Failed to load image {im_name}: {e}")
        return faces

    def load_classes(self, dataset_dir):
        X, Y = [], []
        for sub_dir in os.listdir(dataset_dir):
            path = os.path.join(dataset_dir, sub_dir)
            if os.path.isdir(path):
                faces = self.load_faces(path)
                labels = [sub_dir for _ in range(len(faces))]
                X.extend(faces)
                Y.extend(labels)
                print(f"Loaded {len(faces)} faces for class {sub_dir}")
        return np.asarray(X), np.asarray(Y)

    def get_embedding(self, face_img):
        face_img = face_img.astype('float32')
        face_img = np.expand_dims(face_img, axis=0)
        embedding = self.embedder.embeddings(face_img)
        return embedding[0]

    def prepare_embeddings(self, X):
        return np.asarray([self.get_embedding(face) for face in X])

    def train(self, dataset_dir):
        x, y = self.load_classes(dataset_dir)
        x_embeddings = self.prepare_embeddings(x)

        np.savez_compressed(self.embeddings_path, x_embeddings, y)

        self.encoder = LabelEncoder()
        self.encoder.fit(y)
        Y_encoded = self.encoder.transform(y)

        X_train, X_test, Y_train, Y_test = train_test_split(x_embeddings, Y_encoded, shuffle=True, random_state=17)

        self.model = SVC(kernel='linear', probability=True)
        self.model.fit(X_train, Y_train)

        with open(self.model_path, 'wb') as f:
            pickle.dump(self.model, f)

        print("Model trained and saved successfully.")
        del self.model
        del self.encoder
        del x_embeddings

    def predict(self, img):
        if self.model is None or self.encoder is None:
            with open(self.model_path, 'rb') as f:
                self.model = pickle.load(f)
            self.encoder = LabelEncoder()
            self.encoder.fit(np.load(self.embeddings_path)['arr_1'])

        face = self.extract_face(img)
        embedding = self.get_embedding(face)
        ypred = self.model.predict([embedding])
        return self.encoder.inverse_transform(ypred)[0]


# Example usage:
def register_face():
    face_recognizer = FaceRecognizer(model_path='models/facenet/svm_model.pkl',
                                     embeddings_path='models/facenet/faces_embeddings_done_4classes.npz')
    # Train with new dataset
    face_recognizer.train("dataset")