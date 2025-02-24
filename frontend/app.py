import streamlit as st
import requests

BASE_URL = "http://backend:8000"

st.title("Cybersecurity SaaS Platform")

# Fetch risk assessments
if st.button("View Risk Assessments"):
    response = requests.get(f"{BASE_URL}/risks", headers={"Authorization": "Bearer your_token"})
    risks = response.json().get("risks", [])
    for risk in risks:
        st.write(risk)

# AI Threat Analysis
log_data = st.text_area("Enter security logs for AI analysis")
if st.button("Analyze Threats"):
    response = requests.post(f"{BASE_URL}/analyze-threats/", json={"log_data": log_data})
    st.write(response.json()["analysis"])
