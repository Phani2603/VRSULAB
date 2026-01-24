import cv2
import matplotlib.pyplot as plt

# Read the image as a color image (BGR format by default)
img_bgr = cv2.imread("/content/Common_Grackle-Ronald_Zigler-BS-FI-1280x960.webp")

# Convert BGR to LAB
img_lab = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2LAB)

# Split LAB channels
L, A, B = cv2.split(img_lab)

# Convert LAB back to RGB for display (or for further use)
img_rgb_from_lab = cv2.cvtColor(img_lab, cv2.COLOR_LAB2RGB)

# Convert original BGR to RGB for matplotlib display
img_rgb_original = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)

plt.figure(figsize=(15, 10)) # Adjust figure size for more subplots

# Plot original image
plt.subplot(1, 2, 1)
plt.title("Original Image (RGB)")
plt.imshow(img_rgb_original)
plt.axis("off")

# # Plot L channel
# plt.subplot(2, 3, 2)
# plt.title("LAB - L Channel")
# plt.imshow(L, cmap="gray") # L channel is grayscale
# plt.axis("off")

# # Plot A channel
# plt.subplot(2, 3, 3)
# plt.title("LAB - A Channel")
# plt.imshow(A, cmap="RdYlGn") # A channel represents green-red values
# plt.axis("off")

# # Plot B channel
# plt.subplot(2, 3, 4)
# plt.title("LAB - B Channel")
# plt.imshow(B, cmap="YlGnBu") # B channel represents blue-yellow values
# plt.axis("off")

# Plot the image converted from LAB back to RGB
plt.subplot(1, 2, 2)
plt.title("LAB to RGB")
plt.imshow(img_rgb_from_lab)
plt.axis("off")

plt.tight_layout()
plt.show()
