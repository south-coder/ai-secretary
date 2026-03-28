import tkinter as tk
from tkinter import messagebox
from Main import run_pro
from PIL import Image, ImageTk
import os
import keyboard as kb


# ---------------------------
# 기본 창 설정
# ---------------------------
root = tk.Tk()
root.title("AI SECRETARY")
root.geometry("800x600")
root.resizable(False, False)
root.configure(bg="#e9e9e9")

frames = {}

#---------------------------
# 공통 함수
#---------------------------
def update_capture_image(image_path):
    img= Image.open(image_path)
    img= img.resize((475,265))
    photo = ImageTk.PhotoImage(img)

    capture_box.config(image=photo, text="")
    capture_box.image = photo
#--------------------------------------------------------
hotkey_registered = False
hotkey_id= None
def run_by_hotkey():
    api_key = app_state.get("api_key", "").strip()

    root.after(0, lambda: status_label.config(text="상태 : 실행중...", fg="#1e88e5"))

    try:
        result, image_path = run_pro(api_key)
        root.after(0, lambda r=result, p=image_path: finish_run(r, p))
    except Exception as e:
        root.after(0, lambda err=e: show_run_error(err))
#----------------------------------------------------------------
def start_hotkey_mode():
    global hotkey_registered, hotkey_id

    api_key = app_state.get("api_key","").strip()

    if not api_key:
        messagebox.showerror("잠깐", "API 키가 없습니다!")
        show_frame("api_page")
        return
    if not hotkey_registered:
        hotkey_id = kb.add_hotkey("F2",run_by_hotkey)
        hotkey_registered = True
    run_button.config(text="중단",command=stop_hot_mode)
    status_label.config(text="상태 : 'F2' 대기중...", fg="#ff9800")
#----------------------------------------------------------------
def stop_hot_mode():
    global hotkey_registered,hotkey_id

    if hotkey_registered and hotkey_id is not None:
        kb.remove_hotkey(hotkey_id)
        hotkey_id=None
        hotkey_registered= False
    
    run_button.config(text="실행",command=start_hotkey_mode)
    status_label.config(text="상태 : 대기중", fg="#555555")
#----------------------------------------------------------------
def finish_run(result,image_path):
    status_label.config(text="상태 : 완료!", fg="#2e7d32")
    result_text.delete("1.0", tk.END)
    result_text.insert(tk.END, str(result))
    update_capture_image(image_path)
#----------------------------------------------------------------
def show_run_error(e):
    status_label.config(text="상태 : 오류", fg="red")
    result_text.delete("1.0", tk.END)
    result_text.insert(tk.END, f"오류 발생:\n{e}")
#----------------------------------------------------------------
def show_frame(name):
    frames[name].tkraise()
#----------------------------------------------------------------
def save_api_and_next():
    api_key = api_entry.get().strip()

    if api_key.startswith("OPENAI_API_KEY="):
        api_key = api_key.replace("OPENAI_API_KEY=", "", 1).strip()

    if not api_key:
        messagebox.showwarning("경고", "API 키를 입력해주세요.")
        return

    app_state["api_key"] = api_key
    show_frame("main_page")
#----------------------------------------------------------------
def agree_and_start():
    show_frame("api_page")
#----------------------------------------------------------------
def run_program():
    print("run_program 진입")
    api_key = app_state.get("api_key", "").strip()

    if not api_key:
        messagebox.showwarning("경고", "API 키가 없습니다. 다시 입력해주세요.")
        show_frame("main_page")
        return

    status_label.config(text="상태 : 실행 중...", fg="#1e88e5")
    result_text.delete("1.0", tk.END)
    result_text.insert(tk.END, "작업을 시작합니다...\n")
    root.update()


    try:
        result = run_pro(api_key)

        status_label.config(text="상태 : 완료", fg="#2e7d32")
        result_text.delete("1.0", tk.END)
        result_text.insert(tk.END, result)

        # 입력값 박스에도 결과를 임시 표시
        input_box.config(state="normal")
        input_box.delete("1.0", tk.END)
        input_box.insert(tk.END, "음성 입력 완료 / GPT 응답 생성 완료")
        input_box.config(state="disabled")

    except Exception as e:
        status_label.config(text="상태 : 오류", fg="red")
        result_text.delete("1.0", tk.END)
        result_text.insert(tk.END, f"오류 발생:\n{e}")
#----------------------------------------------------------------
def mic_click():
    input_box.config(state="normal")
    input_box.delete("1.0", tk.END)
    input_box.insert(tk.END, "마이크 버튼 클릭됨\n실제 음성 입력은 실행 버튼 또는 F2 흐름에서 동작합니다.")
    input_box.config(state="disabled")
#----------------------------------------------------------------
def make_page(name):
    frame = tk.Frame(root, bg="#e9e9e9")
    frame.place(x=0, y=0, relwidth=1, relheight=1)
    frames[name] = frame
    return frame
