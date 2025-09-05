import os
import cv2
import numpy as np
import pickle
from mtcnn import MTCNN
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from keras_facenet import FaceNet
import shutil

class FaceRecognizer:
    def __init__(self, model_path='svm_model.pkl', embeddings_path='faces_embeddings_done.npz'):
        self.detector = MTCNN()
        self.embedder = FaceNet()
        self.model_path = model_path
        self.embeddings_path = embeddings_path
        self.target_size = (160, 160)
        self.model = None
        self.encoder = None
        self.load_model()

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

    def get_embedding(self, face_img):
        face_img = face_img.astype('float32')
        face_img = np.expand_dims(face_img, axis=0)
        embedding = self.embedder.embeddings(face_img)
        return embedding[0]

    def prepare_embeddings(self, X):
        return np.asarray([self.get_embedding(face) for face in X])

    def load_model(self):
        if os.path.exists(self.model_path):
            with open(self.model_path, 'rb') as f:
                self.model = pickle.load(f)
        if os.path.exists(self.embeddings_path):
            data = np.load(self.embeddings_path)
            X_emb = data['arr_0']
            Y = data['arr_1']
            self.encoder = LabelEncoder()
            self.encoder.fit(Y)

    def train_incremental(self, new_dataset_dir):
        # 加载新数据
        new_X, new_Y = [], []
        for sub_dir in os.listdir(new_dataset_dir):
            path = os.path.join(new_dataset_dir, sub_dir)
            if os.path.isdir(path):
                faces = self.load_faces(path)
                labels = [sub_dir for _ in range(len(faces))]
                new_X.extend(faces)
                new_Y.extend(labels)
                print(f"Loaded {len(faces)} faces for class {sub_dir}")

        new_X_emb = self.prepare_embeddings(new_X)

        if self.model is None:
            # 如果模型不存在，从头开始训练
            self.model = SVC(kernel='linear', probability=True)
            self.encoder = LabelEncoder()
            self.encoder.fit(new_Y)
            Y_encoded = self.encoder.transform(new_Y)
        else:
            # 增量训练
            new_Y_encoded = self.encoder.transform(new_Y)
            self.model.fit(np.vstack([self.model.support_vectors_, new_X_emb]),
                           np.hstack([self.model.support_  , new_Y_encoded]))

        # 合并新旧嵌入向量和标签
        if os.path.exists(self.embeddings_path):
            old_data = np.load(self.embeddings_path)
            old_X_emb = old_data['arr_0']
            old_Y = old_data['arr_1']
            combined_X_emb = np.vstack([old_X_emb, new_X_emb])
            combined_Y = np.hstack([old_Y, new_Y])
        else:
            combined_X_emb = new_X_emb
            combined_Y = new_Y

        np.savez_compressed(self.embeddings_path, combined_X_emb, combined_Y)

        with open(self.model_path, 'wb') as f:
            pickle.dump(self.model, f)

        print("Model updated and saved successfully.")

        # 删除新数据集文件夹
        if os.path.exists(new_dataset_dir):
            shutil.rmtree(new_dataset_dir)

    def predict(self, img):
        if self.model is None or self.encoder is None:
            self.load_model()

        face = self.extract_face(img)
        embedding = self.get_embedding(face)
        ypred = self.model.predict([embedding])
        return self.encoder.inverse_transform(ypred)[0]

# Example usage:
def register_face():
    face_recognizer = FaceRecognizer(model_path='models/facenet/svm_model.pkl',
                                     embeddings_path='models/facenet/faces_embeddings_done_4classes.npz')
    # 增量训练新数据集
    face_recognizer.train_incremental("new_dataset")
