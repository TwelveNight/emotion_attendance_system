import cv2
import os


def capture_faces(frame, name, save_dir="dataset", num_images=10):
    """
    Capture faces from the provided frame and save them to a specified directory.

    Parameters:
    - frame (numpy.ndarray): The frame from which to detect and save faces.
    - name (str): Name of the person to label the saved images.
    - save_dir (str): Directory where the images will be saved. Default is 'dataset'.
    - num_images (int): Number of images to capture. Default is 10.
    """
    # Load face detector
    faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_alt2.xml")

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
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(35, 35)
        )

        # Display the current number of saved images
        cv2.putText(frame, f"saved_num: {saved_images}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)

        # Save the image only if one face is detected and detection is correct
        if len(faces) == 1:
            (x, y, w, h) = faces[0]
            # cv2.rectangle(frame, (x, y), (x + w, y + h), (50, 50, 200), 2)
            if time_cnt == 0:
                # Save the current frame
                image_name = f"{name}_{image_counter}.jpg"
                image_path = os.path.join(save_path, image_name)
                cv2.imencode('.jpg', frame)[1].tofile(
                    image_path)  # Use tofile method to save the image, ensuring correct handling of Chinese characters
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


# Example usage:
name = input("Please enter name: ")

# Open the webcam
video_capture = cv2.VideoCapture(0)

while True:
    retval, frame = video_capture.read()
    if not retval:
        print("No video capture read")
        break

    saved_images = capture_faces(frame, name)

    cv2.imshow('Camera', frame)

    key = cv2.waitKey(1) & 0xFF
    if key == ord('q') or saved_images >= 10:
        break

# Release the webcam and close all windows
video_capture.release()
cv2.destroyAllWindows()
