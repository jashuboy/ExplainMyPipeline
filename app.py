from flask import Flask, request, jsonify, render_template
import os
import google.generativeai as genai

app = Flask(__name__)

# Configure Gemini
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-1.5-flash")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/analyze", methods=["POST"])
def analyze():
    log = request.json.get("log", "")

    prompt = f"""
You are an AI DevOps and DevSecOps mentor for beginners.

Analyze the following DevOps log and respond in this structure:

What happened:
Severity:
How to fix:
Security note:
Beginner tip:

Log:
{log}
"""

    response = model.generate_content(prompt)

    return jsonify({"result": response.text})

if __name__ == "__main__":
    app.run(debug=True)
