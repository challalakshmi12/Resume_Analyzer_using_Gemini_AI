🤖 AI Resume Analyzer using Gemini AI
An AI-powered Resume Analyzer that evaluates resumes for a target job role using Google's Gemini AI. The application provides an ATS-style evaluation, highlights strengths and weaknesses, suggests improvements, recommends projects, and generates interview questions.

📌 Features
📄 Analyze resumes for any job role
🎯 ATS-style resume evaluation
💪 Identify resume strengths
⚠️ Detect weak areas and suggest improvements
🚀 Recommend relevant projects
🎤 Generate interview questions
🌙 Modern responsive UI with Dark/Light Mode
⚡ Powered by Google Gemini AI
🛠 Tech Stack
Frontend
HTML5
CSS3
JavaScript
Backend
Python
Flask
Flask-CORS
AI
Google Gemini API
📂 Project Structure
AI-Resume-Analyzer/
│
├── index.html
├── resume_api.py
├── requirements.txt
├── README.md
└── screenshots/
⚙️ Installation
1. Clone the repository
git clone https://github.com/YOUR_USERNAME/AI-Resume-Analyzer.git
2. Open the project
cd AI-Resume-Analyzer
3. Install dependencies
pip install -r requirements.txt
4. Get a Gemini API Key
Create a free API key from:

https://aistudio.google.com/app/apikey

5. Add your API Key
Open resume_api.py

Replace

genai.configure(api_key="")
with

genai.configure(api_key="YOUR_GEMINI_API_KEY")
6. Start the Flask Server
python resume_api.py
The backend will start at

http://localhost:8000
7. Open the Application
Open index.html in your browser or use the VS Code Live Server extension.

📷 Screenshots
Create a folder named screenshots and add images such as:

screenshots/
    home.png
    analysis.png
Then include them here:

Home Page
Home

Analysis Result
Analysis

📋 Sample Output
The analyzer provides:

ATS Score
Resume Evaluation
Matching Skills
Missing Skills
Resume Strengths
Weak Areas
Suggested Projects
Interview Questions
💡 Future Improvements
Upload PDF and DOCX resumes
Keyword matching against job descriptions
Download analysis as PDF
Resume comparison
User authentication
Resume history
AI-powered resume tailoring
🤝 Contributing
Contributions are welcome.

Fork the repository.
Create a feature branch.
Commit your changes.
Open a Pull Request.
📜 License
This project is licensed under the MIT License.

👤 Author
GitHub: https://github.com/challalakshmi12

If you found this project helpful, consider giving it a ⭐.
