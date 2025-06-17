import gradio as gr
from PIL import Image

def is_ai_image(image: Image.Image):
    return "這是一張 AI 生成圖片（模擬結果）"

gr.Interface(fn=is_ai_image, inputs="image", outputs="text").launch()
