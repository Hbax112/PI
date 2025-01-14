import cv2
import numpy as np

def doua_traversari(image_path):
    img_orig = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    _, img = cv2.threshold(img_orig, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

    height, width = img.shape
    labels = np.zeros((height, width), dtype=np.int32)
    label = 0
    equivalence = {}

    for i in range(height):
        for j in range(width):
            if img[i, j] == 0:
                neighbors = []
                if i > 0 and j > 0:
                    neighbors.append(labels[i - 1, j])
                    neighbors.append(labels[i, j - 1])
                else:
                    neighbors.append(0)

                neighbors = [n for n in neighbors if n > 0]
                if not neighbors:
                    label += 1
                    labels[i, j] = label
                    equivalence[label] = label
                else:
                    smallest_label = min(neighbors)
                    labels[i, j] = smallest_label
                    for neighbor in neighbors:
                        if neighbor != smallest_label:
                            equivalence[neighbor] = smallest_label

    for i in range(height):
        for j in range(width):
            if labels[i, j] > 0:
                root_label = labels[i, j]
                while equivalence[root_label] != root_label:
                    root_label = equivalence[root_label]
                labels[i, j] = root_label

    return labels

def visualize_labels(labels):
    min_val, max_val = np.min(labels), np.max(labels)
    colored_labels = (labels.astype(np.float32) - min_val) / (max_val - min_val) * 255
    colored_labels = colored_labels.astype(np.uint8)
    colored_labels_color = cv2.applyColorMap(colored_labels, cv2.COLORMAP_JET)

    cv2.imshow("Labeled Image", colored_labels_color)
    cv2.waitKey(0)

def compute_freeman_chain_code(contour):
    chain_code = []
    directions = [(-1, 0), (-1, 1), (0, 1), (1, 1),
                  (1, 0), (1, -1), (0, -1), (-1, -1)]
    for i in range(len(contour)):
        p1 = contour[i]
        p2 = contour[(i + 1) % len(contour)]
        direction = (p2[0] - p1[0], p2[1] - p1[1])

        for j in range(8):
            if direction == directions[j]:
                chain_code.append(j)
                break
    return chain_code

def print_chain_code(chain_code):
    print(" ".join(map(str, chain_code)))

def trace_contour(labeled_img, target_label):
    directions = [(0, -1), (1, -1), (1, 0), (1, 1),
                  (0, 1), (-1, 1), (-1, 0), (-1, -1)]
    contour = []

    start = (-1, -1)
    for i in range(labeled_img.shape[0]):
        for j in range(labeled_img.shape[1]):
            if labeled_img[i, j] == target_label:
                start = (j, i)
                break
        if start != (-1, -1):
            break

    if start == (-1, -1):
        return contour

    current = start
    dir_index = 0
    while True:
        contour.append(current)

        moved = False
        for i in range(8):
            next_point = (current[0] + directions[dir_index][0], current[1] + directions[dir_index][1])
            if labeled_img[next_point[1], next_point[0]] == target_label:
                contour.append(next_point)
                current = next_point
                dir_index = (dir_index + 7) % 8
                moved = True
                break
            dir_index = (dir_index + 1) % 8
        
        if not moved:
            break

        if current == start:
            break

    return contour

def main():
    image_path = "/Users/didu/Desktop/proiect pi/imagini/tema5.jpeg"
    img = cv2.imread(image_path)
    if img is None:
        print("Image not found or unable to open")
        return

    # Convert to grayscale
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    labels = doua_traversari(image_path)

    # Create binary image
    _, binary_img = cv2.threshold(img_gray, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)
    
    if binary_img is None:
        print("Thresholding failed to create a binary image")
        return

    # Gaussian blur and edge detection
    img_blurred = cv2.GaussianBlur(img_gray, (5, 5), 0)
    edges = cv2.Canny(img_blurred, 50, 150)

    contour = trace_contour(labels, 1)
    chain_code = compute_freeman_chain_code(contour)

    # Find contours
    contours, _ = cv2.findContours(binary_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    img_with_contours = cv2.imread(image_path)
    for cnt in contours:
        polygon = cv2.approxPolyDP(cnt, 5, True)
        cv2.drawContours(img_with_contours, [polygon], -1, (0, 255, 0), 2)

    cv2.imshow("Contours", img_with_contours)
    cv2.waitKey(0)

    print("Contour Chain Code: ", end="")
    print_chain_code(chain_code)
#codu inlantuit pentru fiecare imagine, conturul si asa
if __name__ == "__main__":
    main()
