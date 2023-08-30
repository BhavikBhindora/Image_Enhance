#Import libraries
from PIL import Image
from PIL import ImageEnhance
import matplotlib.pyplot as plt

#Read the Image
image = Image.open(r"Path/To/Your/Image")
plt.figure()
plt.imshow(image);plt.title('Before')

#Brightness
enh_bri = ImageEnhance.Brightness(image)
brightness = 1.0
image_brightened = enh_bri.enhance(brightness)
plt.figure()
plt.imshow(image_brightened)

#Color Enhance
enh_col = ImageEnhance.Color(image_brightened)
color = 1.0
image_colored = enh_col.enhance(color)
plt.figure()
plt.imshow(image_colored)

#Contrast
enh_con = ImageEnhance.Contrast(image_colored)
contrast = 1.5
image_contrasted = enh_con.enhance(contrast)
plt.figure()
plt.imshow(image_contrasted)

#Sharpness
enh_sha = ImageEnhance.Sharpness(image_contrasted)
sharpness = 2.0
image_sharped = enh_sha.enhance(sharpness)

#Plot final image
plt.figure()
plt.imshow(image_sharped);plt.title('After');plt.axis('off')
