import os
from PIL import Image

dir_path = "C:/Users/Pierre/Desktop"
os.chdir(dir_path)

with open('photo2.jpg', 'rb') as f:
   jpg_raw_data = f.read()

jpg_data = .decompress(jpg_raw_data)
print(jpg_data)
