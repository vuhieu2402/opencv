import cv2

image = cv2.imread("anh\\bong1.png")



anh_xam = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
#tao nguong
ret, threshold = cv2.threshold(anh_xam, 230, 255, cv2.THRESH_BINARY)
cv2.imshow("anh",threshold)

MIN_AREA = image.shape[1] * image.shape[0] /150
#dem bong
#dem sp duong bao(contour) co kich thuoc > 1 gia tri dinh truoc ta do luong duoc
contours, _ = cv2.findContours(threshold,cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

dem =0
for cnt in contours[:-1] :
    if cv2.contourArea(cnt) >= MIN_AREA :
        dem += 1
        cv2.drawContours(image, [cnt] , -1 , (0,255,0), 2, cv2.LINE_AA)

cv2.imshow("anh", image)

print("so bong la", dem)
#tim threshold




cv2.waitKey()

cv2.destroyAllWindows()