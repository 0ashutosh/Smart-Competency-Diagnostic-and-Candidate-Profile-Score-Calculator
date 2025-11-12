import re, string, secrets, time, datetime
from collections import Counter
from typing import Tuple, List
import pandas as pd
import streamlit as st
from sentence_transformers import SentenceTransformer, util

from .db import insert_interview_log

@st.cache_resource(show_spinner=False)
def load_model():
    # tiny, fast, accurate for semantic similarity
    return SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

MODEL = load_model()

@st.cache_data(show_spinner=False)
def load_questions(path: str) -> pd.DataFrame:
    import os
    print("DEBUG – trying to load:", path)
    print("DEBUG – absolute path:", os.path.abspath(path))
    try:
        df = pd.read_csv("D:\capstone\capstone\data\questions.csv", encoding="utf-8")
        print("DEBUG – columns:", df.columns.tolist())
        print("DEBUG – rows loaded:", len(df))
        df.columns = [c.strip().lower() for c in df.columns]
    except Exception as e:
        print("ERROR loading CSV:", e)
        return pd.DataFrame(columns=["domain", "question", "answer"])

    need = {"domain", "question", "answer"}
    return df if need.issubset(set(df.columns)) else pd.DataFrame(columns=list(need))


STOP = set("""
a an the and or but if then in of on at from by for to with without into within over under again further once
""".split())

def preprocess(text: str) -> List[str]:
    text = text.lower().translate(str.maketrans("", "", string.punctuation))
    return [t for t in text.split() if t.isalpha() and t not in STOP]

def top_keywords(text: str, k:int=8) -> List[str]:
    toks = preprocess(text)
    c = Counter(toks)
    return [w for w,_ in c.most_common(k)]

def evaluate(user_ans: str, ref_ans: str) -> Tuple[float, float, float, List[str]]:
    if not user_ans.strip():
        return 0.0, 0.0, 0.0, []

    emb1 = MODEL.encode(user_ans, convert_to_tensor=True)
    emb2 = MODEL.encode(ref_ans, convert_to_tensor=True)
    sem = float(util.cos_sim(emb1, emb2).item())  # 0..1
    sem_score = max(0.0, min(1.0, sem)) * 100.0

    kws = top_keywords(ref_ans, 8)
    user_tokens = set(preprocess(user_ans))
    covered = sum(1 for k in kws if k in user_tokens)
    cov = (covered / max(1, len(kws))) * 100.0
    missing = [k for k in kws if k not in user_tokens]

    # blend
    final = 0.75*sem_score + 0.25*cov
    return round(final,2), round(sem_score,2), round(cov,2), missing

def run(conn, questions_csv: str = "data/questions.csv"):
    st.header("🗣️ AI Interview Bot")
    df = load_questions(questions_csv)
    if df.empty:
        st.warning("No questions found. Add rows to data/questions.csv")
        return

    domains = sorted(df["domain"].dropna().unique().tolist())
    domain = st.selectbox("Choose a domain", domains)

    if "ibot" not in st.session_state:
        st.session_state.ibot = {"token": secrets.token_urlsafe(8)}
    token = st.session_state.ibot["token"]

    domdf = df[df["domain"] == domain].reset_index(drop=True)
    if "qidx" not in st.session_state:
        st.session_state.qidx = 0
        st.session_state.results = []

    idx = st.session_state.qidx
    total = len(domdf)
    st.progress(0 if total == 0 else idx/total)

    if idx < total:
        row = domdf.iloc[idx]
        st.subheader(f"Q{idx+1}: {row['question']}")
        ans = st.text_area("Your answer:", key=f"ans_{idx}", height=140)
        c1, c2 = st.columns(2)
        if c1.button("Submit"):
            final, sem, cov, missing = evaluate(ans, row["answer"])
            st.info(f"Final Score: **{final:.2f}%**  |  Semantic: **{sem:.1f}%**  |  Coverage: **{cov:.1f}%**")
            if missing:
                st.caption(f"Missing important terms: {', '.join(missing[:6])}")

            now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            insert_interview_log(conn, dict(
                token=token, domain=domain,
                question=row["question"],
                reference_answer=row["answer"],
                user_answer=ans,
                semantic_score=sem, keyword_coverage=cov, final_score=final
            ))
            st.session_state.results.append({"question": row["question"], "final": final})
            st.session_state.qidx += 1
            st.rerun()

        if c2.button("Skip"):
            insert_interview_log(conn, dict(
                token=token, domain=domain,
                question=row["question"],
                reference_answer=row["answer"],
                user_answer="",
                semantic_score=0.0, keyword_coverage=0.0, final_score=0.0
            ))
            st.session_state.results.append({"question": row["question"], "final": 0.0})
            st.session_state.qidx += 1
            st.rerun()
    else:
        st.success("🎉 Done!")
        if st.session_state.results:
            rdf = pd.DataFrame(st.session_state.results)
            st.metric("Average score", f"{rdf['final'].mean():.1f}%")
            st.dataframe(rdf)
        if st.button("Start over"):
            st.session_state.qidx = 0
            st.session_state.results = []
            st.rerun()
