import os
import datetime
import mss
import mss.tools

folder_in_ai = os.path.dirname(os.path.abspath(__file__))
folder = os.path.join(folder_in_ai, "captures")

def clear_old_captures():
    if not os.path.exists(folder):
        return

    for file_name in os.listdir(folder):
        if file_name.lower().endswith(".png"):
            file_path = os.path.join(folder, file_name)
            try:
                os.remove(file_path)
                print("이전 캡처 삭제:", file_path)
            except Exception as e:
                print("삭제 실패:", file_path, e)


def capture_screen():
    print("캡처 실행됨!")

    if not os.path.exists(folder):
        os.mkdir(folder)

    clear_old_captures()

    now = datetime.datetime.now()
    time_str = now.strftime("%Y%m%d_%H%M%S")
    filename = "screen_" + time_str + ".png"
    filepath = os.path.join(folder, filename)

    with mss.mss() as sct:
        screenshot = sct.grab(sct.monitors[2])
        mss.tools.to_png(
            screenshot.rgb,
            screenshot.size,
            output=filepath
        )

    print("저장 완료:", filepath)
    return filepath