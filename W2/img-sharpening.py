import cv2
import matplotlib.pyplot as plt
import numpy as np
# Load image in grayscale
img = cv2.imread("/content/340cbeb8-23fa-4a58-89fd-c3a7a3debcbf.jpg", 0)
# Sharpening kernel (simple 3x3 filter)
kernel = np.array([[0, -1, 0],
[-1, 5, -1],
[0, -1, 0]])

sharpened = cv2.filter2D(img, -1, kernel)
# Show original and sharpened images
plt.figure(figsize=(10,5))
plt.subplot(1,2,1)
plt.imshow(img, cmap='gray' )
plt.title("Original Image")
plt.axis( 'off')
plt.subplot(1,2,2)
plt.imshow(sharpened, cmap='gray' )
plt.title("Sharpened Image")
plt.axis( 'off')
plt. show()

