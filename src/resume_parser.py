import re
from typing import Dict, List, Tuple
from pypdf import PdfReader

EMAIL_RE = re.compile(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+")
PHONE_RE = re.compile(r"(\+?\d[\d \-()]{7,}\d)")

# Simple “degree” detector
DEGREES = [
    "B.Tech", "BTech", "B.E", "BE", "BSc", "BS", "BCA",
    "M.Tech", "MTech", "M.E", "ME", "MSc", "MS", "MCA",
    "PhD", "Doctorate", "MBA"
]

def pdf_to_text(file_path: str) -> Tuple[str, int]:
    reader = PdfReader(file_path)
    pages = len(reader.pages)
    text = []
    for p in reader.pages:
        try:
            text.append(p.extract_text() or "")
        except Exception:
            text.append("")
    return "\n".join(text), pages

def extract_email(text: str) -> str:
    m = EMAIL_RE.search(text)
    return m.group(0) if m else ""

def extract_phone(text: str) -> str:
    m = PHONE_RE.search(text)
    return m.group(1).strip() if m else ""

def extract_name_guess(text: str) -> str:
    # naive: first non-empty line, title-case few words
    for line in text.splitlines():
        s = line.strip()
        if 2 <= len(s.split()) <= 5 and s[0].isalpha():
            return s
    return ""

def extract_degree(text: str) -> str:
    t = text.replace(".", "").upper()
    for d in DEGREES:
        if d.replace(".", "").upper() in t:
            return d
    return ""

def extract_skills(text: str, skillbank: List[str]) -> List[str]:
    t = " " + re.sub(r"[^a-zA-Z0-9#+.\- ]", " ", text.lower()) + " "
    found = set()
    for sk in skillbank:
        pat = r"\b" + re.escape(sk.lower()) + r"\b"
        if re.search(pat, t):
            found.add(sk)
    return sorted(found)

def parse_resume(file_path: str, skillbank: List[str]) -> Dict:
    text, pages = pdf_to_text(file_path)
    name  = extract_name_guess(text)
    email = extract_email(text)
    phone = extract_phone(text)
    degree = extract_degree(text)
    skills = extract_skills(text, skillbank)
    return dict(
        raw_text=text,
        pages=pages,
        name=name,
        email=email,
        phone=phone,
        degree=degree,
        skills=skills
    )
