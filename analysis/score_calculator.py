from models.bert_model import get_jd_resume_similarity

def calculate_ats_score(resume_text, jd_text, grammar_issues, keyboard_issues):
    similarity = get_jd_resume_similarity(resume_text, jd_text)  # out of 100
    grammar_penalty = min(len(grammar_issues) * 0.5, 20)
    filler_penalty = min(sum(keyboard_issues.values()) * 1, 10)

    score = similarity - grammar_penalty - filler_penalty
    return round(max(0, score), 2)