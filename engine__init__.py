"""
Engine package for Clone-Chat (E1)

This package contains the core intelligence layer responsible for:
- Intent detection
- Emotion inference
- Personality modeling
- Action / reaction mapping

UI layers (Streamlit, Web, Mobile) should only interact with this package.
"""

from engine.intent import detect_intent
from engine.emotion import detect_emotion
from engine.action_mapper import map_to_action
from engine.personality import get_personality

__all__ = [
    "detect_intent",
    "detect_emotion",
    "map_to_action",
    "get_personality",
]
