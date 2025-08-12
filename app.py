from flask import Flask, request, jsonify
import os

app = Flask(__name__)

# Folder where uploaded videos will be stored
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def home():
    return "FitBank AI Video Scan API is running!"

@app.route('/upload_video', methods=['POST'])
def upload_video():
    if 'video' not in request.files:
        return jsonify({"error": "No video uploaded"}), 400
    
    video = request.files['video']
    if video.filename == '':
        return jsonify({"error": "No selected file"}), 400
    
    filepath = os.path.join(UPLOAD_FOLDER, video.filename)
    video.save(filepath)

    # Here you can later add AI processing logic
    return jsonify({"message": "Video uploaded successfully", "filename": video.filename})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
