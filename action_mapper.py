def map_to_action(message, intent, emotion, personality, mode, involuntary):
    if mode == "Professional":
        return {
            "type": "neutral_ack",
            "description": "Avatar gives a calm nod (professional-safe)."
        }

    if involuntary and intent == "question" and emotion == "confusion":
        if personality.get("sarcasm", 0) > 0.6:
            return {
                "type": "micro_reaction",
                "description": "Avatar raises eyebrow with a subtle smirk (confused sarcasm)."
            }

    return {
        "type": "neutral",
        "description": "Avatar maintains a neutral attentive expression."
    }