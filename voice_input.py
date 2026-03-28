import speech_recognition as sr
import winsound as ws
import os

print("보이스 인풋 경로",__file__)

print("vtext 로드됨")

def vtext():
    print("vtext 실행중")
    
    dorp = sr.Recognizer()

    base_dir=os.path.dirname(os.path.abspath(__file__))
    sound_path= os.path.join(base_dir, "voice_on.wav")


    with sr.Microphone() as mic:
        print("마이크 실행됨")
        ws.PlaySound(sound_path, ws.SND_FILENAME)
        
        try:
            print("음성 입력 대기 중...")
            audio = dorp.listen(mic, timeout=7, phrase_time_limit=20)

            print("음성 인식 중...")
            text = dorp.recognize_google(audio, language="ko-KR")

            print("입력값:", text)
            return text

        except sr.WaitTimeoutError:
            print("시간 초과 (말 안함)")
            return None

        except Exception as e:
            print("음성 인식 실패:", e)
            return None