import cv2
import numpy as np

img = cv2.imread('anh//goun.jpg')

rows, cols = img.shape[0:2]

input_mt = np.float32([[0,0], [cols-1,0], [0,rows-1]])
output_mt = np.float32([[0,0], [cols/2,0], [cols/2,rows-1]])

M = cv2.getAffineTransform(input_mt, output_mt)
dst = cv2.warpAffine(img, M, (cols, rows))

cv2.imshow('IMG' , dst)
cv2.waitKey(0)