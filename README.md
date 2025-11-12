## 🧠 Smart Competency Diagnostic & AI Resume Analyzer

An intelligent Streamlit web app that **analyzes resumes, recommends skills/courses, and conducts mock interviews** powered by NLP and semantic scoring.
It integrates **MySQL** for data persistence and provides an **Admin Dashboard** for insights and analytics.

---

### 👨‍💻 Authors

* **Ashutosh Agrawal**
* **Ashutosh Kumar Sharma**
* **Anamaneni Abhilash**

---

## 🚀 Features

* 📄 **Resume Parsing** – Extracts candidate name, email, phone, degree, and skills from PDF resumes
* 🧩 **Skill & Domain Prediction** – Identifies user’s domain (e.g., Data Science, Web Dev, Android, etc.)
* 🎯 **Recommendations** – Suggests relevant upskilling courses and next-step skills
* 🤖 **AI Interview Bot** – Conducts domain-specific mock interviews with semantic evaluation
* 📊 **Admin Dashboard** – Displays analytics and user feedback using Plotly visualizations
* 💬 **Feedback Module** – Collects user feedback and ratings
* 🗄️ **MySQL Integration** – Stores user profiles, logs, and feedback persistently

---

## 🏗️ Tech Stack

| Layer                  | Technology                  |
| ---------------------- | --------------------------- |
| Frontend/UI            | Streamlit                   |
| Backend                | Python                      |
| NLP                    | Sentence Transformers, NLTK |
| Database               | MySQL                       |
| Visualization          | Plotly                      |
| Environment Management | python-dotenv               |
| Resume Parsing         | PyPDF                       |

---

## 🗂️ Project Structure

```
📦 smart_competency_diagnostic/
├── app.py
├── src/
│   ├── db.py
│   ├── utils.py
│   ├── recommender.py
│   ├── resume_parser.py
│   ├── interview_bot.py
│
├── data/
│   └── questions.csv
│
├── assets/
│   └── logo.png
│
├── uploads/                 # resumes uploaded by users
├── schema.sql               # MySQL database schema
├── requirements.txt
├── .env
└── README.md
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository

```bash
git clone https://github.com/<your-username>/<your-repo-name>.git
cd <your-repo-name>
```

### 2️⃣ Create a virtual environment

```bash
python -m venv venv
venv\Scripts\activate    # Windows
# OR
source venv/bin/activate # macOS/Linux
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

> 💡 **Note:**
> For CPU-only systems, install PyTorch manually using:
>
> ```bash
> pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu
> ```

### 4️⃣ Setup the MySQL Database

1. Open MySQL and run:

   ```sql
   SOURCE schema.sql;
   ```
2. Update your `.env` file (example):

   ```bash
   DB_HOST=localhost
   DB_PORT=3306
   DB_NAME=smart_competency_diagnostic
   DB_USER=root
   DB_PASSWORD=root
   ```

### 5️⃣ Run the app

```bash
streamlit run app.py
```

Then open [http://localhost:8501](http://localhost:8501) in your browser.

---

## 🧩 Key Modules

| File                 | Description                                                             |
| -------------------- | ----------------------------------------------------------------------- |
| **app.py**           | Main Streamlit app handling navigation, resume upload, and admin panel  |
| **db.py**            | Database connection and insert functions                                |
| **resume_parser.py** | Extracts information from resumes using PyPDF                           |
| **recommender.py**   | Domain classification and skill/course recommendations                  |
| **interview_bot.py** | Interactive AI interview bot with semantic scoring                      |
| **utils.py**         | Helper functions for resume scoring, CSV download, and environment info |

---

## 🧠 Database Schema Overview

### Tables

1. **user_data** – Stores parsed resume info, predicted field, and recommendations
2. **interview_logs** – Logs user interview Q&A and semantic scores
3. **user_feedback** – Collects user satisfaction and comments

SQL schema file: [`schema.sql`](./schema.sql)

---

## 📊 Admin Dashboard

* View all users and feedback
* Download data as CSV
* Visualize:

  * Predicted Fields (Pie Chart)
  * User Levels (Pie Chart)
  * Resume Score Distribution (Histogram)

---

## 💡 Future Enhancements

* Resume ranking & job matching
* Integration with LinkedIn API
* AI-based personality analysis
* Enhanced admin analytics

---

## 📬 Feedback

We welcome feedback and suggestions!
Submit them through the in-app **Feedback** section or open an issue on GitHub.

---

## 🏁 License

This project is licensed under the **MIT License**.
Feel free to use and modify it with attribution.

---

Would you like me to include **badges (e.g., Python version, Streamlit version, License)** and a **demo screenshot placeholder** section at the top?
It’ll make the README look even more professional for GitHub.
