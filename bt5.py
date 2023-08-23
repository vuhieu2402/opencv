import cv2

image = cv2.imread("")

anh_xam = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

ret , nguong = cv2.threshold(anh_xam,127, 255, cv2.THRESH_BINARY)

contours, _ = cv2.findContours(nguong, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
MIN_HEIGHT = image.shape[0] * 0.5
MAX_WIDTH = image.shape[1] * 0.1

dem = 0
for cnt in contours :
    #lay toa do hinh chu nhat bao quanh duong bien
    x, y, w, h =cv2.boundingRect(cnt)
    if w <= MAX_WIDTH and h >= MIN_HEIGHT :
        dem+=1
        crop_number = image[y:y+h , x:x+w]
        cv2.imwrite("anh\\{}.png".format(dem),crop_number)
        cv2.drawContours(image, [cnt] , -1 , (0,255,0) , 2, cv2.LINE_AA)



cv2.imshow("anh" ,image)






