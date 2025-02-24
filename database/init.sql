CREATE DATABASE IF NOT EXISTS cybersec;
USE cybersec;

CREATE TABLE risks (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    impact VARCHAR(255)
);

INSERT INTO risks (name, impact) VALUES ('SQL Injection', 'High'), ('Phishing Attack', 'Medium');
