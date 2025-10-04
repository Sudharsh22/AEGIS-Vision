# ⚡ AEGIS VISION ⚡

**Smart Safety Equipment Detection (TorchScript, YOLOv8)**

Welcome to **AEGIS VISION** – a lightweight, browser-ready safety equipment detection app powered by **YOLOv8**.
This project was built for **real-time workplace safety monitoring**, capable of detecting equipment like fire extinguishers, nitrogen tanks, and more.

---

## 🚀 Live Demo

Try it here: [AEGIS Vision on Hugging Face Spaces](https://huggingface.co/spaces/sudharssh22/AEGIS-Vision)

Upload an image → Adjust the confidence threshold → Detect safety equipment instantly!

---

## 🔍 Features

* ✅ Runs **YOLOv8 TorchScript** for safe deployment (no pickle files).
* ✅ Detects multiple safety equipment classes.
* ✅ Futuristic neon-styled Gradio UI.
* ✅ Works entirely in the browser – no installation needed.

---

## 🛠️ How It Works

1. **Model Training**

   * YOLOv8 trained on a custom dataset of safety equipment.
   * Exported to **TorchScript** (`best.torchscript`) for Hugging Face deployment.

2. **Inference**

   * Input images resized to 640×640.
   * Model returns bounding boxes + class labels + confidence scores.
   * Results drawn on the image in real time.

3. **UI/UX**

   * Built with **Gradio Blocks**.
   * Includes a **futuristic black + neon mesh theme** ✨.

---

## 📂 Project Structure

```
├── app.py              # Gradio interface + inference code  
├── best.torchscript    # TorchScript YOLOv8 model  
├── requirements.txt    # Python dependencies  
└── README.md           # Project documentation (this file)  
```

---

## 📦 Installation & Usage

Clone the repo and run locally:

```bash
# Clone the repo
git clone https://github.com/Sudharsh22/AEGIS-Vision.git
cd AEGIS-Vision

# Install dependencies
pip install -r requirements.txt

# Run the Gradio app
python app.py
```

---

## 📦 Requirements

Dependencies are minimal:

```
gradio
ultralytics
torch
opencv-python-headless
numpy
```

---

## 🎯 Example Detections

* 🧯 Fire Extinguisher
* 🛢️ Nitrogen Tank
* 🦺 Safety Vest
* (Extend with more classes as needed…)

---

## 🌟 Credits

* **YOLOv8** by [Ultralytics](https://github.com/ultralytics/ultralytics)
* **Gradio** for interactive UI
* **Hugging Face** for hosting the demo

💡 *This project was developed as part of a hackathon to showcase how AI can enhance workplace safety.*
