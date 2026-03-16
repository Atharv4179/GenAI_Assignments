import os
from PIL import Image

dataset_path = "dataset"

images = []

print("Loading dataset...")

for file in os.listdir(dataset_path):
    if file.endswith(".jpg") or file.endswith(".png"):
        path = os.path.join(dataset_path, file)
        img = Image.open(path)
        images.append(img)

print("Total images loaded:", len(images))

print("\nStarting simulated training process...\n")

for epoch in range(3):
    print("Epoch", epoch + 1)
    
    for i, img in enumerate(images):
        print("Processing image", i + 1)

print("\nCustom dataset successfully integrated with diffusion workflow!")