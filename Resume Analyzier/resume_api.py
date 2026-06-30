from flask import Flask, request, jsonify
from flask_cors import CORS
import google.generativeai as genai

# Configure API key
genai.configure(api_key="paste your API key here")  # <= replace

model = genai.GenerativeModel("models/gemini-2.5-flash")
#prompt 

def resume_analyzer_prompt(text, role):
    return f"""
You are an expert ATS Resume Analyzer.

Analyze this resume for the role: {role}

Resume:
{text}

Provide a concise response using the following format:

📊 ATS Score: XX/100

✅ Matching Skills:
- Skill 1
- Skill 2
- Skill 3

❌ Missing Skills:
- Skill 1
- Skill 2
- Skill 3

💪 Strengths:
- Maximum 3 points

⚠️ Improvements:
- Maximum 3 points

🚀 Suggested Projects:
- Maximum 2 projects

🎤 Top Interview Questions:
- Maximum 5 questions

Rules:
- Keep the entire response under 300 words.
- Use bullet points only.
- Do NOT rewrite the entire resume.
- Be clear and concise.
"""

app = Flask(__name__)
CORS(app)                                  # Enable CORS for frontend

@app.route("/analyze", methods=["POST"])
def analyze_resume():
    data = request.json
    resume = data.get("resume")
    role = data.get("role")

    response = model.generate_content(resume_analyzer_prompt(resume, role))
    return jsonify({"result": response.text})

if __name__ == "__main__":
    app.run(port=8000, debug=True)
