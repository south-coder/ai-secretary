import Screen_capture
import voice_input
from gpt_client import ask_gpt
from voice_output import speak
import os

print("메인 경로",__file__)

def run_pro(api_key):
    print("run_pro 시작")
    print("프로그램을 실행 합니다")

    capture = Screen_capture.capture_screen()
    print("캡처 완료")

    text = voice_input.vtext()
    print("음성 입력 함수 종료")
    print("입력값:", text)

    if not text:
        return "음성 입력값이 없습니다.", capture

    result = ask_gpt(text, capture, api_key)
    print("답변:", result)

    if result:
        speak(result)

    print("이미지 경로:", capture)
    return result, capture


if __name__ == "__main__":
    pass
    