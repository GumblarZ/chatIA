import pyttsx3
import module.sanitization as trat

def speak(text):
    tt = trat.remove_tag_content(text)
<<<<<<< Updated upstream
=======
    ##print(f"Assistente: {text}")
>>>>>>> Stashed changes
    engine = pyttsx3.init()
    engine.say(tt)
    engine.runAndWait()
    