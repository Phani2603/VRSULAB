# Digital Image Processing Laboratory

This repository serves as a comprehensive academic record of computer vision and digital image processing implementations. The curriculum transitions from fundamental pixel-level operations to complex high-level vision tasks, emphasizing both theoretical understanding and practical application using the OpenCV framework.

## Project Methodology

The lab exercises are implemented using Python 3.13, leveraging the `opencv-contrib-python` library for advanced image processing algorithms and `matplotlib` for rigorous data visualization and result analysis. Each module is designed to isolate specific components of the image processing pipeline, from pre-processing and enhancement to segmentation and classification.

## Laboratory Modules

The repository is structured into distinct modules corresponding to key domains in the field:

### W1: Point Processing and Intensity Transformations
This module explores pixel-wise operations where the output at a specific location depends solely on the intensity value at that same location in the input image.

- **histogram_eqlztn.py**: Implements global histogram equalization. This technique enhances the contrast of an image by effectively spreading out the most frequent intensity values, linearizing the cumulative distribution function (CDF) of the image histogram.
- **clahe.py**: Implements Contrast Limited Adaptive Histogram Equalization. Unlike global equalization, CLAHE operates on small regions (tiles) to enhance local contrast while imposing a limit on contrast amplification to prevent the enhancement of background noise.
- **clr_enhncement.py**: Explores color-specific enhancements. This involves transforming images into luminance-chrominance color spaces (such as HSV or LAB) to isolate intensity for enhancement without distorting the original chromaticity of the scene.

### W2: Spatial Filtering and Domain Operations
This module focuses on neighborhood operations where the output pixel value is determined by a weighted sum of pixels in a local neighborhood, typically implemented via convolution.

- **img-smoothing.py**: Covers low-pass filtering techniques. Implementations include Gaussian blurring for noise reduction (using a weighted average defined by a Gaussian distribution) and Median filtering, which is particularly effective at removing salt-and-pepper noise while preserving edges.
- **img-sharpening.py**: Focuses on high-pass filtering and derivative-based operators. This includes the application of Laplacian kernels and unsharp masking to emphasize high-frequency components, thereby enhancing edges and fine structural details.

### W4: Edge Detection and Gradient Analysis
This module addresses the identification of significant local changes in image intensity, which often correspond to physical boundaries of objects.

- **edge-detection.py**: Provides a comparative analysis of gradient-based operators. It includes First-order derivative operators (Sobel, Prewitt) and the Canny Edge Detector, which utilizes a multi-stage algorithm including noise reduction, gradient calculation, non-maximum suppression, and hysteresis thresholding for optimal edge localization.

### W5: Image Segmentation and Morphological Analysis
Segmentation involves partitioning a digital image into multiple segments (sets of pixels) to simplify or change the representation of an image into something more meaningful and easier to analyze.

- **otsus-binarization.py**: Implements Otsu's method for automatic threshold selection. This algorithm iterates through all possible threshold values and calculates a measure of spread for the pixel levels each side of the threshold, aiming to minimize intra-class variance (or maximize inter-class variance).
- **feature-extraction.py**: Focuses on the quantitative description of segmented regions. This involves calculating geometric descriptors such as area, perimeter, circularity, and centroid locations, which are essential for downstream object recognition tasks.

### W6: Computational Intelligence and Deep Learning
The final modules integrate modern machine learning and deep learning paradigms for high-level semantic understanding of visual data.

- **ml-based-od.py**: Demonstrates object detection using classical machine learning pipelines, often involving manual feature extraction (like HOG or Haar cascades) followed by a classifier (like SVM or Adaboost).
- **dl-for-image-classification.py**: Implements deep hierarchical models, specifically Convolutional Neural Networks (CNNs). These models automatically learn spatial hierarchies of features through backpropagation, achieving state-of-the-art performance in complex image classification benchmarks.

## Installation and Execution

### System Requirements
- Python Runtime: Version 3.13 or higher.
- Dependency Management: [uv](https://github.com/astral-sh/uv) is the preferred tool for environment reproducible.

### Setup Instructions
1. Clone the repository to your local environment.
2. Initialize the virtual environment and install all requisite dependencies:
   ```bash
   uv sync
   ```
3. Execute individual laboratory scripts using the Python interpreter within the synchronized environment.

### Core Dependencies
- **OpenCV (contrib-python)**: Primary library for computer vision algorithms.
- **Matplotlib**: Utilized for plotting histograms, intensity profiles, and result comparisons.

---
*Academically structured for the Digital Image Processing (VRSU) Laboratory.*
