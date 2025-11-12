import base64
import streamlit as st
import socket, platform, secrets

def download_link_df(df, filename="data.csv", label="Download CSV"):
    csv = df.to_csv(index=False).encode("utf-8")
    b64 = base64.b64encode(csv).decode()
    href = f'<a href="data:file/csv;base64,{b64}" download="{filename}">{label}</a>'
    st.markdown(href, unsafe_allow_html=True)

def get_env_info():
    host = socket.gethostname()
    try:
        ip = socket.gethostbyname(host)
    except Exception:
        ip = ""
    osver = f"{platform.system()} {platform.release()}"
    tok = secrets.token_urlsafe(12)
    return tok, ip, host, osver

SECTION_HINTS = [
    ("objective", 6),
    ("summary", 6),
    ("education", 12),
    ("experience", 16),
    ("internship", 6),
    ("skills", 7),
    ("hobbies", 4),
    ("interests", 5),
    ("achievements", 13),
    ("certifications", 12),
    ("projects", 19),
]

def score_resume(raw_text: str) -> int:
    text = raw_text.lower()
    score = 0
    for key, pts in SECTION_HINTS:
        if key in text:
            score += pts
    return min(score, 100)  # cap
