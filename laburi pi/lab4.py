import cv2
import numpy as np
import matplotlib.pyplot as plt

def display_images(original, filtered, title_original="Original", title_filtered="Filtered"):
    plt.figure(figsize=(10, 5))

    plt.subplot(1, 2, 1)
    plt.title(title_original)
    plt.imshow(original, cmap='gray')
    plt.axis('off')

    plt.subplot(1, 2, 2)
    plt.title(title_filtered)
    plt.imshow(filtered, cmap='gray')
    plt.axis('off')

    plt.show()

image = cv2.imread("/Users/didu/Desktop/proiect pi/imagini/images.jpeg", cv2.IMREAD_GRAYSCALE)

if image is None:
    raise FileNotFoundError("Image file not found. Please provide a valid path.")

# Low-Pass Filters
# Gaussian Blur
kernel_size = 5
gaussian_blur = cv2.GaussianBlur(image, (kernel_size, kernel_size), 0)
display_images(image, gaussian_blur, title_filtered="Gaussian Blur")

# Arithmetic Mean Filter
kernel_mean = np.ones((3, 3), np.float32) / 9
mean_filter = cv2.filter2D(image, -1, kernel_mean)
display_images(image, mean_filter, title_filtered="Arithmetic Mean Filter")

# High-Pass Filters
# Laplacian Filter
laplacian = cv2.Laplacian(image, cv2.CV_64F)
laplacian = np.uint8(np.absolute(laplacian))
display_images(image, laplacian, title_filtered="Laplacian Filter")

# High-Pass Filter (Custom Kernel from Slide 10, Relation 4)
high_pass_kernel = np.array([[0, -1, 0],
                             [-1, 5, -1],
                             [0, -1, 0]], dtype=np.float32)
high_pass_filter = cv2.filter2D(image, -1, high_pass_kernel)
display_images(image, high_pass_filter, title_filtered="High-Pass Filter (3x3)")