from scipy.fft import fft2
import cv2

img = cv2.imread("image.png")
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
(thresh, bw_img) = cv2.threshold(gray_img, 127, 255, cv2.THRESH_BINARY)
cv2.imshow('Black white image', bw_img)

img_data = []

for arr in img:
    small_list = []
    for items in arr:
        small_list.append(1 if items[0] > 0 else 0)
    img_data.append(small_list)

compressed = fft2(img_data)
print(compressed)
with open("data.fft", "w+") as file:
    file.write(str(compressed))
