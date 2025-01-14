import cv2
import os
image_path = '/Users/didu/Desktop/proiect pi/imagini/images.jpeg'
directory = '/Users/didu/Desktop/proiect pi/imagini'
img = cv2.imread(image_path)
try:
    cv2.imshow('Image',img)
except:
    print("Image not exist")
key = cv2.waitKey()
if key == 27: 
 cv2.destroyAllWindows()  

os.chdir(directory)
print("Before saving image:")
print(os.listdir(directory))
filename = 'SavedCat.jpg'
cv2.imwrite(filename,img)
print("After saving image:")
print(os.listdir(directory))
print('Successfully saved')