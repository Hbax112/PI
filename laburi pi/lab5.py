import cv2
import numpy as np
import time
from matplotlib import pyplot as plt

image = cv2.imread("/Users/didu/Desktop/proiect pi/imagini/poza.jpeg")

def apply_gaussian_filter(image, kernel_size, sigma):
    start_time = time.time()
    gaussian_filtered = cv2.GaussianBlur(image, (kernel_size, kernel_size), sigma)
    elapsed_time = time.time() - start_time
    return gaussian_filtered, elapsed_time

def apply_2d_filter(image, kernel):
    start_time = time.time()
    filtered_image = cv2.filter2D(image, -1, kernel)
    elapsed_time = time.time() - start_time
    return filtered_image, elapsed_time

# param pt filtru Gaussian 
gaussian_kernel_size = 5  
sigma = 1.0               

#2D kernel
custom_kernel = np.array([[0, -1, 0],
                          [-1, 4, -1],
                          [0, -1, 0]], dtype=np.float32)

# aplicare filtru Gaussian 
gaussian_result, gaussian_time = apply_gaussian_filter(image, gaussian_kernel_size, sigma)

# aplicare filtru 2D 
custom_result, custom_time = apply_2d_filter(image, custom_kernel)

# rezultate
plt.figure(figsize=(12, 6))


plt.subplot(1, 3, 1)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title('Imaginea originală')

plt.subplot(1, 3, 2)
plt.title(f"Gaussian Filter\nProcessing Time: {gaussian_time:.4f}s")
plt.imshow(gaussian_result, cmap='gray')

plt.subplot(1, 3, 3)
plt.title(f"2D Filter\nProcessing Time: {custom_time:.4f}s")
plt.imshow(custom_result, cmap='gray')

plt.tight_layout()
plt.show()
