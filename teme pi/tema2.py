import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread("/Users/didu/Desktop/proiect pi/imagini/images.jpeg", cv2.IMREAD_GRAYSCALE)

def prag_binarizare_global(image_gray):
    prag_final = np.mean(image_gray)
    
    _, imagine_binara = cv2.threshold(image_gray, prag_final, 255, cv2.THRESH_BINARY)
    
    return imagine_binara, prag_final

def egalizare_histograma(image_gray):
    imagine_egalizata = cv2.equalizeHist(image_gray)
    return imagine_egalizata

imagine_binara, prag_final = prag_binarizare_global(image)
imagine_egalizata = egalizare_histograma(image)

plt.figure(figsize=(15, 10))
plt.subplot(2, 3, 1)
plt.title("Imagine originală (grayscale)")
plt.imshow(image, cmap="gray")
plt.axis('off')
plt.subplot(2, 3, 2)
plt.title(f"Imagine binarizată (Prag final: {prag_final:.2f})")
plt.imshow(imagine_binara, cmap="gray")
plt.axis('off')
plt.subplot(2, 3, 3)
plt.text(0.5, 0.5, f"Prag final calculat:\n{prag_final:.2f}", fontsize=12, ha='center', va='center')
plt.axis('off')
plt.subplot(2, 3, 4)
plt.title("Imagine egalizată")
plt.imshow(imagine_egalizata, cmap="gray")
plt.axis('off')
plt.subplot(2, 3, 5)
plt.title("Histograma imaginii originale")
plt.hist(image.ravel(), bins=256, range=[0, 256], color='black')
plt.subplot(2, 3, 6)
plt.title("Histograma imaginii egalizate")
plt.hist(imagine_egalizata.ravel(), bins=256, range=[0, 256], color='black')
plt.tight_layout()
plt.show()
