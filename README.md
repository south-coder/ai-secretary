# AI Secretary v1.0

## 🔹 Overview
AI Secretary is a Python-based AI automation tool designed to simplify user workflows.

This project integrates screen capture, voice input, AI processing, and text-to-speech output into a single streamlined system.

---

## 🎬 Demo Video
[Watch Demo](https://youtu.be/oqLrI7nKdbc)

---
## 📸 Demo Flow

ui operation sequence
1#
<img width="798" height="629" alt="1" src="https://github.com/user-attachments/assets/08d8b81c-9ece-4c27-a323-b28ecd813ea8" />
Introduction screen

The program starts with a simple onboarding screen that guides the user through how the system works.
2#
<img width="798" height="625" alt="2" src="https://github.com/user-attachments/assets/b96b415d-53fa-424c-93c9-71acf8123eb1" />
Voice-based interaction

The system operates through voice input, allowing users to interact naturally without typing.
3#
<img width="799" height="627" alt="3" src="https://github.com/user-attachments/assets/3f3bbf89-cb79-40c5-8390-fdd043b30266" />
Hotkey execution (F2)

Pressing the assigned F2 key triggers the system, activating both screen capture and voice input.
4#
<img width="799" height="628" alt="4" src="https://github.com/user-attachments/assets/e4bfc626-e12d-4793-84de-2d3029460b20" />
Ask about the screen

Users can ask questions about the current screen after activation.
5#
<img width="800" height="628" alt="5" src="https://github.com/user-attachments/assets/2eb2059e-1625-44c3-9760-427f61d44387" />
Ready to start

The system is now ready to begin interaction.
6#
<img width="800" height="631" alt="6" src="https://github.com/user-attachments/assets/206557ce-5ac3-4ddd-86a2-ee44fbe18cc2" />
License agreement

The user must agree to the terms before using the program.
7#
<img width="800" height="628" alt="7" src="https://github.com/user-attachments/assets/fdb4a573-9ca5-4f6e-aa51-ef7af0625a2a" />
API key input

Users enter their API key to enable AI functionality.
The program runs locally and does not store the key externally.
8#
<img width="798" height="632" alt="8" src="https://github.com/user-attachments/assets/43bdce4b-d072-41eb-9f41-9e843b466db8" />
Main interface (idle state)

The main interface includes:

Run button
Microphone button
Screen preview area
Result display area
9#
<img width="797" height="625" alt="9" src="https://github.com/user-attachments/assets/9093f44d-008e-4420-862c-a5290249e152" />
Waiting for F2 input

After clicking run, the system waits for the F2 key to start processing.
10#
<img width="800" height="627" alt="10" src="https://github.com/user-attachments/assets/e94584a1-791a-47c6-aa1c-d4464ed76073" />
Microphone interaction

The microphone button provides user guidance,
while actual voice input is handled through the run/F2 flow.
11#
<img width="1644" height="907" alt="11" src="https://github.com/user-attachments/assets/9e9e7be2-6327-459b-966c-78460f3024c8" />
Execution result

The system captures the screen, processes voice input,
and generates AI responses in real time.
---

## 🚀 Features
- Screen capture
- Voice input (speech recognition)
- AI response generation
- Text-to-speech output
- Simple UI
- Hotkey execution (F2)

---

## 🧠 How It Works
1. Click the Run button  
2. Press F2  
3. Screen is captured  
4. Voice input is recorded  
5. AI analyzes the input  
6. Result is returned (text + speech)

---

## 🛠 Tech Stack
- Python
- Tkinter
- OpenAI API
- SpeechRecognition
- pyttsx3
- mss

---

## 📂 Structure
Main.py
Ui.py
gpt_client.py
Screen_capture.py
voice_input.py
voice_output.py

---

## ⚠️ Security
- Runs locally
- No external storage of API key
- Be careful when API key is visible on screen

---

## 🔄 Version
### v1.0
- Prototype completed
- Core functionality implemented

### v1.5 (Planned)
- UI → PyQt
- Better TTS
- Refactoring

---

## 👨‍💻 Developer
SACO

---

## 🎯 Final Note
This project focuses on integrating multiple features into one seamless user experience.

Video icon address https://icons8.kr/icons
