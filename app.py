import os, time, datetime, json
import streamlit as st
import pandas as pd
import plotly.express as px
from PIL import Image
from src.db import get_conn, insert_user_data, insert_feedback
from src.resume_parser import parse_resume
from src.recommender import SKILLBANK, classify_field, recommend_skills, recommend_courses
from src.interview_bot import run as run_interview
from src.utils import download_link_df, get_env_info, score_resume

# Auto-download NLTK bits on first run (quiet)
import nltk
for pkg, path in [("punkt","tokenizers/punkt"), ("stopwords","corpora/stopwords"), ("wordnet","corpora/wordnet")]:
    try:
        nltk.data.find(path)
    except LookupError:
        nltk.download(pkg, quiet=True)

st.set_page_config(page_title="AI Resume Analyzer (Modern)", page_icon="🧠", layout="wide")

# Optional logo
logo_path = os.path.join("assets", "logo.png")
if os.path.exists(logo_path):
    st.image(Image.open(logo_path), width=180)

st.title("AI Resume Analyzer")

PAGES = ["User", "Interview Bot", "Feedback", "Admin", "About"]
choice = st.sidebar.selectbox("Navigate", PAGES)

conn = None
try:
    conn = get_conn()
except Exception as e:
    st.sidebar.error(f"DB connection failed: {e}")

if choice == "User":
    st.subheader("Upload your resume (PDF)")
    up = st.file_uploader("Choose PDF", type=["pdf"])
    name = st.text_input("Your Name *")
    email = st.text_input("Your Email *")

    if up and name and email:
        # Save uploaded file
        save_dir = "uploads"
        os.makedirs(save_dir, exist_ok=True)
        save_path = os.path.join(save_dir, up.name)
        with open(save_path, "wb") as f:
            f.write(up.read())

        with st.spinner("Analyzing resume..."):
            res = parse_resume(save_path, SKILLBANK)
            user_level = "Fresher"
            t = res["raw_text"].lower()
            if "internship" in t:
                user_level = "Intermediate"
            if "experience" in t or "work experience" in t:
                user_level = "Experienced"

            field = classify_field(res["skills"])
            rec_sk = recommend_skills(field)
            rec_courses = recommend_courses(field)
            score = score_resume(res["raw_text"])

            st.success(f"Hello {res['name'] or name} 👋")
            col1, col2 = st.columns(2)
            with col1:
                st.write("**Extracted info**")
                st.write(f"Email: {res['email'] or email}")
                st.write(f"Phone: {res['phone'] or '—'}")
                st.write(f"Degree: {res['degree'] or '—'}")
                st.write(f"Pages: {res['pages']}")
            with col2:
                st.write("**Skills detected**")
                st.write(", ".join(res['skills']) or "—")

            st.info(f"Predicted Field: **{field}**  |  Level: **{user_level}**")
            st.progress(score/100)
            st.write(f"**Resume Score:** {score}/100")

            st.subheader("Recommended Skills")
            st.write(", ".join(rec_sk) if rec_sk else "—")

            st.subheader("Recommended Courses")
            if rec_courses:
                for i,(title, link) in enumerate(rec_courses, start=1):
                    st.markdown(f"{i}. [{title}]({link})")
            else:
                st.caption("No course recommendations for this field yet.")

            # Insert into DB
            if conn:
                token, ip, host, osver = get_env_info()
                row = dict(
                token=token,
                ip=ip,
                host=host,
                os=osver,
                name=name or res['name'] or "",
                email=email or res['email'] or "",
                phone=res['phone'] or "",
                degree=res['degree'] or "",
                page_count=res['pages'],
                predicted_field=field,
                user_level=user_level,
                skills=json.dumps(res['skills']),
                recommended_skills=json.dumps(rec_sk),
                recommended_courses=json.dumps(rec_courses),
                resume_score=score,
                pdf_filename=up.name
            )


                try:
                    insert_user_data(conn, row)
                except Exception as e:
                    st.error(f"Could not save to DB: {e}")

elif choice == "Interview Bot":
    if conn:
        run_interview(conn, "data/questions.csv")
    else:
        st.error("DB not connected. Check your .env and MySQL.")

elif choice == "Feedback":
    st.subheader("Feedback")
    with st.form("fb"):
        fname = st.text_input("Name")
        fmail = st.text_input("Email")
        fscore = st.slider("Rate us", 1, 5, 5)
        fcomment = st.text_area("Comments (optional)")
        sub = st.form_submit_button("Submit")
        if sub:
            if conn:
                try:
                    insert_feedback(conn, fname, fmail, fscore, fcomment)
                    st.success("Thanks! Feedback recorded.")
                except Exception as e:
                    st.error(f"Could not save feedback: {e}")
            else:
                st.error("DB not connected.")

elif choice == "Admin":
    st.subheader("Admin Dashboard")
    user = st.text_input("Username")
    pwd = st.text_input("Password", type="password")
    if st.button("Login"):
        if user == "admin" and pwd == "ADMIN":
            if not conn:
                st.error("DB not connected.")
            else:
                try:
                    with conn.cursor() as cur:
                        cur.execute("SELECT id, ip, resume_score, predicted_field, user_level, name, email, created_at FROM user_data ORDER BY created_at DESC")
                        rows1 = cur.fetchall()
                        df1 = pd.DataFrame(rows1, columns=[desc[0] for desc in cur.description])

                        cur.execute("SELECT id, name, email, score, comments, created_at FROM user_feedback ORDER BY created_at DESC")
                        rows2 = cur.fetchall()
                        df2 = pd.DataFrame(rows2, columns=[desc[0] for desc in cur.description])
                except Exception as e:
                    st.error(e)
                    st.stop()

                st.write("### Users")
                st.dataframe(df1, use_container_width=True)
                download_link_df(df1, "users.csv")

                st.write("### Feedback")
                st.dataframe(df2, use_container_width=True)
                download_link_df(df2, "feedback.csv")

                if not df1.empty:
                    st.write("### Analytics")
                    colA, colB, colC = st.columns(3)
                    with colA:
                        fig = px.pie(df1, names="predicted_field", title="Predicted Field")
                        st.plotly_chart(fig, use_container_width=True)
                    with colB:
                        fig = px.pie(df1, names="user_level", title="User Level")
                        st.plotly_chart(fig, use_container_width=True)
                    with colC:
                        fig = px.histogram(df1, x="resume_score", nbins=10, title="Resume Score")
                        st.plotly_chart(fig, use_container_width=True)
        else:
            st.error("Wrong credentials.")

else:
    st.markdown("""
### About
This is a modern rewrite of your AI Resume Analyzer:
- Pure-Python PDF parsing (no binary pain).
- Lightweight NLP (NLTK).
- Fast semantic scoring via Sentence Transformers (CPU).
- MySQL for persistence.
- Streamlit UI with Admin/Feedback dashboards.

Built to be Windows-friendly and version-stable.
                


Built by:                                           
Ashutosh Agrawal,  
Ashutosh Kumar Sharma,  
Anamaneni Abhilash
""")
