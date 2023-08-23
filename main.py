import cv2
import imutils

#lenh doc anh cv2.imread
anh_doc = cv2.imread("anh\\goun.jpg")

#xoay anh
anh_xoay = imutils.rotate(anh_doc, 90)
#show anh

cv2.imshow("anh",anh_doc)
cv2.imshow("Goun Youn Jung",anh_xoay)

#dung chuong trinh cho bam phim
cv2.waitKey()
cv2.destroyAllWindows()