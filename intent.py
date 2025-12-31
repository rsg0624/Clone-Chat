def detect_intent(text):
    text = text.lower()
    if "?" in text:
        return "question"
    if any(word in text for word in ["lol", "haha", "😂"]):
        return "humor"
    return "statement"