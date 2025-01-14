import cv2
import numpy as np
from matplotlib import pyplot as plt


def contur_extragere(imagine):
    gri = cv2.cvtColor(imagine, cv2.COLOR_BGR2GRAY)
    blur = cv2.blur(gri, (3, 3))
    kernel = np.ones((5,5),np.uint8)
    gradient = cv2.morphologyEx(blur, cv2.MORPH_GRADIENT, kernel)
    return gradient

def umplere_regiuni(imagine):
    gri = cv2.cvtColor(imagine, cv2.COLOR_BGR2GRAY)

    _, binar = cv2.threshold(gri, 127, 255, cv2.THRESH_BINARY_INV)

    kernel = np.ones((9,9),np.uint8)
    closing = cv2.morphologyEx(binar, cv2.MORPH_CLOSE, kernel)

    return closing

imagine = cv2.imread("/Users/didu/Desktop/proiect pi/poza.jpeg")

contur = contur_extragere(imagine)
umplere = umplere_regiuni(imagine)

plt.figure(figsize=(10, 5))
plt.subplot(1, 3, 1)
plt.imshow(cv2.cvtColor(imagine, cv2.COLOR_BGR2RGB))
plt.title('Imaginea originală')
plt.subplot(1, 3, 2)
plt.imshow(contur, cmap='gray')
plt.title('Extragere contur cu morfologie')
plt.subplot(1, 3, 3)
plt.imshow(umplere, cmap='gray')
plt.title('Umplere regiuni cu morfologie')

plt.show()