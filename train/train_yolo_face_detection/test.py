import os

from ultralytics import YOLO
import cv2

cap = cv2.VideoCapture(0)
ret, frame = cap.read()

while ret:
    ret, frame = cap.read()
    H, W, _ = frame.shape

    model_path = os.path.join('..', '..', 'models', 'yolov8n-face.pt')

    # Load a model
    model = YOLO(model_path)  # load a custom model

    threshold = 0.5

    results = model(frame)[0]

    for result in results.boxes.data.tolist():
        x1, y1, x2, y2, score, class_id = result

        if score > threshold:
            cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 4)
            cv2.putText(frame, results.names[int(class_id)].upper(), (int(x1), int(y1 - 10)),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv2.LINE_AA)

    cv2.imshow('frame', frame)
    cv2.waitKey(1)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()

cv2.destroyAllWindows()
