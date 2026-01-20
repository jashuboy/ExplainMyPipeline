from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.json
    log = data.get("log", "")

    # TEMP: mock response (replace with Gemini later)
    response = {
        "what_happened": "The build failed due to permission issues.",
        "severity": "Medium",
        "fix": "Check file permissions in the Dockerfile.",
        "security": "Avoid running containers as root.",
        "tip": "Verify permissions before building images."
    }

    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True)
