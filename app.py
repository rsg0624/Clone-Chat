import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from engine.intent import detect_intent
from engine.emotion import detect_emotion
from engine.personality import load_personality
from engine.action_mapper import map_to_action

st.set_page_config(layout="wide")
st.title("E1 – Avatar Thought → Action Simulator")

col1, col2, col3 = st.columns(3)

with col1:
    mode = st.selectbox("Mode", ["Professional", "Friends", "Inner Circle"])

with col2:
    involuntary = st.toggle("Enable Involuntary Reaction", value=True)

with col3:
    mood = st.selectbox("Mood Override", ["Auto", "Neutral", "Happy", "Tired", "Serious"])

st.divider()

left, center, right = st.columns([2, 5, 3])

with left:
    st.subheader("Avatar / Personality")
    personality_name = st.selectbox("Personality Profile", ["Witty", "Calm", "Sarcastic", "Humble"])
    personality = load_personality(personality_name)
    st.json(personality)

with center:
    st.subheader("Thought / Message Input")
    message = st.text_area("Enter text (thought / message)", height=120, placeholder="Example: Had your dinner?")
    run = st.button("Simulate")

    if run and message.strip():
        intent = detect_intent(message)
        emotion = detect_emotion(message)
        action = map_to_action(message, intent, emotion, personality, mode, involuntary)

        st.markdown("### 🎬 Resulting Avatar Action")
        st.success(action["description"])

with right:
    st.subheader("AI Reasoning")
    if run and message.strip():
        st.write("**Detected Intent**")
        st.code(intent)
        st.write("**Detected Emotion**")
        st.code(emotion)
        st.write("**Final Action Decision**")
        st.json(action)
