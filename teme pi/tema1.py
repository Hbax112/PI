import cv2
import numpy as np

def apply_multi_thresholding(image_path):
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    if img is None:
        print("Nu am putut deschide sau găsi imaginea")
        return

    img_float = img.astype(np.float32) / 255.0

    samples = img_float.reshape((-1, 1))

    K = 3
    labels = np.zeros(samples.shape[0], dtype=np.int32)
    centers = np.zeros((K, 1), dtype=np.float32)

    _, labels, centers = cv2.kmeans(samples, K, None, 
                                     (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_COUNT, 100, 1.0), 
                                     10, cv2.KMEANS_PP_CENTERS)

    segmented_img = centers[labels.flatten()]
    segmented_img = segmented_img.reshape(img.shape)
    segmented_img = (segmented_img * 255).astype(np.uint8)

    print("Valorile pragurilor (maximelor) obținute:")
    for center in centers.flatten():
        print(center * 255.0)

    cv2.imshow("Imaginea dupa aplicarea pragurilor multiple", segmented_img)

def floyd_steinberg_dithering(src):
    for y in range(src.shape[0] - 1):
        for x in range(1, src.shape[1] - 1):
            old_pixel = src[y, x]
            new_pixel = 255 if old_pixel > 127 else 0
            src[y, x] = new_pixel
            error = old_pixel - new_pixel
            
            src[y, x + 1] = np.clip(src[y, x + 1] + error * 7 / 16, 0, 255)
            src[y + 1, x - 1] = np.clip(src[y + 1, x - 1] + error * 3 / 16, 0, 255)
            src[y + 1, x] = np.clip(src[y + 1, x] + error * 5 / 16, 0, 255)
            src[y + 1, x + 1] = np.clip(src[y + 1, x + 1] + error * 1 / 16, 0, 255)

if __name__ == "__main__":
    image_path = "/Users/didu/Desktop/proiect pi/imagini/images.jpeg"
    image = cv2.imread(image_path)
    if image is None:
        print("Could not open or find the image")
        exit(-1)

    apply_multi_thresholding(image_path)

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    dithered_image = gray.copy()
    floyd_steinberg_dithering(dithered_image)
    cv2.imshow("Floyd-Steinberg Dithering", dithered_image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
