from flask import Flask, request, render_template, redirect, url_for, send_from_directory
import os
from video_edit import generate_random_videos

app = Flask(__name__)

# Set the upload folder and allowed extensions
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['ALLOWED_EXTENSIONS'] = {'mp4', 'mkv', 'avi', 'mov', 'mp3', 'wav', 'flac'}
app.config['MAX_CONTENT_LENGTH'] = 100 * 1024 * 1024  # 100 MB limit for file size

# Ensure upload folder exists
if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

# Function to check allowed file extensions
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

# Store uploaded video file names
uploaded_videos = []

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        os.system('rm outputs/*')
        # Get the files from the request
        video_files = request.files.getlist('video')
        audio_file = request.files.get('audio')
        
        # Get string inputs
        audio_start = request.form.get('string1')
        audio_end = request.form.get('string2')

        video_paths = []
        # Handle video file uploads
        if video_files:
            for video in video_files:
                if video and allowed_file(video.filename):
                    filename = video.filename
                    video_file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                    video.save(video_file_path)
                    video_paths.append(video_file_path)
                    uploaded_videos.append(filename)

        audio_file_path = None
        # Handle audio file upload
        if audio_file and allowed_file(audio_file.filename):
            audio_file_path = os.path.join(app.config['UPLOAD_FOLDER'], audio_file.filename)
            audio_file.save(audio_file_path)
        
        generate_random_videos(video_paths, audio_file_path, audio_start, audio_end, 60, 10)
        os.system('rm uploads/*')
        # After processing, redirect to the video list page
        return redirect(url_for('view_videos'))
    
    return render_template('upload.html')

@app.route('/view_videos')
def view_videos():
    video_files = [(i, f) for i, f in enumerate(sorted(os.listdir('outputs'))) if f.endswith('.mp4')]
    print(video_files)
    
    return render_template('view_videos.html', video_files=video_files)

@app.route('/download/<filename>')
def download_file(filename):
    return send_from_directory('outputs', filename)

@app.route('/delete_outputs')
def delete_outputs():
    os.system('rm outputs/*')
    return redirect(url_for('view_videos'))

if __name__ == '__main__':
    app.run(host='localhost', port=5000)
