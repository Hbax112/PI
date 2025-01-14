import cv2
import numpy as np
import matplotlib.pyplot as plt

image_path = cv2.imread('/Users/didu/Desktop/proiect pi/imagini/images.jpeg')

gray = cv2.cvtColor(image_path,cv2.COLOR_BGR2GRAY)
imagine_gri_salvata=gray
cv2.imshow('Gray image',gray )
key = cv2.waitKey()

(thresh,BlackAndWhiteImage) = cv2.threshold (gray,127,255,cv2.THRESH_BINARY)
cv2.imshow( 'Imagine Alb Negru ', BlackAndWhiteImage)
key = cv2.waitKey()

hsvImage = cv2.cvtColor(image_path, cv2.COLOR_BGR2HSV)
cv2.imshow('HSV image', hsvImage)
key = cv2.waitKey()

imgGray=cv2.imread('/Users/didu/Desktop/proiect pi/imagini/images.jpeg',0)
plt.hist(imgGray.ravel(),256,[0,256])
plt.title("Histograma imaginii in tonuri de gri")
plt.show()

color=('b','g','r')
for i, col in enumerate (color):
  histr=cv2.calcHist([image_path],[i],None,[256],[0,256])
  plt.plot(histr,color=col)
  plt.xlim([0,256])

plt.title("Histograma imaginii color")
plt.show()
