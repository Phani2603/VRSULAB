# LAB EXP 1 --   IMAGE ENHANCEMENT
# POINT PROCESSING
# HISTOGRAM EQUALIZATION
import cv2
import matplotlib.pyplot as plt

img = cv2.imread("/content/VWMIm0mZC4U3tajmmSropd3fbJHaFWugK5fhO5E3ySQ.webp", 0)

he_img=cv2.equalizeHist(img)

plt.figure(figsize=(12,5))

plt.subplot(1,3,1)
plt.title("Original Image")
plt.imshow(img, cmap="gray")
plt.axis("off")

plt.subplot(1,3,2)
plt.title("Histogram Equalized")
plt.imshow(he_img, cmap="gray")
plt.axis("off")

plt.subplot(1,3,3)
plt.title("Histogram")
plt.hist(img.ravel(), bins=256)
plt.show()
