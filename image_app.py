# image_app.py
import torch
from torchvision import models, transforms
from PIL import Image

# 初始化全域變數
model = None
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# 圖像轉換（需與訓練時一致）
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
])

def load_model():
    global model
    if model is None:
        model = models.resnet18(pretrained=False)
        model.fc = torch.nn.Linear(model.fc.in_features, 2)
        model.load_state_dict(torch.load("resnet_ai_detector.pth", map_location=device))
        model.eval().to(device)
        print("✅ 圖片模型已載入")

def is_ai_image(image: Image.Image) -> str:
    if image is None:
        return "請上傳圖片"

    load_model()  # 確保模型已經載入
    input_tensor = transform(image).unsqueeze(0).to(device)

    with torch.no_grad():
        output = model(input_tensor)
        _, pred = torch.max(output, 1)

    class_names = ["real", "fake"]
    return f"這是一張 {class_names[pred.item()].upper()} 圖片"
