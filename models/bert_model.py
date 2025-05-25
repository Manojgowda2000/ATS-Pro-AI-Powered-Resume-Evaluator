from transformers import BertTokenizer, BertModel
import torch
from sklearn.metrics.pairwise import cosine_similarity

tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = BertModel.from_pretrained('bert-base-uncased')

def embed_text(text):
    inputs = tokenizer(text, return_tensors='pt', truncation=True, max_length=512)
    with torch.no_grad():
        outputs = model(**inputs)
    return outputs.last_hidden_state[:, 0, :].numpy()

def get_jd_resume_similarity(resume_text, jd_text):
    resume_vec = embed_text(resume_text)
    jd_vec = embed_text(jd_text)
    score = cosine_similarity(resume_vec, jd_vec)[0][0]
    return round(score * 100, 2)