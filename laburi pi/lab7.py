import cv2
import numpy as np

def compute_gradient_magnitude(img):

    grad_x = cv2.Sobel(img, cv2.CV_32F, 1, 0, ksize=3)
    grad_y = cv2.Sobel(img, cv2.CV_32F, 0, 1, ksize=3)

    magnitude = cv2.magnitude(grad_x, grad_y)


    return magnitude


def adaptive_threshold_edge_detection(magnitude, window_size=15, C=0):
  
    mag_8u = cv2.normalize(magnitude, None, 0, 255, cv2.NORM_MINMAX).astype(np.uint8)


    bin_adaptive = cv2.adaptiveThreshold(
        mag_8u, 255,
        cv2.ADAPTIVE_THRESH_MEAN_C,  
        cv2.THRESH_BINARY,
        window_size,
        C
    )
    
    return bin_adaptive


def hysteresis_thresholding(magnitude, edge_map, low_ratio=0.5, high_ratio=0.2):

    mag_8u = cv2.normalize(magnitude, None, 0, 255, cv2.NORM_MINMAX)
    
    max_val = mag_8u.max()
    high_thresh = max_val * high_ratio
    low_thresh = high_thresh * low_ratio
    
    mag_8u = mag_8u.astype(np.float32)
    
    result = np.zeros_like(mag_8u, dtype=np.uint8)
    
    strong_i, strong_j = np.where(mag_8u > high_thresh)
    result[strong_i, strong_j] = 255

    weak_i, weak_j = np.where((mag_8u <= high_thresh) & (mag_8u >= low_thresh))
    

    
    to_visit = list(zip(strong_i, strong_j))
    
    neighbors = [(-1, -1), (-1, 0), (-1, 1),
                 ( 0, -1),           ( 0, 1),
                 ( 1, -1), ( 1, 0), ( 1, 1)]
    
    weak_set = set(zip(weak_i, weak_j))  

    while to_visit:
        x, y = to_visit.pop()
        
        for dx, dy in neighbors:
            nx, ny = x + dx, y + dy
            if 0 <= nx < mag_8u.shape[0] and 0 <= ny < mag_8u.shape[1]:
                if (nx, ny) in weak_set:
                    result[nx, ny] = 255
                    weak_set.remove((nx, ny))
                    to_visit.append((nx, ny))
    

    return result


def main():
    img = cv2.imread('/Users/didu/Desktop/proiect pi/imagini/soldat.jpg', cv2.IMREAD_GRAYSCALE)
    if img is None:
        print("Eroare la încărcarea imaginii!")
        return

    img_blur = cv2.GaussianBlur(img, (3,3), 0)
    
    magnitude = compute_gradient_magnitude(img_blur)
    
    edge_map_adaptive = adaptive_threshold_edge_detection(magnitude, window_size=15, C=2)
    
   
    edges_final = hysteresis_thresholding(magnitude, edge_map_adaptive, 
                                          low_ratio=0.5, 
                                          high_ratio=0.2)
    
    cv2.imshow("Input", img)
    cv2.imshow("Adaptive Edge Map", edge_map_adaptive)
    cv2.imshow("Final Edges (Hysteresis)", edges_final)
    cv2.waitKey(0)

    cv2.imwrite("edges_adaptive.jpg", edge_map_adaptive)
    cv2.imwrite("edges_final_hysteresis.jpg", edges_final)

if __name__ == "__main__":
    main()
