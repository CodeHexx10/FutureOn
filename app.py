from flask import Flask, render_template, request, redirect, url_for
import os
from PIL import Image
import torch
from werkzeug.utils import secure_filename
import uuid
import pickle
from pyngrok import ngrok
import requests


app = Flask(__name__)

# Configure the upload folder for images
UPLOAD_FOLDER = '/content/drive/MyDrive/Colab Notebooks/Hackathon/static/images'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Allowed extensions for file upload
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

# Ensure the upload folder exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def allowed_file(filename):
    """Check if the file extension is allowed."""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Load the BLIP model and processor
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

print(device)

with open('blip_caption.pkl', 'rb') as file:
    model = pickle.load(file)

with open('blip_caption_vis_processor.pkl', 'rb') as file:
    blip_caption_vis_processor = pickle.load(file)

@app.route('/')
def home():
    return render_template('Index.html')  # Ensure this template exists

@app.route('/Query.html', methods=['GET', 'POST'])
@app.route('/Query.html', methods=['GET', 'POST'])
def query():
    if request.method == 'POST':
        # Check if the post request has the file part
        if 'image' not in request.files:
            return render_template('Query.html', error='No file part')
        
        file = request.files['image']
        
        # If the user does not select a file, the browser also submits an empty part without a filename
        if file.filename == '':
            return render_template('Query.html', error='No selected file')
        
        if file and allowed_file(file.filename):
            # Secure the filename and make it unique
            original_filename = secure_filename(file.filename)
            unique_filename = str(uuid.uuid4()) + "_" + original_filename
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], unique_filename)
            file.save(file_path)
            print(f"File saved at: {file_path}")  # Debugging
            
            # Initialize caption variable
            caption = None
            
            # Generate caption using the model
            try:
                # Open the image using PIL
                image = Image.open(file_path).convert("RGB")
                
                # Preprocess the image and generate the caption
                image_preprocessed = blip_caption_vis_processor["eval"](image).unsqueeze(0).to(device)
                with torch.no_grad():
                    caption_str = model.generate({"image": image_preprocessed})
                
                # Assign generated caption to `caption`
                caption = caption_str[0] if isinstance(caption_str, list) else caption_str
                print(f"Generated Caption: {caption}")  # Debugging
            except Exception as e:
                print(f"Error generating caption: {e}")
                caption = "Error generating caption."
            
            return render_template('Query.html', filename=unique_filename, caption=caption)
    
    return render_template('Query.html')


if __name__ == '__main__':
  ngrok.set_auth_token("2lcNLOxb0Nqn25WCqCkheYm5AOw_kVaUj8YT1MxNGkCPS2FL")
  ngrok_tunnel = ngrok.connect(5000)
  print('Public URL:', ngrok_tunnel.public_url)
  app.run()
