from ultralytics import YOLO
import os


def capture_face_from_frame(frame):
    H, w, _ = frame.shape
    model_path = os.path.join('models', 'yolov8n-face.pt')

    model = YOLO(model_path)

    threshold = 0.5

    results = model(frame)[0]
    for result in results.boxes.data.tolist():
        x1, y1, x2, y2, score, class_id = result
        if score > threshold:
            return frame[int(y1) - 100:int(y2) + 50, int(x1) - 50:int(x2) + 50]
    print("No face detected.")
    return None
