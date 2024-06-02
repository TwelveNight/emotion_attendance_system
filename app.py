from flask import Flask, render_template, Response, request, redirect, url_for
import cv2
from user_registration import register_user, capture_face
from attendance import check_in, check_out, view_attendance

app = Flask(__name__)

camera = cv2.VideoCapture(0)


def gen_frames():
    while True:
        success, frame = camera.read()
        if not success:
            break
        else:
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


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        user_id = request.form['user_id']
        register_user(user_id)
        return redirect(url_for('index'))
    return render_template('register.html')


@app.route('/check_in', methods=['POST'])
def check_in_route():
    user_id = request.form['user_id']
    model_type = request.form['model_type']
    check_in(user_id, model_type)
    return redirect(url_for('index'))


@app.route('/check_out', methods=['POST'])
def check_out_route():
    user_id = request.form['user_id']
    model_type = request.form['model_type']
    check_out(user_id, model_type)
    return redirect(url_for('index'))


@app.route('/view_attendance')
def view_attendance_route():
    attendance_data = view_attendance()
    return render_template('attendance.html', data=attendance_data)


if __name__ == '__main__':
    app.run(debug=True)
