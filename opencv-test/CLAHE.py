import numpy as np
import cv2

img = cv2.imread(r'F:\Desktop\scl.jpg', 0)
# create a CLAHE object (Arguments are optional).
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
cl1 = clahe.apply(img)
equ = cv2.equalizeHist(img)
res = np.hstack((img, equ, cl1))
# 对比原图，普通直方图均衡化，CLAHE均衡化
cv2.imshow('res', res)
cv2.waitKey(0)


