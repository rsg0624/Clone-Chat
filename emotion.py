def detect_emotion(text):
    text = text.lower()
    if any(word in text for word in ["lol", "haha", "😂"]):
        return "amusement"
    if "?" in text:
        return "confusion"
    return "neutral"