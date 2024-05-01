from PIL import Image, ImageTk
import cv2

image = Image.open('Image/test_08-Copy.jpg')
print(type(image))

img = cv2.imread('Image/test_08-Copy.jpg')
img_2 = Image.fromarray(img)
print(type(img_2))