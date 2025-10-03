# Smart Competency Diagnostic and Candidate Profile Score Calculator

A capstone project (AI Resume Analyzer + Interview Bot + Candidate Profiling).  
This system extracts skills from resumes, evaluates candidate answers, and provides AI-powered interview scoring.

---

## 🚀 Features
- Resume parsing (using `pyresparser` + `spaCy`)
- Candidate profile scoring
- AI Interview Bot (semantic + keyword coverage)
- Data visualization via `Streamlit`
- Adaptive skill-gap detection

---

## 🛠️ Installation & Setup

### 1. Clone Repo
```bash
git clone https://github.com/0ashutosh/Smart-Competency-Diagnostic-and-Candidate-Profile-Score-Calculator.git
cd Smart-Competency-Diagnostic-and-Candidate-Profile-Score-Calculator/App
```

### 2. Create Virtual Environment
```bash
python -m venv venv
venv\Scripts\activate   # Windows
# OR
source venv/bin/activate   # Linux/Mac
```

### 3. Install Dependencies
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

If you don’t have `requirements.txt`, generate it once:
```bash
pip freeze > requirements.txt
```

### 4. Download Required Models
These will be auto-installed when you run the app:
- NLTK: `punkt`, `punkt_tab`, `stopwords`, `wordnet`
- spaCy: `en_core_web_sm`
- SentenceTransformer: `all-MiniLM-L6-v2`

(Handled automatically in code, but you can install manually if needed.)

Manual installs:
```bash
python -m nltk.downloader punkt punkt_tab stopwords wordnet
python -m spacy download en_core_web_sm
```

---

## ▶️ Run the App
```bash
cd App
streamlit run App.py
```

---

## ❌ Common Errors & Fixes

### 1. `ModuleNotFoundError`
If a module is missing:
```bash
pip install <module-name>
```

### 2. `numpy.core.multiarray failed to import`
Downgrade NumPy:
```bash
pip install "numpy<2.0"
```

### 3. `ImportError: cached_download`
Install compatible huggingface version:
```bash
pip install "huggingface-hub<0.13"
```

### 4. NLTK resource not found
```bash
python -m nltk.downloader punkt punkt_tab stopwords wordnet
```

### 5. spaCy model missing
```bash
python -m spacy download en_core_web_sm
```

---

## 📂 Project Structure
```
Smart-Competency-Diagnostic-and-Candidate-Profile-Score-Calculator/
│
├── App/                # Main application
│   ├── App.py          # Streamlit app
│   ├── questions.csv   # Sample interview Q&A
│   └── ...
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 👨‍💻 Contributors
- **Ashutosh Agrawal**
- **Ashutosh Kumar Sharma**
- **Anamaneni Abhilash**

---

## 📜 License