#----------------------------------------------------------------
def add_logo(frame):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    img_path = os.path.join(base_dir, "images", "logo.png")

    img = Image.open(img_path)
    img = img.resize((100, 100))

    logo_img = ImageTk.PhotoImage(img)

    logo = tk.Label(frame, image=logo_img, bg="#e9e9e9")
    logo.image = logo_img

    logo.place(x=690, y=5)
#----------------------------------------------------------------
def add_big_button(frame, text, command, x, y, w=380, h=70):
    btn = tk.Button(
        frame,
        text=text,
        command=command,
        font=("Pretendard", 26, "bold"),
        bg="#2f55e7",
        fg="white",
        activebackground="#2447c9",
        activeforeground="white",
        relief="flat",
        bd=0,
        cursor="hand2"
    )
    btn.place(x=x, y=y, width=w, height=h)
    return btn
#----------------------------------------------------------------
# 상태 저장
# ---------------------------
app_state = {
    "api_key": ""
}


# ---------------------------
intro1 = make_page("intro1")
add_logo(intro1)

tk.Label(
    intro1,
    text="안녕하세요 사용자님!\n지금부터 AI SECRETARY\n의 사용방법을 설명드릴게요",
    font=("Pretendard", 38, "bold"),
    fg="#2f55e7",
    bg="#e9e9e9",
    justify="center"
).place(x=90, y=180)

skip_btn = tk.Button(
    intro1,
    text="건너뛰기",
    command=lambda: show_frame("license_page"),
    font=("Pretendard", 30, "bold"),
    fg="#2f55e7",
    bg="#e9e9e9",
    relief="flat",
    bd=0,
    cursor="hand2"
)
skip_btn.place(x=435, y=465, width=175, height=70)

next_btn = tk.Button(
    intro1,
    text="다음",
    command=lambda: show_frame("intro2"),
    font=("Pretendard", 30, "bold"),
    fg="#2f55e7",
    bg="#e9e9e9",
    bd=0,
    cursor="hand2"
)
next_btn.place(x=190, y=465, width=150, height=70)

#-----------------------------------------------------------------------------
intro2 = make_page("intro2")
add_logo(intro2)

tk.Label(
    intro2,
    text="시스템은 사용자의\n음성인식으로 작동합니다.",
    font=("Pretendard", 38, "bold"),
    fg="#2f55e7",
    bg="#e9e9e9",
    justify="center"
).place(x=100, y=190)

add_big_button(intro2, "다음", lambda: show_frame("intro3"), 210, 465)
#-----------------------------------------------------------------------------
intro3 = make_page("intro3")
add_logo(intro3)

tk.Label(
    intro3,
    text='프로그램에서 할당된\n"F2" 버튼을 누르면 자동으로\n마이크와 함께 실행\n현재 화면을 캡쳐합니다.',
    font=("Pretendard", 38, "bold"),
    fg="#2f55e7",
    bg="#e9e9e9",
    justify="center"
).place(x=90, y=150)

add_big_button(intro3, "다음", lambda: show_frame("intro4"), 210, 465)
#-----------------------------------------------------------------------------
intro4 = make_page("intro4")
add_logo(intro4)

tk.Label(
    intro4,
    text='그후 화면에 대한\n질문을 하면 됩니다.\n간단하죠?',
    font=("Pretendard", 38, "bold"),
    fg="#2f55e7",
    bg="#e9e9e9",
    justify="center"
).place(x=180, y=190)

add_big_button(intro4, "다음", lambda: show_frame("intro5"), 210, 465)
#-----------------------------------------------------------------------------
intro5 = make_page("intro5")
add_logo(intro5)

tk.Label(
    intro5,
    text="그럼 시작해 볼까요?",
    font=("Pretendard", 38, "bold"),
    fg="#2f55e7",
    bg="#e9e9e9"
).place(x=180, y=250)

add_big_button(intro5, "다음", lambda: show_frame("license_page"), 210, 465)


# ---------------------------
api_page = make_page("api_page")
add_logo(api_page)

tk.Label(
    api_page,
    text="사용자의 API를 입력해 주세요",
    font=("Pretendard", 26, "bold"),
    fg="#2f55e7",
    bg="#e9e9e9"
).place(x=150, y=70, width=500, height=50)

api_entry = tk.Entry(
    api_page,
    font=("Pretendard", 18),
    relief="flat",
    bd=0
)
api_entry.place(x=60, y=140, width=690, height=72)

tk.Label(
    api_page,
    text="보안 안내",
    font=("Pretendard", 20, "bold"),
    fg="#2f55e7",
    bg="#e9e9e9",
).place(x=60, y=220)

security_text = (
    "본 프로그램은 사용자의 API Key를 외부로 전송하거나 저장하지 않으며, "
    "모든 처리는 사용자의 로컬 환경에서 직접 이루어집니다.\n\n"
    "다만, OpenAI API 호출 과정에서 해당 Key는 OpenAI 서버와 통신에 사용됩니다. "
    "이는 OpenAI의 공식 정책에 따른 정상적인 동작입니다.\n"
    "**만약 api 입력이 어렵다면 사용하지 않을것을 권장 합니다**\n"
    "(프로그램은 외부와 통신을 하지 않습니다!)"
)

