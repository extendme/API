import gradio as gr
from PIL import Image
import numpy as np

# 模擬圖片判斷邏輯
def is_ai_image(image: Image.Image):
    if image is None:
        return "請上傳圖片"
    # TODO: 在這裡接入圖片模型
    return "這是一張 AI 生成圖片（模擬）"

# 模擬語音判斷邏輯
def is_ai_voice(audio):
    if audio is None:
        return "請上傳語音"
    # audio = (sample_rate, np.array)
    # TODO: 在這裡接入語音模型
    return "這是一段 AI 生成語音（模擬）"

# Gradio 分頁介面（Tabs）
with gr.Blocks(title="AI 真假判斷系統") as demo:
    gr.Markdown("## AI 圖片與語音鑑別系統")
    with gr.Tab("image_checker"):
        img_input = gr.Image(type="pil", label="上傳圖片")
        img_output = gr.Text(label="判斷結果")
        img_button = gr.Button("辨識圖片")
        img_button.click(fn=is_ai_image, inputs=img_input, outputs=img_output)

    with gr.Tab("audio_checker"):
        audio_input = gr.Audio(type="numpy", label="上傳語音（wav/mp3）")
        audio_output = gr.Text(label="判斷結果")
        audio_button = gr.Button("辨識語音")
        audio_button.click(fn=is_ai_voice, inputs=audio_input, outputs=audio_output)

demo.launch()
