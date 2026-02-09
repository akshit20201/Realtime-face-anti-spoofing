🛡️ Real-Time Face Anti-Spoofing System (Real vs Fake)

A real-time face anti-spoofing system that detects whether a face shown to a webcam is REAL (live human) or FAKE (photo / mobile screen / printed image) using OpenCV and computer vision techniques.

This project is designed for academic / final-year / mini-project use and runs fully on a webcam without special hardware.

📌 Features

🎥 Real-time webcam face detection

🟩 Green box for REAL face

🟥 Red box for FAKE face

📊 Liveness score display

📱 Detects mobile phone photo spoofing

🖼️ Detects printed photo attacks

⚡ Lightweight (no heavy deep learning required)

🧠 How It Works

The system uses passive anti-spoofing techniques:

1️⃣ Face Detection

Haar Cascade (haarcascade_frontalface_default.xml)

Detects faces from live webcam feed

2️⃣ Liveness / Spoof Detection

The system checks:

Technique	Purpose
Blur Detection	Fake images are smoother
Texture Variance	Real skin has natural noise
Brightness Check	Mobile screens reflect light
Combined Threshold Logic	Improves accuracy

📱 Mobile phone photos usually:

Have smooth texture

High brightness

Artificial reflections
→ detected as FAKE

👤 Real faces:

Uneven skin texture

Natural shadows
→ detected as REAL


