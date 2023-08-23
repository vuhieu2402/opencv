import cv2

camera = cv2.VideoCapture(0)

for i in range(10) :
    ret, frame = camera.read()
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
last_frame = gray
while True :
    ret, frame = camera.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    abs_img = cv2.absdiff(last_frame, gray)

    last_frame = gray

    _ , threshold = cv2.threshold(abs_img, 30, 255, cv2.THRESH_BINARY)

    contours, _ = cv2.findContours(threshold, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    for contour in contours :
        if cv2.contourArea(contour) < 900 :
            continue

        x, y, w, h = cv2.boundingRect(contour)
        cv2.rectangle(frame, (x,y) , (x+w , y+h), (0,255,0), 2)

    cv2.imshow("window",frame)

    if cv2.waitKey(1) == ord('q') :
        break

cv2.destroyAllWindows()
camera.release()