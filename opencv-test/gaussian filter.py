import gaussiannoise
import cv2

img = cv2.imread(r"F:\Desktop\t1.png")
gaussiannoise.GaussianNoise(img, 0.5, 2, 0.5)
img1 = cv2.GaussianBlur(img, (5, 5), 2)
cv2.namedWindow('tt', cv2.WINDOW_NORMAL)
cv2.namedWindow('tt_gaussian_blur', cv2.WINDOW_NORMAL)
cv2.imshow('tt', img)
cv2.imshow('tt_gaussian_blur', img1)
cv2.waitKey(0)
