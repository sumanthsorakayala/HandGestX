# 🖐️ HandGestX – Control Your Computer with Hand Gestures using OpenCV & MediaPipe
HandGestX is a Python-based desktop automation project that allows users to control their computer using hand gestures captured via webcam. Using MediaPipe for real-time hand tracking and PyAutoGUI for mouse/keyboard control, it turns your hand into a virtual controller — no hardware required.

✨ Features
🎯 Real-time mouse control using index finger

🖱️ Left click, Right click, and Mouse hold gestures

🔊 Volume up/down with specific hand signs

🧭 Scroll up/down using finger movements

📷 Built with OpenCV, MediaPipe, PyAutoGUI

💻 Packaged as a standalone Windows .exe using PyInstaller

🛠️ Tech Stack
Python 3.12

OpenCV

MediaPipe

PyAutoGUI

PyInstaller

🧠 How It Works
Tracks 21 hand landmarks in real time using webcam

Identifies gestures (e.g., finger count, tip positions)

Maps gestures to system control actions

🚀 Getting Started
To run the source code:

bash
Copy
Edit
pip install opencv-python mediapipe pyautogui
python main.py
