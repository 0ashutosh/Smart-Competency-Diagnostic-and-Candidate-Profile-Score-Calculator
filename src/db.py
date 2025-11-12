import os
import pymysql
from dotenv import load_dotenv

load_dotenv()  # loads .env file if present

def get_conn():
    return pymysql.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME"),
        cursorclass=pymysql.cursors.DictCursor
    )

def insert_user_data(conn, row):
    with conn.cursor() as cur:
        cur.execute("""
    INSERT INTO user_data
    (token, ip, host, os, name, email, phone, degree, page_count,
     predicted_field, user_level, skills, recommended_skills, recommended_courses,
     resume_score, pdf_filename)
    VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
""", (
    row["token"], row["ip"], row["host"], row["os"], row["name"], row["email"],
    row["phone"], row["degree"], row["page_count"], row["predicted_field"],
    row["user_level"], row["skills"], row["recommended_skills"], 
    row["recommended_courses"], row["resume_score"], row["pdf_filename"]
))

    conn.commit()

def insert_feedback(conn, name, email, score, comments):
    sql = """
        INSERT INTO user_feedback (name, email, score, comments, created_at)
        VALUES (%s, %s, %s, %s, NOW())
    """
    with conn.cursor() as cur:
        cur.execute(sql, (name, email, score, comments))
    conn.commit()

def insert_interview_log(conn, row: dict):
    cols = ",".join(row.keys())
    vals = ",".join(["%s"]*len(row))
    sql = f"INSERT INTO interview_logs ({cols}) VALUES ({vals})"
    with conn.cursor() as cur:
        cur.execute(sql, list(row.values()))
