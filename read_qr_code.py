import cv2

qr_cd = cv2.QRCodeDetector()

cam = cv2.VideoCapture(0)
while True:
    ret , frame = cam.read()
    if ret :
        ret_qr, decode_info, point, _ = qr_cd.detectAndDecodeMultiple(frame)
        if ret_qr :
            for s,p in zip(decode_info, point) :
                if s:
                    cv2.putText(frame, s , (100,100),cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0),1, cv2.LINE_AA)
                else:
                    pass
                color = (0,0,255)
                    
                frame = cv2.polylines(frame, [p.astype(int)] ,True ,color,8)  
                
        cv2.imshow('QR code', frame)
    phim_bam = cv2.waitKey(1)
    if phim_bam == ord('q'):
        break
    
cv2.destroyAllWindows()