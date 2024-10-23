from flask import Flask, render_template, request
import os
from PIL import Image
from werkzeug.utils import secure_filename
import torch
import uuid
import pickle
from pyngrok import ngrok

from langchain_openai import ChatOpenAI

app = Flask(__name__)

# Device setup for PyTorch
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(device)

UPLOAD_FOLDER = '/content/drive/MyDrive/Colab Notebooks/Code-Hex-V-0.02/static/images'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

# Initialize OpenAI API Key
openai_api_key = ''
llm = ChatOpenAI(api_key=openai_api_key)

# Ensure the upload folder exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def allowed_file(filename):
    """Check if the file extension is allowed."""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Load your BLIP model and processor
with open('blip_caption.pkl', 'rb') as file:
    model = pickle.load(file)

with open('blip_caption_vis_processor.pkl', 'rb') as file:
    blip_caption_vis_processor = pickle.load(file)

@app.route('/')
def home():
    return render_template('Index.html')

@app.route('/Query.html', methods=['GET', 'POST'])
def query():
    user_message = ""
    filename = None
    bot_response = "Please send a message or upload an image."

    if request.method == 'POST':
        if 'message-input' in request.form:
            user_message = request.form.get("message-input", "").strip()
            if user_message:
                response = llm.invoke(user_message + " Write a brief 5-line description about the image and it should be informative.")
                bot_response = response.content
                print(bot_response)

        if 'file-input' in request.files:
            file = request.files['file-input']
            if file and allowed_file(file.filename):
                original_filename = secure_filename(file.filename)
                unique_filename = str(uuid.uuid4()) + "_" + original_filename
                file_path = os.path.join(app.config['UPLOAD_FOLDER'], unique_filename)
                file.save(file_path)

                image = Image.open(file_path).convert('RGB')

                # Preprocess image using the visual processor
                image_preprocessed = blip_caption_vis_processor["eval"](image).unsqueeze(0).to(device)

                # Generate caption using your model
                caption_str = model.generate({"image": image_preprocessed})
                print(caption_str)
                print(file_path)

                filename = file_path
                bot_response = caption_str

    return render_template('Query.html', filename=filename, user_message=user_message, bot_response=bot_response)

if __name__ == '__main__':
    # Ngrok setup to expose the Colab server
    ngrok.set_auth_token("")
    ngrok_tunnel = ngrok.connect(5000)
    print('Public URL:', ngrok_tunnel.public_url)
    app.run()
