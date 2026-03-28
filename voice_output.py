import pyttsx3 as pt

def speak(text):
    engine = pt.init()
    engine.say(text)
    print("tts 정상 실행중")
    engine.runAndWait()