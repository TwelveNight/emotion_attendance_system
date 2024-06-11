import os

from mtcnn import MTCNN
import cv2
import numpy as np
import matplotlib.pyplot as plt
import pickle
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from keras_facenet import FaceNet


class FACELOADING:
    def __init__(self, directory):
        self.directory = directory
        self.target_size = (160, 160)
        self.X = []
        self.Y = []
        self.detector = MTCNN()

    def extract_face(self, filename):
        img = cv2.imread(filename)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        x, y, w, h = self.detector.detect_faces(img)[0]['box']
        x, y = abs(x), abs(y)
        face = img[y:y + h, x:x + w]
        face_arr = cv2.resize(face, self.target_size)
        return face_arr

    def load_faces(self, dir):
        faces = []
        for im_name in os.listdir(dir):
            try:
                path = dir + im_name
                single_face = self.extract_face(path)
                faces.append(single_face)
            except Exception as e:
                pass
        return faces

    def load_classes(self):
        for sub_dir in os.listdir(self.directory):
            path = self.directory + '/' + sub_dir + '/'
            FACES = self.load_faces(path)
            labels = [sub_dir for _ in range(len(FACES))]
            print(f"Loaded successfully: {len(labels)}")
            self.X.extend(FACES)
            self.Y.extend(labels)

        return np.asarray(self.X), np.asarray(self.Y)

    def plot_images(self):
        plt.figure(figsize=(18, 16))
        for num, image in enumerate(self.X):
            ncols = 3
            nrows = len(self.Y) // ncols + 1
            plt.subplot(nrows, ncols, num + 1)
            plt.imshow(image)
            plt.axis('off')


detector = MTCNN()
faceloading = FACELOADING("dataset")
X, Y = faceloading.load_classes()
print(Y)

embedder = FaceNet()


def get_embedding(face_img):
    face_img = face_img.astype('float32')  # 3D(160x160x3)
    face_img = np.expand_dims(face_img, axis=0)
    # 4D (Nonex160x160x3)
    yhat = embedder.embeddings(face_img)
    return yhat[0]  # 512D image (1x1x512)


EMBEDDED_X = []

for img in X:
    EMBEDDED_X.append(get_embedding(img))

EMBEDDED_X = np.asarray(EMBEDDED_X)

np.savez_compressed('faces_embeddings_done_4classes_test.npz', EMBEDDED_X, Y)

encoder = LabelEncoder()
encoder.fit(Y)
Y = encoder.transform(Y)

X_train, X_test, Y_train, Y_test = train_test_split(EMBEDDED_X, Y, shuffle=True, random_state=17)

model = SVC(kernel='linear', probability=True)
model.fit(X_train, Y_train)

t_im = cv2.imread("face.jpg")
t_im = cv2.cvtColor(t_im, cv2.COLOR_BGR2RGB)
x, y, w, h = detector.detect_faces(t_im)[0]['box']

t_im = t_im[y:y + h, x:x + w]
t_im = cv2.resize(t_im, (160, 160))

test_im = get_embedding(t_im)
test_im = [test_im]

ypreds = model.predict(test_im)
encoder.inverse_transform(ypreds)
print(ypreds)

#save the model
with open('svm_model_test.pkl', 'wb') as f:
    pickle.dump(model, f)
