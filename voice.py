import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
import os
import tempfile

def speak(text):
    print(f"Jarvis: {text}")
    try:
        tts = gTTS(text=text, lang='en')
        with tempfile.NamedTemporaryFile(delete=False, suffix='.mp3') as f:
            tmpfile = f.name
        tts.save(tmpfile)
        playsound(tmpfile)
        os.remove(tmpfile)
    except Exception as e:
        print(f"Speech error: {e}")

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        audio = recognizer.listen(source, timeout=5, phrase_time_limit=10)
    try:
        query = recognizer.recognize_google(audio)
        print(f"You said: {query}")
        return query.lower()
    except sr.UnknownValueError:
        speak("Sorry, I didn't catch that.")
        return ""
    except sr.WaitTimeoutError:
        return ""