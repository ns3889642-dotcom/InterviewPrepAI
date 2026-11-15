InterviewPrepAI 🎯

AI-Powered Interview Preparation Platform

InterviewPrepAI is a Python-based interview preparation application built with Streamlit. It helps users practice technical and HR interview questions, evaluate their answers, and track their interview performance.

🚀 Features

- Multiple Subjects: Practice Python, Java, C++, SQL and HR questions.
- Difficulty Levels: Choose Beginner, Intermediate or Advanced.
- Question Generation: Get interview questions based on your selected subject and difficulty.
- Answer Evaluation: Evaluate answers using TF-IDF, text similarity and keyword matching.
- Performance Tracking: View total attempts, average score and best score.
- Performance Analytics: Explore interview score history and subject-wise performance.
- Interview History: Review previous questions, scores and dates.
- CSV Export: Download interview history.
- PDF Reports: Generate downloadable performance reports.

🛠️ Technologies Used

- Python
- Streamlit
- SQLite
- Pandas
- Scikit-learn
- Matplotlib
- ReportLab

📁 Project Structure

InterviewPrepAI/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── modules/
│   ├── database.py
│   ├── evaluator.py
│   ├── question_bank.py
│   └── report_generator.py
│
└── data/
    └── interview_history.db

⚙️ Installation and Setup

1. Clone the repository

git clone https://github.com/ns3889642-dotcom/InterviewPrepAI.git

2. Open the project folder

cd InterviewPrepAI

3. Create a virtual environment

python -m venv venv

4. Activate the environment (Windows PowerShell)

venv\Scripts\Activate

5. Install dependencies

pip install -r requirements.txt

6. Run the application

python -m streamlit run app.py

The application will open in your browser.

📊 Performance Dashboard

The dashboard provides:

- Total interview attempts
- Average performance score
- Best score
- Interview score history
- Subject-wise performance
- Previous interview attempts

🎯 Project Objective

The objective of InterviewPrepAI is to provide an accessible platform for interview practice, answer evaluation and performance tracking.

👩‍💻 Developer

Neha Sharma

- GitHub: https://github.com/ns3889642-dotcom
- LinkedIn: https://linkedin.com/in/neha-sharma-125761427

---

Built with Python and Streamlit.