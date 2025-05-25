import streamlit as st
from parser.resume_parser import parse_resume
from parser.job_description_parser import parse_job_description
from analysis.grammar_checker import check_grammar
from analysis.keyboard_usage import analyze_keyboard_usage
from analysis.score_calculator import calculate_ats_score

st.title("📝 Resume ATS Score Calculator")

uploaded_resume = st.file_uploader("Upload your Resume (PDF)", type="pdf")
job_desc = st.text_area("Paste Job Description here")

if uploaded_resume and job_desc:
    resume_text = parse_resume(uploaded_resume)
    jd_text = parse_job_description(job_desc)

    grammar_issues = check_grammar(resume_text)
    keyboard_analysis = analyze_keyboard_usage(resume_text)

    ats_score = calculate_ats_score(resume_text, jd_text, grammar_issues, keyboard_analysis)

    st.metric("ATS Score", f"{ats_score} / 100")
    st.write("**Grammar Issues:**", grammar_issues)
    st.write("**Keyboard Usage Issues:**", keyboard_analysis)