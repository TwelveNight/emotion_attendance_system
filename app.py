from flask import Flask, render_template, Response, request, redirect, url_for, flash, jsonify
import os
import signal
import cv2
import tensorflow as tf
import torch

import face_matching
from attendance import view_attendance, save_attendance
from emotion_recognition import recognize_emotion
from user_register import register_face
from utils import save_frame
from flask_cors import CORS

os.environ["TF_GPU_ALLOCATOR"] = "cuda_malloc_async"
os.environ["TF_CPP_VMODULE"] = "gpu_process_state=10,gpu_cudamallocasync_allocator=10"

a = tf.zeros([], tf.float32)

app = Flask(__name__)
CORS(app)
CORS(app, resources={r"/*": {"origins": "*"}})  # 仅允许 http://example.com 访问
app.secret_key = 'secret_key'

camera = cv2.VideoCapture(0)
detected_face = None
global_frame = None

skip_landmarks = False


def gen_frames():
    global detected_face
    global global_frame
    global skip_landmarks

    while True:
        success, frame = camera.read()
        global_frame = frame
        if not success:
            break

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

@app.route('/get_video_feed_url')
def get_video_feed_url():
    video_feed_url = url_for('video_feed')
    return jsonify({'url': video_feed_url})


@app.route('/register', methods=['POST'])
def register():
    global global_frame, skip_landmarks
    data = request.get_json()
    user_id= data.get('username')
    face_count = 1

    if global_frame is None:
        flash("No frame available for capturing faces.")
        return redirect(url_for('index'))

    skip_landmarks = True

    while face_count <= 10:
        if global_frame is not None:
            face_count = save_frame(global_frame, user_id, image_counter=face_count)
        else:
            flash("No face detected.")
            break

    if face_count > 10:
        flash("User registered successfully.")
    else:
        flash("User registration failed. No face detected in some frames.")
    torch.cuda.empty_cache()
    register_face()

    skip_landmarks = False

    return redirect(url_for('index'))


@app.route('/check_in', methods=['POST'])
def check_in_route():
    global detected_face
    global global_frame
    global skip_landmarks

    skip_landmarks = True

    if global_frame is not None:
        user_id = face_matching.recognize_faces(global_frame)
        data = request.get_json()
        model_type = data.get('model_type')
        print(user_id)
        if user_id is not None:
            emotion = recognize_emotion(global_frame, model_type)
            save_attendance(user_id, "check-in", emotion)
            message = emotion
        else:
            message = "User not recognized."
    else:
        message = "No face detected."

    skip_landmarks = False

    return message


@app.route('/check_out', methods=['POST'])
def check_out_route():
    global detected_face
    global global_frame
    global skip_landmarks

    skip_landmarks = True

    if global_frame is not None:
        user_id = face_matching.recognize_faces(global_frame)
        data = request.get_json()
        model_type = data.get('model_type')
        if user_id is not None:
            emotion = recognize_emotion(global_frame, model_type)
            save_attendance(user_id, "check-out", emotion)
            message = "Success:" + emotion
        else:
            message = "User not recognized."
    else:
        message = "No face detected."

    skip_landmarks = False

    return message


@app.route('/view_attendance')
def view_attendance_route():
    attendance_data = view_attendance().iloc[::-1]
    return render_template('attendance.html', data=attendance_data)


@app.route('/terminate', methods=['POST'])
def terminate():
    pid = os.getpid()
    os.kill(pid, signal.SIGTERM)
    return 'Application terminated'


if __name__ == '__main__':
    app.run(debug=True, port=8088)
