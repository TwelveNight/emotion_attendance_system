from ultralytics import YOLO


if __name__ == '__main__':
    # Load a model
    model = YOLO("yolov8n.yaml")  # build a new model from scratch

    # Use the model
    results = model.train(data="data.yaml", epochs=50)  # train the model
