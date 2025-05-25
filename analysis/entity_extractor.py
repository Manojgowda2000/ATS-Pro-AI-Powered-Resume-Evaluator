import spacy

# Load small or medium model
nlp = spacy.load("en_core_web_sm")

def extract_entities(text):
    doc = nlp(text)
    skills = []
    roles = []
    for ent in doc.ents:
        if ent.label_ in ['ORG', 'PERSON', 'GPE']:
            roles.append(ent.text)
        elif ent.label_ in ['NORP', 'FAC', 'PRODUCT']:
            skills.append(ent.text)
    return {
        "skills": list(set(skills)),
        "roles": list(set(roles))
    }
