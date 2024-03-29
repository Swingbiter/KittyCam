from flask import Flask, render_template, request, Response
import cv2

app = Flask(__name__)

# camera stuff
camera = cv2.VideoCapture(0)
def gen_frames():
    while True:
        success, frame = camera.read()
        if not success:
            break
        else:
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield(b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

# routes
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/login', methods=['POST'])
def login():
    if request.form['pswd'] == "poopersnooper":
        return render_template('stream.html')
    else:
        return "frig off"

@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

# do the thing
if __name__ == "__main__":
    app.run(host='0.0.0.0')