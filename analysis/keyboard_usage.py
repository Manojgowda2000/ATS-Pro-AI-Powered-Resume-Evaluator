def analyze_keyboard_usage(text):
    filler_words = ['basically', 'actually', 'very', 'just', 'kind of', 'sort of']
    usage = {word: text.lower().count(word) for word in filler_words if word in text.lower()}
    return usage