
````markdown
# 🧠 AI Resume Analyzer & Smart Interview Bot  

This is a **capstone project** built using **Streamlit, NLP, and Machine Learning**.  
It helps job seekers analyze their resumes, get skill/course recommendations, calculate resume scores, and practice interviews with an **AI Interview Bot**.  

---

## 🚀 Features
- 📑 **Resume Analyzer**  
  - Upload a PDF resume  
  - Extracts details (skills, education, experience)  
  - Predicts domain (Data Science, Web Dev, Android, iOS, UI/UX)  
  - Suggests recommended skills & courses  
  - Provides resume score and improvement tips  

- 🎥 **Learning Resources**  
  - Personalized courses  
  - Resume writing tips video  
  - Interview preparation video  

- 🗣️ **AI Interview Bot**  
  - Domain-specific interview questions  
  - Evaluates answers using:
    - **Semantic similarity** (sentence embeddings)  
    - **Keyword coverage** (important terms)  
    - **Answer length penalty check**  
  - Gives a **final interview score + feedback**  
  - Stores results in MySQL for analytics  

- 🛠️ **Admin Dashboard**  
  - View all users & their resume analysis  
  - View feedback data  
  - Pie-chart analytics (domains, scores, experience level, locations, etc.)  

- 💬 **Feedback System**  
  - Collects user ratings and comments  
  - Displays past feedback with analytics  

---

## 🖥️ Tech Stack
- **Frontend & App**: Streamlit  
- **Backend**: Python  
- **Database**: MySQL (pymysql connector)  
- **ML/NLP**: NLTK, Sentence Transformers, Pyresparser  
- **Visualization**: Plotly, Streamlit-Tags  
- **Other**: HuggingFace, Geopy, PDFMiner  

---

## ⚙️ Installation & Setup  

1. **Clone this repo**  
   ```bash
   git clone https://github.com/<your-username>/<repo-name>.git
   cd <repo-name>
````

2. **Create & activate virtual environment**

   ```bash
   python -m venv venv
   source venv/bin/activate   # On Linux/Mac
   venv\Scripts\activate      # On Windows
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Setup MySQL Database**

   * Create database `cv`
   * Tables will be auto-created when you run the app

5. **Run the app**

   ```bash
   streamlit run App.py
   ```

---

## 📊 Database Schema

* **user_data** → stores user resume details & recommendations
* **user_feedback** → stores feedback and ratings
* **interview_logs** → stores interview answers & scores

---

## 📂 Project Structure

```
AI-Resume-Analyzer/
│── App.py                # Main Streamlit app
│── Courses.py            # Predefined courses & video data
│── requirements.txt      # Python dependencies
│── README.md             # Project documentation
│── Logo/                 # Logo & icons
│── Uploaded_Resumes/     # User resumes (ignored in Git)
│── .gitignore            # Ignore venv, cache, logs, etc.
```

---

## 👨‍💻 Contributors

* [Ashutosh Agrawal](https://www.linkedin.com/in/ashutosh-agrawal-b3a331244/)
* [Ashutosh Kumar Sharma](https://www.linkedin.com/in/ashutosh-sharma-062247257/)
* [Anamaneni Abhilash](https://www.linkedin.com/in/anamaneni-abhilash-969a37379/)

---

## 📜 License

This project is for **academic and learning purposes**.

---

```
