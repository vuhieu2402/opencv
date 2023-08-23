import cv2
import numpy as np

#dinh nghia nguong loc mau
lower_red = np.array([0,100,100])
upper_red = np.array([10,255,255])
lower_green = np.array([40,50,50])
upper_red = np.array([90,255,255])
lower_yellow = np.array([15,150,150])
upper_yellow = np.array([35,255,255])

#doc anh
image = cv2.imread("")
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

mask_red = cv2.inRange(hsv, lower_red, upper_red)



