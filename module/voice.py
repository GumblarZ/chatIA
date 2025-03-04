import pyttsx3
import module.tratamento as trat

def speak(text):
    tt = trat.remove_tag_content(text)
    print(f"Assistente: {text}")
    engine = pyttsx3.init()
    engine.say(tt)
    engine.runAndWait()
    