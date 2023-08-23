import cv2
import numpy as np

img = cv2.imread('')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

_ , threshold = cv2.threshold(gray, 235, 255, cv2.THRESH_BINARY)

contours, _ = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

font = cv2.FONT_HERSHEY_COMPLEX

for cnt in contours:
    approx = cv2.approxPolyDP(cnt, 0.01*cv2.arcLength(cnt, True), True)
    cv2.drawContours(img, [approx], -1 , (0,255,0) , 1)
    x = approx.ravel()[0]
    y = approx.ravel()[1]
    
    if len(approx) == 3:
        cv2.putText(img, "tam giac" , (x,y), font, (0,0,255),1, cv2.LINE_AA)
        
    elif len(approx) == 4:
        cv2.putText(img, "chu nhat" , (x,y), font, (0,0,255),1, cv2.LINE_AA)
    
    elif len(approx) == 5:
        cv2.putText(img, "ngu giac" , (x,y), font, (0,0,255),1, cv2.LINE_AA)
        
    else :
        cv2.putText(img, "hinh tron" , (x,y), font, (0,0,255),1, cv2.LINE_AA)

cv2.imshow("anh", img)
cv2.imshow("anh" , threshold)
cv2.waitKey(0)
cv2.destroyAllWindows()