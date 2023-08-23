import cv2
#doc anh
img = cv2.imread("simple.jpg")

#show anh
cv2.imshow("Anh",img)

#dừng màn hình
cv2.waitKey()

# resize anh
img2 = cv2.resize(img,dsize=None,fx=0.5,fy=0.5)
cv2.imshow("Anh",img2)
cv2.waitKey()
# đóng các cửa sổ
cv2.destroyAllWindows()