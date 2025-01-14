import cv2
import numpy as np

def global_thresholding(src):
    gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)  
    otsu_thresh, dst = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    print(f"Threshold used by Otsu's method: {otsu_thresh}")
    return dst

def histogram_equalization(src):
    if src.shape[2] == 3:  
        b, g, r = cv2.split(src)
        b = cv2.equalizeHist(b)
        g = cv2.equalizeHist(g)
        r = cv2.equalizeHist(r)
        return cv2.merge((b, g, r))
    else:
        return cv2.equalizeHist(src)

def plot_histogram(image):
    bgr_planes = cv2.split(image)
    hist_size = 256
    hist_range = [0, 256]

    b_hist = cv2.calcHist([bgr_planes[0]], [0], None, [hist_size], hist_range)
    g_hist = cv2.calcHist([bgr_planes[1]], [0], None, [hist_size], hist_range)
    r_hist = cv2.calcHist([bgr_planes[2]], [0], None, [hist_size], hist_range)

    hist_w, hist_h = 512, 400
    bin_w = int(np.round(hist_w / hist_size))
    hist_image = np.zeros((hist_h, hist_w, 3), dtype=np.uint8)

    cv2.normalize(b_hist, b_hist, 0, hist_image.shape[0], cv2.NORM_MINMAX)
    cv2.normalize(g_hist, g_hist, 0, hist_image.shape[0], cv2.NORM_MINMAX)
    cv2.normalize(r_hist, r_hist, 0, hist_image.shape[0], cv2.NORM_MINMAX)

    for i in range(1, hist_size):
        cv2.line(hist_image, (bin_w * (i - 1), hist_h - int(b_hist[i - 1])),
                 (bin_w * i, hist_h - int(b_hist[i])),
                 (255, 0, 0), 2, 8, 0)
        cv2.line(hist_image, (bin_w * (i - 1), hist_h - int(g_hist[i - 1])),
                 (bin_w * i, hist_h - int(g_hist[i])),
                 (0, 255, 0), 2, 8, 0)
        cv2.line(hist_image, (bin_w * (i - 1), hist_h - int(r_hist[i - 1])),
                 (bin_w * i, hist_h - int(r_hist[i])),
                 (0, 0, 255), 2, 8, 0)

    cv2.imshow("Histogram", hist_image)

def main():
    src = cv2.imread("/Users/didu/Desktop/proiect pi/imagini/images.jpeg")
    if src is None:
        print("Could not open or find the image")
        return

    binarized = global_thresholding(src)
    histogram_equalized = histogram_equalization(src)

    cv2.imshow("Original", src)
    cv2.imshow("Binarized", binarized)
    cv2.imshow("Histogram Equalized", histogram_equalized)
    plot_histogram(src)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
