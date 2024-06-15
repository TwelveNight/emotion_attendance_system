import pickle

import cv2

from utils import get_face_landmarks

emotions = ['happy', 'sad', 'surprised']

with open('../../models/model.pkl', 'rb') as f:
# with open('../../models/svm_model.pkl', 'rb') as f:
    model = pickle.load(f)

# img = cv2.imread('check.jpg')
# face_landmarks = get_face_landmarks(img, draw=False, static_image_mode=True)
# if face_landmarks:
#     prediction = model.predict([face_landmarks])
#     print(emotions[int(prediction[0])])

cap = cv2.VideoCapture(0)

ret, global_frame = cap.read()

while ret:
    ret, global_frame = cap.read()

    face_landmarks = get_face_landmarks(global_frame, draw=True, static_image_mode=False)

    if face_landmarks:
        output = model.predict([face_landmarks])
        print(emotions[int(output[0])])
        cv2.putText(global_frame,
                    emotions[int(output[0])],
                    (10, global_frame.shape[0] - 1),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    3,
                    (0, 255, 0),
                    5)

    cv2.imshow('frame', global_frame)

    cv2.waitKey(25)

    if cv2.waitKey(25) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
