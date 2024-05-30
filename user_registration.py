import cv2
import os
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'

def capture_face():
    # 这里省略OpenCV捕捉人脸图像的代码
    pass

def register_user():
    face_image = capture_face()
    # 保存人脸图像和特征（示例代码）
    user_id = "user123"
    os.makedirs(f"data/users/{user_id}", exist_ok=True)
    cv2.imwrite(f"data/users/{user_id}/face.jpg", face_image)
    print("User registered successfully.")
