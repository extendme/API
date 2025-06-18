# ai_checker.py
import gradio as gr
from ai_detector_func import predict_image

# 語音部分模擬函式（你之後可整合語音模型）
def is_ai_voice(audio):
    if audio is None:
        return "請上傳語音"
    return "這是一段 AI 生成語音（模擬）"

# Gradio 分頁介面
with gr.Blocks(title="AI 真假判斷系統") as demo:
    gr.Markdown("## AI 圖片與語音鑑別系統")
    
    with gr.Tab("image_checker"):
        img_input = gr.Image(type="pil", label="上傳圖片")
        img_output = gr.Text(label="判斷結果")
        img_button = gr.Button("辨識圖片")
        img_button.click(fn=predict_image, inputs=img_input, outputs=img_output)

    with gr.Tab("audio_checker"):
        audio_input = gr.Audio(type="numpy", label="上傳語音（wav/mp3）")
        audio_output = gr.Text(label="判斷結果")
        audio_button = gr.Button("辨識語音")
        audio_button.click(fn=is_ai_voice, inputs=audio_input, outputs=audio_output)

demo.launch()
