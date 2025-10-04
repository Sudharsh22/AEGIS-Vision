import gradio as gr
from ultralytics import YOLO

# Load TorchScript model (relative path for Hugging Face)
model = YOLO("best.torchscript")

# Prediction function
def detect_objects(image, conf):
    results = model.predict(image, save=False, conf=conf)
    detected_dict = {}
    for r in results:
        for box in r.boxes:
            cls = int(box.cls[0])
            conf_val = float(box.conf[0])
            label = model.names[cls]
            if label in detected_dict:
                detected_dict[label] = max(detected_dict[label], conf_val)
            else:
                detected_dict[label] = conf_val
    return results[0].plot(), detected_dict

# Futuristic CSS
custom_css = """
body {
    margin: 0;
    padding: 0;
    background: #000;
    font-family: 'Orbitron', sans-serif;
    color: #0ff;
    overflow-y: auto;
}
h1 {
    font-size: 42px;
    text-align: center;
    color: #00eaff;
    text-shadow: 0 0 6px #00eaff, 0 0 12px #ff00ff;
    margin-bottom: 10px;
}
h2 {
    text-align: center;
    font-size: 18px;
    color: #aaa;
    margin-bottom: 30px;
}
.gradio-container {
    border-radius: 12px;
    box-shadow: 0 0 20px rgba(0,255,255,0.3);
    padding: 20px;
    background: rgba(10, 10, 10, 0.85);
    position: relative;
    z-index: 2;
}
#mesh {
    position: fixed;
    top: 0; 
    left: 0;
    width: 100vw;
    height: 100vh;
    z-index: -1;
    background: 
        repeating-linear-gradient(
            to right,
            rgba(0, 255, 255, 0.15) 0px,
            rgba(0, 255, 255, 0.15) 2px,
            transparent 2px,
            transparent 60px
        ),
        repeating-linear-gradient(
            to bottom,
            rgba(255, 0, 255, 0.1) 0px,
            rgba(255, 0, 255, 0.1) 2px,
            transparent 2px,
            transparent 60px
        );
    animation: meshmove 25s linear infinite;
}
@keyframes meshmove {
    from { background-position: 0 0; }
    to { background-position: 400px 400px; }
}
button {
    background: #111;
    color: #0ff !important;
    border: 1px solid #0ff !important;
    box-shadow: 0 0 8px #0ff, 0 0 16px #0ff inset;
    transition: 0.3s;
}
button:hover {
    background: #0ff !important;
    color: #000 !important;
    box-shadow: 0 0 16px #0ff, 0 0 32px #0ff inset;
}
"""

mesh_html = """<div id="mesh"></div>"""

# Gradio Interface
with gr.Blocks(css=custom_css) as demo:
    gr.HTML("<h1>⚡ AEGIS VISION ⚡</h1>")
    gr.HTML("<h2>Smart Safety Equipment Detection (TorchScript)</h2>")
    gr.HTML(mesh_html)

    with gr.Row():
        with gr.Column():
            inp = gr.Image(type="numpy", label="Upload Image")
            conf = gr.Slider(0.2, 0.8, value=0.25, step=0.05, label="Confidence Threshold")
            btn = gr.Button("🚀 Run Detection")
        with gr.Column():
            out_img = gr.Image(type="numpy", label="Detection Result")
            out_label = gr.Label(label="Detected Classes")

    btn.click(fn=detect_objects, inputs=[inp, conf], outputs=[out_img, out_label])

demo.launch()
