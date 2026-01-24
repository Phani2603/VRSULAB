import cv2
import matplotlib.pyplot as plt

img = cv2.imread("/content/6a91b53f05b6af2182fd7ef75e92e128.webp",0)
clahe=cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
clahe_img=clahe.apply(img)

plt.figure(figsize=(12,5))

plt.subplot(1,3,1)
plt.title("Original Image")
plt.imshow(img, cmap="grey")
plt.axis("off")

plt.subplot(1,3,2)
plt.title("CLAHE Equalized")
plt.imshow(clahe_img, cmap="grey")
plt.axis("off")

plt.subplot(1,3,3)
plt.title("CLAHE")
plt.hist(clahe_img.ravel(), bins=256)
plt.show()