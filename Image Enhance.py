# -*- coding: utf-8 -*-
"""
Created on Thu Dec 29 10:20:57 2022

@author: 114
"""

from PIL import Image
from PIL import ImageEnhance
import matplotlib.pyplot as plt

image = Image.open(r"C:\Users\114\Downloads\Sharp_bari1Size 181 x 1220 mmType Matt Surface Floor (By FloorMonk).jpg")
plt.figure()
plt.imshow(image);plt.title('Before')

enh_bri = ImageEnhance.Brightness(image)
brightness = 1.0
image_brightened = enh_bri.enhance(brightness)
plt.figure()
plt.imshow(image_brightened)

enh_col = ImageEnhance.Color(image_brightened)
color = 1.0
image_colored = enh_col.enhance(color)
plt.figure()
plt.imshow(image_colored)

enh_con = ImageEnhance.Contrast(image_colored)
contrast = 1.5
image_contrasted = enh_con.enhance(contrast)
plt.figure()
plt.imshow(image_contrasted)

enh_sha = ImageEnhance.Sharpness(image_contrasted)
sharpness = 2.0
image_sharped = enh_sha.enhance(sharpness)
plt.figure()
plt.imshow(image_sharped);plt.title('After');plt.axis('off')