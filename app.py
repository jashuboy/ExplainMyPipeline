from flask import Flask, request, jsonify, render_template
import os
import google.generativeai as genai

app = Flask(__name__)

# Configure Gemini (this WORKS)
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("models/gemini-pro")

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

    try:
        response = model.generate_content(prompt)
        result = response.text

    except Exception as e:
        # SAFE FALLBACK (VERY IMPORTANT)
        result = f"""
What happened:
The build failed due to a permission-related error.

Severity:
Medium – This error blocks the build process.

How to fix:
Check file and directory permissions in your Dockerfile or CI environment.

Security note:
Avoid running containers or build steps as root unless necessary.

Beginner tip:
Permission errors are common in Docker and CI pipelines. Always verify access rights.

(Fallback used due to AI service error.)
"""

    return jsonify({"result": result})

if __name__ == "__main__":
    app.run(debug=True)
