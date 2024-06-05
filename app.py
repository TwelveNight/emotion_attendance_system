from flask import Flask, render_template, Response, request, redirect, url_for, flash
from attendance import view_attendance, save_attendance, find_user
from train.train_sklearn_emotion.utils import get_face_landmarks
from user_registration import register_user
from emotion_recognition import recognize_emotion
import pickle
import cv2
import os
import tensorflow as tf

os.environ["TF_GPU_ALLOCATOR"] = "cuda_malloc_async"
os.environ["TF_CPP_VMODULE"] = "gpu_process_state=10,gpu_cudamallocasync_allocator=10"

a = tf.zeros([], tf.float32)

app = Flask(__name__)
app.secret_key = 'secret_key'

camera = cv2.VideoCapture(0)
detected_face = None
global_frame = None

emotions = ['happy', 'sad', 'surprised']

with open('models/model.pkl', 'rb') as f:
    model = pickle.load(f)


def gen_frames():
    global detected_face
    global global_frame
    # face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_alt2.xml')

    while True:
        success, frame = camera.read()
        global_frame = frame
        if not success:
            break
        else:
            face_landmarks = get_face_landmarks(frame, draw=False, static_image_mode=False)
            if face_landmarks:
                output = model.predict([face_landmarks])
                cv2.putText(global_frame,
                            emotions[int(output[0])],
                            (10, frame.shape[0] - 1),
                            cv2.FONT_HERSHEY_SIMPLEX,
                            3,
                            (0, 255, 0),
                            5)

            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/register', methods=['POST'])
def register():
    global detected_face
    global global_frame
    user_id = request.form['user_id']
    if global_frame is not None:
        success = register_user(user_id, global_frame)
        if success:
            flash("User registered successfully.")
        else:
            flash("User registration failed. No face detected.")
    else:
        flash("No face detected.")
    return redirect(url_for('index'))


@app.route('/check_in', methods=['POST'])
def check_in_route():
    global detected_face
    global global_frame
    if global_frame is not None:
        model_type = request.form['model_type']
        user_id = find_user(global_frame)
        print(user_id)
        if user_id is not None:
            emotion = recognize_emotion(global_frame, model_type)
            print(emotion)
            save_attendance(user_id, "check-in", emotion)
            message = "Check-in successful."
        else:
            message = "User not recognized."
    else:
        message = "No face detected."
    return render_template('message.html', message=message)


@app.route('/check_out', methods=['POST'])
def check_out_route():
    global detected_face
    global global_frame
    if global_frame is not None:
        model_type = request.form['model_type']
        user_id = find_user(global_frame)
        if user_id is not None:
            emotion = recognize_emotion(global_frame, model_type)
            save_attendance(user_id, "check-out", emotion)
            message = "Check-out successful."
        else:
            message = "User not recognized."
    else:
        message = "No face detected."
    return render_template('message.html', message=message)


@app.route('/view_attendance')
def view_attendance_route():
    attendance_data = view_attendance()
    return render_template('attendance.html', data=attendance_data)


if __name__ == '__main__':
    app.run(debug=True, port=8088)
