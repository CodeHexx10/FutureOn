# FutureOn - Conversational and Image Recognition Chatbot

### Project Topic:
Conversational and Image Recognition Chatbot

### Hackathon:
Developed during **HackHeritage 2024**, a 24-hour hackathon held at **Heritage Institute of Technology** from **6th Sept 2024 to 7th Sept 2024**.

### Contributors

| ![Debanshu](https://avatars.githubusercontent.com/Debanshu2002?s=150) | ![Dibyo](https://avatars.githubusercontent.com/TheRecursiveGuy?s=150) | ![Saqib](https://avatars.githubusercontent.com/jvedsaqib?s=150) |
|:---------------------------------------------------------------------:|:--------------------------------------------------------------------:|:--------------------------------------------------------------:|
| [Debanshu Das](https://github.com/Debanshu2002)                       | [Dibyo Banerjee](https://github.com/TheRecursiveGuy)                 | [Saqib Javed](https://github.com/jvedsaqib)                    |

| ![Sayan](https://avatars.githubusercontent.com/Leoreee?s=150) | ![Soubhagya](https://avatars.githubusercontent.com/SOubhagyaPaul?s=150) | ![Suvra](https://avatars.githubusercontent.com/Ether-suvra?s=150) |
|:-------------------------------------------------------------:|:---------------------------------------------------------------------:|:---------------------------------------------------------------:|
| [Sayan Ranjan Khatua](https://github.com/Leoreee)             | [Soubhagya Paul](https://github.com/SOubhagyaPaul)                    | [Suvra Bhattacharjee](https://github.com/Ether-suvra)            |



---

## Project Description
**FutureOn** is a conversational and image recognition chatbot that integrates advanced AI models to handle both text-based conversations and image recognition tasks. Using the power of OpenAI's ChatGPT for natural language understanding and **BLIP (Bootstrapping Language-Image Pretraining)** for image captioning, the chatbot can interact intelligently with users and describe uploaded images.

---

## Setup Instructions

### 1. Clone the repository:
```bash
git clone https://github.com/CodeHexx10/FutureOn.git
cd FutureOn
```

### 2. Install required dependencies:
Ensure you have Python installed. Then run:
```bash
pip install -r requirements.txt
```

### 3. Running the application:
Once all dependencies are installed, launch the Flask app:
```bash
python app.py
```

---

## Models and Techniques

### BLIP2 (Bootstrapping Language-Image Pretraining 2):
BLIP2 leverages transfer learning to bootstrap vision-language pretraining, bridging the gap between image understanding and textual descriptions. This model enhances the chatbot's ability to recognize and generate meaningful captions for uploaded images.

### Salesforce-LAVIS:
The **LAVIS** (Language-Aware Vision & Image System) model suite from Salesforce powers the image recognition capabilities of the chatbot, facilitating advanced image captioning and understanding through pretrained models.

### Transfer Learning:
We employed **transfer learning** by fine-tuning pre-trained models like BLIP2, enabling faster convergence and higher accuracy when dealing with image-to-text tasks.

---

## Model Links
- [BLIP-LAVIS Model](https://www.kaggle.com/models/jvedsaqib/blip-lavis)

---

## License
This project is licensed under the MIT License.
