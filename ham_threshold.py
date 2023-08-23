
#chuyển ảnh màu -> xám -> chọn ngưỡng -> duyệt từng điểm ảnh

import cv2
from pygame.transform import threshold

img = cv2.imread("beauty.jpg")
#chuyển màu
gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# 127 là ngưỡng
# ret,thres_binary = cv2.threshold(gray_img,127,255,cv2.THRESH_BINARY)
# cv2.imshow("anh gray",thres_binary)




#adaptive threshold: tu dong lay nguong
threshold = cv2.adaptiveThreshold(gray_img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 5)
cv2.imshow(threshold)



cv2.waitKey()
cv2.destroyAllWindows()


# hàm tìm cạnh Canny
#hàm làm mờ,giảm nhiễu