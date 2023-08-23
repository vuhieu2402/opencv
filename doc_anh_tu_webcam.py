import cv2
camera_id = 0
#mở camera
cap = cv2.VideoCapture(camera_id)

#đọc ảnh từ camera
while True :
    #đọc từng frame
    ret , frame =cap.read()
    
    #hiện ảnh
    if ret:
        cv2.imshow("Cam",frame)
    
    #kiểm tra nếu bấm Q thì thoát
    if cv2.waitKey(1) & 0xFF  == ord('q') :
        break
    
#giải phóng camera 
cap.release()
cv2.destroyAllWindows()
