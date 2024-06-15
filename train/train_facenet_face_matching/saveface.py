import os
import cv2
from ultralytics import YOLO


def capture_faces_with_yolo(frame, name, model, save_dir="dataset", num_images=10, threshold=0.5):
    # Set the directory and name to save images
    save_path = os.path.join(save_dir, name)
    if not os.path.exists(save_path):
        os.makedirs(save_path)

    # Initialize image counter
    image_counter = 1

    # Image number
    saved_images = 0

    # Timer counter
    time_cnt = 0

    while saved_images < num_images:
        # Detect faces using YOLO model
        results = model(frame)[0]

        # Display the current number of saved images
        cv2.putText(frame, f"saved_num: {saved_images}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)

        # Save the image only if one face is detected and detection is correct
        for result in results.boxes.data.tolist():
            x1, y1, x2, y2, score, class_id = result

            if score > threshold:
                if time_cnt == 0:
                    # Crop the detected face
                    face = frame[int(y1):int(y2), int(x1):int(x2)]
                    # Save the cropped face
                    image_name = f"{name}_{image_counter}.jpg"
                    image_path = os.path.join(save_path, image_name)
                    cv2.imencode('.jpg', face)[1].tofile(image_path)  # Use tofile method to save the image
                    print(f"Save image: {image_name}")
                    image_counter += 1
                    saved_images += 1
                    time_cnt = 2  # Reset timer
                else:
                    time_cnt -= 1  # Timer countdown

        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            break

    print("Images saved successfully!")
    return saved_images  # Return the number of saved images


# Load the YOLO model
model_path = os.path.join('..', '..', 'models', 'yolov8n-face.pt')
model = YOLO(model_path)

# Example usage:
name = input("Please enter name: ")

# Open the webcam
video_capture = cv2.VideoCapture(0)

while True:
    retval, frame = video_capture.read()
    if not retval:
        print("No video capture read")
        break

    saved_images = capture_faces_with_yolo(frame, name, model, num_images=10)

    cv2.imshow('Camera', frame)

    key = cv2.waitKey(1) & 0xFF
    if key == ord('q') or saved_images >= 10:
        break

# Release the webcam and close all windows
video_capture.release()
cv2.destroyAllWindows()
