import streamlit as st
from gtts import gTTS
import os
import tempfile

st.set_page_config(page_title="Learn Kannada via Hindi", page_icon="🗣️", layout="centered")

st.title("🗣️ Learn Kannada using Hindi")
st.subheader("छोटे-छोटे वाक्यों से सीखिए ಕನ್ನಡ ಭಾಷೆ")

# --- Lesson Selection ---
lessons = {
    "Greetings (नमस्ते / ನಮಸ್ಕಾರ)": [
        ("Hello", "नमस्ते", "ನಮಸ್ಕಾರ (Namaskāra)"),
        ("How are you?", "आप कैसे हैं?", "ಹೇಗಿದ್ದೀರಾ (Hegiddīrā)"),
        ("Thank you", "धन्यवाद", "ಧನ್ಯವಾದಗಳು (Dhanyavādagaḷu)")
    ],
    "Daily Words (रोज़मर्रा के शब्द)": [
        ("Water", "पानी", "ನೀರು (Nīru)"),
        ("Food", "भोजन", "ಆಹಾರ (Āhāra)"),
        ("Name", "नाम", "ಹೆಸರು (Hesaru)")
    ],
}

choice = st.selectbox("Choose a topic:", list(lessons.keys()))

st.image("https://media.giphy.com/media/fxsqOYnIMEefC/giphy.gif", width=200)

st.markdown("### ✨ Learn these Kannada phrases with Hindi help")

# --- Display Lesson ---
for eng, hindi, kannada in lessons[choice]:
    st.markdown(f"**{eng}**  \n🗣️ Hindi: {hindi}  \n💬 Kannada: {kannada}")

    # Text to speech (Hindi explanation)
    if st.button(f"🔊 Hear Hindi for '{eng}'"):
        tts = gTTS(text=f"{eng} का कन्नड़ में मतलब है {kannada}", lang='hi')
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmp:
            tts.save(tmp.name)
            st.audio(tmp.name)

st.success("✅ Keep practicing daily — थोड़ा-थोड़ा बोलिए हर दिन!")
