import gradio as gr

# 假裝的語音分析邏輯（你之後可換成自己的模型）
def is_ai_voice(audio):
    # audio = (sample_rate, numpy array)
    return "這是 AI 生成語音（模擬）"

gr.Interface(
    fn=is_ai_voice,
    inputs=gr.Audio(type="numpy", label="上傳語音檔（wav/mp3）"),
    outputs=gr.Text(label="判斷結果"),
    title="AI 語音鑑別系統",
    description="上傳一段語音，我們將嘗試判斷是否為 AI 生成"
).launch()
