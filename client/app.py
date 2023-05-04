import os
from flask import Flask, render_template, request, flash, redirect, url_for
from werkzeug.utils import secure_filename
import numpy as np
import cv2
import tensorflow as tf

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads/'
app.config['ALLOWED_EXTENSIONS'] = {'mp4'}

# Create the 'uploads' directory if it does not exist
if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

def analyze_video(video_path):
    frame_size = (224, 224)
    num_frames = 20

    video_frames = []
    cap = cv2.VideoCapture(video_path)
    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    step = frame_count // num_frames

    for i in range(0, frame_count, step):
        cap.set(cv2.CAP_PROP_POS_FRAMES, i)
        ret, frame = cap.read()
        if ret:
            frame = cv2.resize(frame, frame_size)
            if frame is not None:
                video_frames.append(frame)
        if len(video_frames) >= num_frames:
            break

    while len(video_frames) < num_frames:
        video_frames.append(frame)

    cap.release()

    video_frames = [f for f in video_frames if f is not None and f.shape == video_frames[0].shape]
    stacked_frames = np.stack(video_frames, axis=0)
    input_data = np.expand_dims(stacked_frames, axis=0)

    prediction = model.predict(input_data)
    return 'Foul' if prediction >= 0.5 else 'No Foul'

# Load the model
model = tf.keras.models.load_model(r'C:\Users\Yaish\Downloads\New Model\punch_classifier_model.h5')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            
            result = analyze_video(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return f"The video is a {result}."

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
