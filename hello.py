import cv2
import numpy as np
img = cv2.imread(r"E:\photolib\1.jpg",cv2.IMREAD_GRAYSCALE)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.imwrite(r'E:\photolib\2.jpg',img)