from flask import Flask, request, jsonify, render_template, redirect, url_for
import requests

app = Flask(__name__)

# 🔐 Replace with your Hugging Face API Key
HUGGING_FACE_API_KEY = "your_actual_hugging_face_api_key"
HF_MODEL = "stabilityai/stable-diffusion-2"  # Example model, change as needed

@app.route('/')
def home():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>AI Logo Generator</title>
        <script src="https://cdn.jsdelivr.net/particles.js/2.0.0/particles.min.js"></script>
        <style>
            body {
                font-family: Arial, sans-serif;
                text-align: center;
                background: linear-gradient(135deg, #1e3c72, #2a5298);
                color: white;
                margin: 0;
                padding: 0;
                overflow: hidden;
            }
            #particles-js {
                position: absolute;
                width: 100%;
                height: 100%;
                z-index: -1;
            }
            .container {
                background: rgba(255, 255, 255, 0.15);
                backdrop-filter: blur(10px);
                border-radius: 15px;
                padding: 50px;
                width: 90%;
                max-width: 600px;
                box-shadow: 0 5px 20px rgba(255, 255, 255, 0.3);
                text-align: center;
                margin: 8% auto;
            }
            h1 {
                margin-bottom: 20px;
                letter-spacing: 2px;
                word-spacing: 5px;
            }
            input, select, button {
                padding: 14px;
                width: 100%;
                border: none;
                border-radius: 8px;
                font-size: 18px;
                text-align: center;
                background: rgba(255, 255, 255, 0.2);
                color: white;
                outline: none;
                margin-bottom: 15px;
                letter-spacing: 1px;
                word-spacing: 3px;
            }
            button {
                background: linear-gradient(90deg, #ff6f61, #ffcc00);
                font-size: 18px;
                cursor: pointer;
                margin-top: 15px;
            }
        </style>
    </head>
    <body>
        <div id="particles-js"></div>
        <div class="container">
            <h1>🚀 AI Logo Generator</h1>
            <form action="/generate-logo" method="POST">
                <div class="input-group">
                    <input type="text" name="brand" placeholder="💡 Enter Brand Name" required>
                </div>
                <div class="input-group">
                    <input type="text" name="style" placeholder="🎨 Preferred Style (Minimal, Bold, Modern)" required>
                </div>
                <div class="input-group">
                    <select name="category" required>
                        <option value="" disabled selected>🗂️ Select Business Type</option>
                        <option value="Business">Business</option>
                        <option value="Ecommerce">Ecommerce</option>
                        <option value="Technology">Technology</option>
                        <option value="Startups">Startups</option>
                    </select>
                </div>
                <div class="input-group">
                    <select name="size" required>
                        <option value="512x512" selected>🔸 Medium (512x512)</option>
                        <option value="256x256">🔹 Small (256x256)</option>
                        <option value="1024x1024">🔺 Large (1024x1024)</option>
                    </select>
                </div>
                <button type="submit">✨ Generate Logo</button>
            </form>
        </div>
        <script>
            particlesJS("particles-js", {
                "particles": {
                    "number": { "value": 100 },
                    "size": { "value": 3 },
                    "move": { "speed": 2 },
                    "color": { "value": "#ffffff" }
                }
            });
        </script>
    </body>
    </html>
    """

if __name__ == '__main__':
    print("🚀 AI Logo Generator Running at: http://127.0.0.1:5000/")
    app.run(debug=True, host='0.0.0.0', port=5000)