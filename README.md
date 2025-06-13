
# 🖱️ AI Virtual Mouse

Control your computer mouse with hand gestures using computer vision and artificial intelligence. This project uses OpenCV, MediaPipe, and PyAutoGUI to detect hand landmarks and translate gestures into mouse movements and clicks in real time.

![AI Virtual Mouse Demo](https://user-images.githubusercontent.com/your-gif-link-if-available.gif)

## 🚀 Features

* Real-time hand tracking using webcam
* Move mouse with your index finger
* Click actions based on finger gestures
* Supports left-click and right-click
* Lightweight and runs on most machines
* No external hardware required

## 📸 Demo

> Add a demo video or GIF here
> *(Optional but recommended for better engagement)*

## 🛠️ Technologies Used

* [OpenCV](https://opencv.org/)
* [MediaPipe](https://developers.google.com/mediapipe)
* [PyAutoGUI](https://pyautogui.readthedocs.io/en/latest/)
* [NumPy](https://numpy.org/)

## 📂 Project Structure

```
AI-Virtual-Mouse/
│
├── hand_Module.py        # Custom hand detection module using MediaPipe
├── VirtualMouse.py       # Main script to run virtual mouse
├── README.md             # Project documentation
└── requirements.txt      # Python dependencies
```

## 🧠 How It Works

1. Captures video from your webcam.
2. Detects and tracks your hand using MediaPipe.
3. Identifies key landmarks on your fingers.
4. Converts index finger position to mouse pointer movement.
5. Detects pinch gestures to simulate mouse clicks.

## 🖥️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/RandomRohit-hub/Ai-virtual-Mouse.git
cd Ai-virtual-Mouse
```

### 2. Create virtual environment (optional but recommended)

```bash
python -m venv venv
source venv/bin/activate  # On Windows use venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the script

```bash
python VirtualMouse.py
```

> Ensure your webcam is functional.

## 👋 Hand Gesture Controls

| Gesture                             | Action             |
| ----------------------------------- | ------------------ |
| Index finger up                     | Move mouse pointer |
| Index + Middle fingers up (pinch)   | Left Click         |
| Thumb + Index finger close together | Right Click        |

> More gestures can be added in `VirtualMouse.py`.

## ❗ Troubleshooting

* Webcam not opening? Try changing the `cv2.VideoCapture(0)` to `cv2.VideoCapture(1)` if you have multiple cameras.
* Slow response? Close background applications and lower webcam resolution.

## 📄 License

This project is licensed under the [MIT License](LICENSE).

## 🙌 Acknowledgements

* [MediaPipe Hands](https://google.github.io/mediapipe/solutions/hands.html) by Google
* [PyAutoGUI](https://pyautogui.readthedocs.io/) for mouse automation


