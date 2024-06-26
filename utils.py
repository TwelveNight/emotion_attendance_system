import os
import cv2
import face_detection


def save_frame(frame, name, save_dir="dataset", image_counter=1):
    # Set the directory and name to save images
    save_path = os.path.join(save_dir, name)
    if not os.path.exists(save_path):
        os.makedirs(save_path)

    # Save the current frame
    image_name = f"{name}_{image_counter}.jpg"
    image_path = os.path.join(save_path, image_name)
    face = face_detection.capture_face_from_frame(frame)
    cv2.imencode('.jpg', face)[1].tofile(
        image_path)  # Use tofile method to save the image, ensuring correct handling of characters
    print(f"Save image: {image_name}")
    return image_counter + 1  # Return the next image counter
