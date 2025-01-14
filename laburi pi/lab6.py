import numpy as np
from collections import deque
import matplotlib.pyplot as plt
import random


def bfs_labeling(binary_image):
    rows, cols = binary_image.shape
    labels = np.zeros_like(binary_image, dtype=int)
    label = 1

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for r in range(rows):
        for c in range(cols):
            if binary_image[r, c] == 0 and labels[r, c] == 0:
                queue = deque([(r, c)])
                labels[r, c] = label

                while queue:
                    cr, cc = queue.popleft()
                    for dr, dc in directions:
                        nr, nc = cr + dr, cc + dc
                        if 0 <= nr < rows and 0 <= nc < cols:
                            if binary_image[nr, nc] == 0 and labels[nr, nc] == 0:
                                labels[nr, nc] = label
                                queue.append((nr, nc))

                label += 1

    return labels


def two_pass_labeling(binary_image):
    rows, cols = binary_image.shape
    labels = np.zeros_like(binary_image, dtype=int)
    equivalences = {}
    label = 1

    for r in range(rows):
        for c in range(cols):
            if binary_image[r, c] == 0:
                neighbors = []
                if r > 0 and labels[r - 1, c] > 0:
                    neighbors.append(labels[r - 1, c])
                if c > 0 and labels[r, c - 1] > 0:
                    neighbors.append(labels[r, c - 1])

                if not neighbors:
                    labels[r, c] = label
                    equivalences[label] = {label}
                    label += 1
                else:
                    min_label = min(neighbors)
                    labels[r, c] = min_label
                    for lbl in neighbors:
                        equivalences[min_label].update(equivalences[lbl])
                        equivalences[lbl] = equivalences[min_label]

    representative = {}
    for lbl, eq_set in equivalences.items():
        rep = min(eq_set)
        for eq_lbl in eq_set:
            representative[eq_lbl] = rep

    for r in range(rows):
        for c in range(cols):
            if labels[r, c] > 0:
                labels[r, c] = representative[labels[r, c]]

    return labels


def colorize_labels(labels):
    rows, cols = labels.shape
    unique_labels = np.unique(labels)
    colors = {label: (random.random(), random.random(), random.random()) for label in unique_labels if label != 0}
    color_image = np.ones((rows, cols, 3))

    for r in range(rows):
        for c in range(cols):
            if labels[r, c] > 0:
                color_image[r, c] = colors[labels[r, c]]

    return color_image


if __name__ == "__main__":
    binary_image = np.array([
        [1, 0, 0, 1, 0, 1],
        [1, 0, 0, 1, 0, 0],
        [1, 0, 0, 1, 0, 1],
        [1, 0, 1, 1, 0, 0],
        [1, 0, 1, 0, 0, 1],
        [1, 1, 1, 0, 0, 0]
    ])

    print("Imaginea binară:")
    print(binary_image)

    print("\nEtichetare BFS:")
    bfs_labels = bfs_labeling(binary_image)
    print(bfs_labels)

    print("\nEtichetare cu două treceri:")
    two_pass_labels = two_pass_labeling(binary_image)
    print(two_pass_labels)

    bfs_colored = colorize_labels(bfs_labels)
    two_pass_colored = colorize_labels(two_pass_labels)

    plt.figure(figsize=(12, 6))

    plt.subplot(1, 3, 1)
    plt.title("Imagine binară")
    plt.imshow(binary_image, cmap='gray')

    plt.subplot(1, 3, 2)
    plt.title("Etichetare BFS")
    plt.imshow(bfs_colored)

    plt.subplot(1, 3, 3)
    plt.title("Etichetare 2 treceri")
    plt.imshow(two_pass_colored)

    plt.show()