tk.Label(
    api_page,
    text=security_text,
    font=("Pretendard", 17, "bold"),
    fg="#595959",
    bg="#e9e9e9",
    justify="left",
    wraplength=680
).place(x=60, y=260)

add_big_button(api_page, "다음", save_api_and_next, 210, 495)


# ---------------------------
# license_page
# ---------------------------
license_page = make_page("license_page")
add_logo(license_page)

tk.Label(
    license_page,
    text="사용권 동의",
    font=("Pretendard", 28, "bold"),
    fg="white",
    bg="#2f55e7"
).place(x=130, y=10, width=550, height=70)

license_text = (
    "[프로그램 사용권 및 면책 조항]\n\n"
    "-본 프로그램은 OpenAI API 사용 과정에서의 불편함을 개선하고,"
    "사용자의\n 작업 효율을 향상시키기 위한 목적으로 개발되었습니다.\n"
    "-본 프로그램의 저작권은 제작자에게 있으며,"
    "제작자의 명시적인 허가 없이\n 본 프로그램을 무단으로 복제, 배포, 판매하는 행위를 금지합니다.\n\n"
    "사용자는 본 프로그램을 사용하는 과정에서 발생할 수 있는 모든 결과 및\n 책임에 대해"
    "전적으로 본인의 책임 하에 이용하여야 합니다.\n\n"
    "-본 프로그램은 외부 API(OpenAI 등)를 활용하며,\n"
    "API 사용으로 인해 발생하는 비용, 오류, 데이터 처리 결과 등에 대해서도\n"
    "제작자는 어떠한 책임도 지지 않습니다.\n"
    "-또한 본 프로그램의 사용으로 인해 발생하는 직·간접적인 손해,\n"
    "데이터 손실, 시스템 오류 등에 대해 제작자는 법적 책임을 지지 않습니다.\n"
    "특정 목적에 대한 적합성이나 안정성을 보장하지 않습니다.\n"
    "-본 조항에 동의하지 않을 경우 프로그램 사용을 중단해야 합니다."
)

license_label = tk.Label(
    license_page,
    text=license_text,
    font=("Pretendard", 14, "bold"),
    fg="#595959",
    bg="#e9e9e9",
    justify="center",
    wraplength=620
)
license_label.place(x=100, y=100)

add_big_button(license_page, "동의합니다", agree_and_start, 210, 500)


# ---------------------------
# main_page
# ---------------------------
main_page = make_page("main_page")
add_logo(main_page)

guide_label = tk.Label(
    main_page,
    text="실행 클릭시 F2를 누르면 작업 실행",
    font=("Pretendard", 12),
    fg="black",
    bg="#e9e9e9"
)
guide_label.place(x=45, y=35)

# 실행 버튼
run_button = tk.Button(
    main_page,
    text="실행",
    command=start_hotkey_mode,
    font=("Pretendard", 28, "bold"),
    bg="#3558e8",
    fg="white",
    activebackground="#2a49c3",
    activeforeground="white",
    relief="flat",
    bd=0,
    cursor="hand2"
)
run_button.place(x=70, y=85, width=120, height=120)

# 마이크 버튼
mic_button = tk.Button(
    main_page,
    text="🎤",
    command=mic_click,
    font=("Pretendard", 42),
    bg="#2ba3e8",
    fg="white",
    activebackground="#2187be",
    activeforeground="white",
    relief="flat",
    bd=0,
    cursor="hand2"
)
mic_button.place(x=70, y=225, width=120, height=120)

# 캡처 화면 자리
capture_box = tk.Label(
    main_page,
    text="캡처된 화면",
    font=("Pretendard", 28, "bold"),
    fg="#cfcfcf",
    bg="#8d8d8d"
)
capture_box.place(x=270, y=85, width=475, height=265)

# 입력값 박스
input_box = tk.Text(
    main_page,
    font=("Pretendard", 18, "bold"),
    bg="#dddddd",
    fg="#8c8c8c",
    relief="flat",
    bd=0
)
input_box.place(x=55, y=390, width=690, height=120)
input_box.insert("1.0", "입력값")
input_box.config(state="disabled")

# 상태 표시
status_label = tk.Label(
    main_page,
    text="상태 : 대기",
    font=("Pretendard", 14, "bold"),
    fg="#555555",
    bg="#e9e9e9"
)
status_label.place(x=55, y=530)

# 결과창
result_text = tk.Text(
    main_page,
    font=("Pretendard", 11),
    bg="white",
    fg="black",
    relief="solid",
    bd=1
)
result_text.place(x=270, y=530, width=475, height=50)
result_text.insert("1.0", "여기에 결과가 표시됩니다.")


# ---------------------------
# 시작 화면
# ---------------------------
show_frame("intro1")
root.mainloop()
