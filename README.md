# 🧠 AI Resume Analyzer & Smart Interview Bot  

A **Final Year Capstone Project** built using **Streamlit, NLP, and Machine Learning**.  
This tool helps job seekers analyze their resumes, get skill & course recommendations, calculate resume scores, and practice interviews with an **AI-powered Interview Bot**.  

---

## 🚀 Features  

### 📑 Resume Analyzer
- Upload a **PDF Resume**  
- Extracts details (Skills, Education, Experience, Degree, etc.)  
- Predicts career domain:
  - Data Science  
  - Web Development  
  - Android Development  
  - iOS Development  
  - UI/UX Design  
- Suggests **recommended skills & courses**  
- Provides a **resume score** with improvement tips  

### 🎥 Learning Resources
- Personalized course recommendations  
- Resume writing tips video  
- Interview preparation video  

### 🗣️ AI Interview Bot
- Domain-specific interview questions  
- Evaluates answers using:
  - **Semantic similarity** (Sentence Embeddings)  
  - **Keyword coverage** (Important concepts)  
  - **Answer length check (penalty for too short answers)**  
- Gives:
  - Final Interview Score (0–100)  
  - Detailed Feedback (missing terms, suggestions)  
- Stores results in **MySQL Database** for analytics  

### 🛠️ Admin Dashboard
- Secure Admin Login  
- View all **user resume analysis results**  
- View & download feedback data  
- Pie-chart analytics:
  - Domains distribution  
  - Resume scores  
  - User experience levels  
  - User locations (City/State/Country)  

### 💬 Feedback System
- Collects **user ratings (1–5) and comments**  
- Displays **past feedback analytics** with charts  

---

## 🖥️ Tech Stack  

- **Frontend & App**: [Streamlit](https://streamlit.io/)  
- **Backend**: Python  
- **Database**: MySQL (via `pymysql`)  
- **ML/NLP**:  
  - NLTK  
  - Sentence Transformers  
  - Pyresparser  
- **Visualization**: Plotly, Streamlit-Tags  
- **Other Libraries**: HuggingFace, Geopy, PDFMiner, PIL  

---

## ⚙️ Installation & Setup  

### 1️⃣ Clone the repository  
```bash
git clone https://github.com/0ashutosh/Smart-Competency-Diagnostic-and-Candidate-Profile-Score-Calculator.git
cd Smart-Competency-Diagnostic-and-Candidate-Profile-Score-Calculator



2️⃣ Create Virtual Environment
```bash
python -m venv venv
venv\Scripts\activate   # On Windows
source venv/bin/activate  # On Linux/Mac


3️⃣ Install dependencies
```bash
pip install -r requirements.txt



4️⃣ Setup Database
Install MySQL Server
Create a database named cv
Update your MySQL username/password inside App.py:
```bash
connection = pymysql.connect(host='localhost', user='root', password='yourpassword', db='cv')



5️⃣ Run the App
```bash
streamlit run App/App.py



📊 Example Outputs
Resume Analyzer

✅ Extracted details and recommendations
✅ Resume score progress bar

AI Interview Bot

✅ Domain-wise questions
✅ Instant scoring + feedback

Admin Dashboard

✅ View all user analytics
✅ Pie-chart reports (domain, skills, location, scores)


📂 Project Structure:
📦 Smart-Competency-Diagnostic-and-Candidate-Profile-Score-Calculator
 ┣ 📂 App
 ┃ ┣ 📜 App.py          # Main Streamlit app
 ┃ ┣ 📜 Courses.py      # Predefined course recommendations
 ┃ ┣ 📂 Logo            # Logo images
 ┃ ┣ 📂 Uploaded_Resumes
 ┣ 📜 requirements.txt  # Python dependencies
 ┣ 📜 README.md         # Project documentation
 ┣ 📜 .gitignore        # Ignore venv, cache, etc.



🧑‍💻 Contributors:
Ashutosh Agrawal
Ashutosh Kumar Sharma
Anamaneni Abhilash

📜 License
