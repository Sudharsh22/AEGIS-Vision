# ⚡ AEGIS VISION ⚡

**AI-Enabled Gear Identification System**

Smart Safety Equipment Detection (TorchScript, YOLOv8)

---

Welcome to **AEGIS VISION** – an AI-powered **safety monitoring system** designed to detect essential safety equipment such as fire extinguishers, nitrogen tanks, and more.
The name **AEGIS** stands for **AI-Enabled Gear Identification System**, reflecting its mission to act as a digital shield for workplace safety.

---

## 🚀 Demo

Try it directly here: [AEGIS Vision on Hugging Face Spaces](https://huggingface.co/spaces/your-username/AEGIS-Vision)

Upload an image → Adjust the confidence threshold → Instantly detect safety equipment!

---

## 🔍 Features

* ✅ **TorchScript YOLOv8** for secure, pickle-free deployment.
* ✅ Detects multiple **safety equipment classes**.
* ✅ Futuristic **Gradio UI** with neon styling.
* ✅ **Browser-ready** – no installation needed.

---

## 🛠️ How It Works

1. **Model Training**

   * YOLOv8 trained on custom safety equipment dataset.
   * Exported as `TorchScript` (`best.torchscript`) for Hugging Face deployment.

2. **Inference**

   * Images resized to 640×640.
   * Model outputs bounding boxes, classes, and confidence.
   * Detections rendered on images in real time.

3. **UI/UX**

   * Built with **Gradio Blocks**.
   * Includes futuristic black + neon mesh theme ✨.

---

## 📂 Project Structure

```
├── app.py              # Gradio interface + inference code
├── best.torchscript    # YOLOv8 TorchScript model
├── requirements.txt    # Python dependencies
└── README.md           # Documentation (this file)
```

---

## 📦 Requirements

Your Hugging Face Space automatically installs these dependencies:

```
gradio
ultralytics
torch
opencv-python-headless
numpy
```

---

## 🎯 Example Detections

* Fire Extinguisher 🧯
* Nitrogen Tank 🛢️
* (Add your custom classes here…)

---

## 🌟 Credits

* **Ultralytics YOLOv8** → [GitHub](https://github.com/ultralytics/ultralytics)
* **Gradio** → Interactive browser apps
* **Hugging Face Spaces** → Hosting the demo

---

💡 Developed as part of a hackathon to showcase how **AI can enhance workplace safety** with **AEGIS – AI-Enabled Gear Identification System**.
