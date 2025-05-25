# 📄 ResumeRadar – AI-Powered Resume ATS Score Calculator

ResumeRadar is an advanced AI-based application that analyzes resumes and evaluates them based on key ATS (Applicant Tracking System) criteria. Using NLP models like BERT, grammar and format checkers, and keyword matchers, ResumeRadar provides users with actionable insights to improve their resumes and boost job application success rates.

---

## 🚀 Features

✅ **AI Resume Parsing with BERT**  
✅ **Grammar and Spelling Check**  
✅ **Keyboard Usage Analysis (e.g., filler words)**  
✅ **Formatting Checker (section completeness, font consistency)**  
✅ **Job Description Matching**  
✅ **Visual ATS Score Breakdown**  
✅ **Streamlit-based Interactive UI**

---

## 🧠 How It Works

ResumeRadar analyzes a resume in PDF format, processes it through AI models and rule-based systems, and returns:

- Matched keywords from the job description
- Detected grammar and spelling issues
- Filler word usage and readability problems
- Formatting issues like missing sections or inconsistent layout
- Final ATS score and a visual breakdown of scoring components

---

## 🛠️ Tech Stack

| Layer      | Technology |
|------------|-------------|
| UI         | Streamlit   |
| NLP Engine | BERT (via HuggingFace Transformers) |
| Parsing    | PyMuPDF, PyPDF2 |
| Grammar    | LanguageTool API |
| Charting   | Pandas + Streamlit Charts |
| Entity Recognition | spaCy (customizable) |

---

## 📦 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Manojgowda2000/ATS-Pro-AI-Powered-Resume-Evaluator.git
cd ATS-Pro-AI-Powered-Resume-Evaluator
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
python -m spacy download en_core_web_sm
```

### 3. Run the App

```bash
streamlit run app.py
```

---

## 🤝 Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss what you’d like to change or improve.
