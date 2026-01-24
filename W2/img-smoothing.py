# Spatial Domain Filtering - Smoothing

import cv2
import matplotlib.pyplot as plt


# Load 3 different images

img_avg = cv2.imread("/content/sample_data/average blur ex. jpg")
img_gauss = cv2.imread("/content/sample_data/guassian blur.webp")
img_median = cv2.imread("/content/sample_data/median blur eg.png")

# Check loading
if img_avg is None or img_gauss is None or img_median is None:
  print("Error: One or more images not found. Check file paths!")
  exit()
# Convert BGR > RGB for correct display
img_avg_rgb = cv2.cvtColor(img_avg, cv2.COLOR_BGR2RGB)
img_gauss_rgb = cv2.cvtColor(img_gauss, cv2.COLOR_BGR2RGB)
img_median_rgb = cv2.cvtColor(img_median, cv2.COLOR_BGR2RGB)


# Convert BGR > RGB for correct display
img_avg_rgb = cv2.cvtColor(img_avg, cv2.COLOR_BGR2RGB)
img_gauss_rgb = cv2.cvtColor(img_gauss, cv2.COLOR_BGR2RGB)
img_median_rgb = cv2.cvtColor(img_median, cv2.COLOR_BGR2RGB)
#

# Apply filters
#
# 1. Average Smoothing
avg_blur = cv2.blur(img_avg, (5, 5))
avg_blur_rgb = cv2.cvtColor(avg_blur, cv2.COLOR_BGR2RGB)
# 2. Gaussian Smoothing
gaussian_blur = cv2.GaussianBlur(img_gauss, (5, 5), 0)
gaussian_blur_rgb = cv2.cvtColor(gaussian_blur, cv2.COLOR_BGR2RGB)
# 3. Median Smoothing
median_blur = cv2.medianBlur(img_median, 5)
median_blur_rgb = cv2.cvtColor(median_blur, cv2.COLOR_BGR2RGB)

# Display Before and After for each filter
#

plt.figure(figsize=(14, 10))
#
plt.subplot(3, 2, 1)

plt.figure(figsize=(14, 10))
#
plt.subplot(3, 2, 1)
plt.imshow(img_avg_rgb)
plt.title("Original Image (Average Blur)")
plt.axis('off')
plt.subplot(3, 2, 2)
plt.imshow(avg_blur_rgb)
plt.title("After Average Blur")
plt.axis('off')
#
plt.subplot(3, 2, 3)
plt.imshow(img_gauss_rgb)
plt.title("Original Image (Gaussian Blur)")
plt.axis('off')
plt.subplot(3, 2, 4)
plt.imshow(gaussian_blur_rgb)
plt.title("After Gaussian Blur")
plt.axis('off')
# ----- Median Blur
plt.subplot(3, 2, 5)
plt.imshow(img_median_rgb)
#

plt.title("Original Image (Gaussian Blur)")
plt.axis('off')
plt.subplot(3, 2, 4)
plt.imshow(gaussian_blur_rgb)
plt.title("After Gaussian Blur")
plt.axis('off')
# Median Blur
plt.subplot(3, 2, 5)
plt.imshow(img_median_rgb)
plt.title("Original Image (Median Blur)")
plt.axis('off')
plt.subplot(3, 2, 6)
plt.imshow(median_blur_rgb)
plt.title("After Median Blur")
plt.axis('off')
plt.tight_layout()
plt. show()