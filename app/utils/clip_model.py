import torch
import clip
from PIL import Image

# model (ViT-B/32)
DEVICE = "cuda" if torch.cuda.is_available() else "cpu"
MODEL, PREPROCESS = clip.load("ViT-B/32", device=DEVICE)

def get_image_embedding(filepath: str):
    image = PREPROCESS(Image.open(filepath)).unsqueeze(0).to(DEVICE)
    with torch.no_grad():
        image_features = MODEL.encode_image(image)
        image_features /= image_features.norm(dim=-1, keepdim=True)
    return image_features.cpu().numpy().astype("float32")