import cv2
import os


def save_frame(frame, name, save_dir="dataset", image_counter=1):
    # Set the directory and name to save images
    save_path = os.path.join(save_dir, name)
    if not os.path.exists(save_path):
        os.makedirs(save_path)

    # Save the current frame
    image_name = f"{name}_{image_counter}.jpg"
    image_path = os.path.join(save_path, image_name)
    cv2.imencode('.jpg', frame)[1].tofile(
        image_path)  # Use tofile method to save the image, ensuring correct handling of characters
    print(f"Save image: {image_name}")
    return image_counter + 1  # Return the next image counter


def register_user(user_id, frame):
    cv2.imwrite('ipynb_test/test.jpg', frame)
    if frame is not None:
        os.makedirs(f"data/users/{user_id}", exist_ok=True)
        cv2.imwrite(f"data/users/{user_id}/face.jpg", frame)
        print("User registered successfully.")
        return True
    else:
        print("No face detected. Registration failed.")
        return False
