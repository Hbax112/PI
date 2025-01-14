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

# Frequency Domain Filters
# Low-Pass Filter (Ideal)
def ideal_low_pass_filter_frequency(image, radius=30):
    rows, cols = image.shape
    crow, ccol = rows // 2, cols // 2

    mask = np.zeros((rows, cols), np.uint8)
    cv2.circle(mask, (ccol, crow), radius, 1, thickness=-1)

    dft = np.fft.fft2(image)
    dft_shift = np.fft.fftshift(dft)

    dft_filtered = dft_shift * mask
    dft_ishift = np.fft.ifftshift(dft_filtered)
    filtered_image = np.fft.ifft2(dft_ishift)
    filtered_image = np.abs(filtered_image)

    return filtered_image

# Low-Pass Filter (Gaussian)
def gaussian_low_pass_filter_frequency(image, sigma=10):
    rows, cols = image.shape
    crow, ccol = rows // 2, cols // 2

    x = np.arange(-ccol, ccol)
    y = np.arange(-crow, crow)
    x, y = np.meshgrid(x, y)

    gaussian_kernel = np.exp(-(x**2 + y**2) / (2 * sigma**2))

    dft = np.fft.fft2(image)
    dft_shift = np.fft.fftshift(dft)

    dft_filtered = dft_shift * gaussian_kernel
    dft_ishift = np.fft.ifftshift(dft_filtered)
    filtered_image = np.fft.ifft2(dft_ishift)
    filtered_image = np.abs(filtered_image)

    return filtered_image

# High-Pass Filter (Ideal)
def ideal_high_pass_filter_frequency(image, radius=30):
    rows, cols = image.shape
    crow, ccol = rows // 2, cols // 2

    mask = np.ones((rows, cols), np.uint8)
    cv2.circle(mask, (ccol, crow), radius, 0, thickness=-1)

    dft = np.fft.fft2(image)
    dft_shift = np.fft.fftshift(dft)

    dft_filtered = dft_shift * mask
    dft_ishift = np.fft.ifftshift(dft_filtered)
    filtered_image = np.fft.ifft2(dft_ishift)
    filtered_image = np.abs(filtered_image)

    return filtered_image

# High-Pass Filter (Gaussian)
def gaussian_high_pass_filter_frequency(image, sigma=10):
    rows, cols = image.shape
    crow, ccol = rows // 2, cols // 2

    x = np.arange(-ccol, ccol)
    y = np.arange(-crow, crow)
    x, y = np.meshgrid(x, y)

    gaussian_kernel = 1 - np.exp(-(x**2 + y**2) / (2 * sigma**2))

    dft = np.fft.fft2(image)
    dft_shift = np.fft.fftshift(dft)

    dft_filtered = dft_shift * gaussian_kernel
    dft_ishift = np.fft.ifftshift(dft_filtered)
    filtered_image = np.fft.ifft2(dft_ishift)
    filtered_image = np.abs(filtered_image)

    return filtered_image

low_pass_ideal = ideal_low_pass_filter_frequency(image, radius=30)
display_images(image, low_pass_ideal, title_filtered="Frequency Domain Ideal Low-Pass")

gaussian_low_pass = gaussian_low_pass_filter_frequency(image, sigma=10)
display_images(image, gaussian_low_pass, title_filtered="Frequency Domain Gaussian Low-Pass")

high_pass_ideal = ideal_high_pass_filter_frequency(image, radius=30)
display_images(image, high_pass_ideal, title_filtered="Frequency Domain Ideal High-Pass")

gaussian_high_pass = gaussian_high_pass_filter_frequency(image, sigma=10)
display_images(image, gaussian_high_pass, title_filtered="Frequency Domain Gaussian High-Pass")
