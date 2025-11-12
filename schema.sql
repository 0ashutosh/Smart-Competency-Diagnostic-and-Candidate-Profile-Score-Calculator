-- ==========================================================
-- Database: smart_competency_diagnostic
-- Author: Ashutosh Agrawal, Ashutosh Kumar Sharma, Anamaneni Abhilash
-- Description: Schema for Smart Competency Diagnostic & Candidate Profile Score Calculator
-- ==========================================================

CREATE DATABASE IF NOT EXISTS smart_competency_diagnostic;
USE smart_competency_diagnostic;

-- ==========================================================
-- Table: user_data
-- Stores user information, resume data, predicted fields, and recommendations
-- ==========================================================
CREATE TABLE IF NOT EXISTS user_data (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    token VARCHAR(50) NOT NULL,
    ip VARCHAR(50),
    host VARCHAR(100),
    os VARCHAR(100),
    name VARCHAR(200),
    email VARCHAR(200),
    phone VARCHAR(50),
    degree VARCHAR(200),
    page_count INT,
    predicted_field VARCHAR(200),
    user_level VARCHAR(50),
    skills JSON,
    recommended_skills JSON,
    recommended_courses JSON,
    resume_score INT,
    pdf_filename VARCHAR(200),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- ==========================================================
-- Table: interview_logs
-- Stores competency test logs and semantic evaluation results
-- ==========================================================
CREATE TABLE IF NOT EXISTS interview_logs (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    token VARCHAR(50) NOT NULL,
    domain VARCHAR(100) NOT NULL,
    question TEXT NOT NULL,
    reference_answer TEXT NOT NULL,
    user_answer TEXT,
    semantic_score FLOAT,
    keyword_coverage FLOAT,
    final_score FLOAT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- ==========================================================
-- Table: user_feedback
-- Stores user feedback and satisfaction scores
-- ==========================================================
CREATE TABLE IF NOT EXISTS user_feedback (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL,
    score INT NOT NULL,
    comments TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- ==========================================================
-- Optional Indexes for Faster Queries
-- ==========================================================
CREATE INDEX idx_user_token ON user_data (token);
CREATE INDEX idx_log_token ON interview_logs (token);
CREATE INDEX idx_feedback_email ON user_feedback (email);

-- ==========================================================
-- End of Schema
-- ==========================================================
