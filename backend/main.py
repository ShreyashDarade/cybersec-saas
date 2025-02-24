from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
import mysql.connector
import ollama

app = FastAPI()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Database Connection
def get_db():
    return mysql.connector.connect(
        host="mysql_db",
        user="root",
        password="1234",
        database="cybersec"
    )

@app.get("/risks")
def get_risks(token: str = Depends(oauth2_scheme)):
    """Fetch risk assessments"""
    db = get_db()
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM risks")
    risks = cursor.fetchall()
    return {"risks": risks}

@app.post("/analyze-threats/")
def analyze_threats(log_data: str):
    """Analyze security logs with AI"""
    response = ollama.chat(model="llama3", messages=[{"role": "user", "content": log_data}])
    return {"analysis": response['message']}
