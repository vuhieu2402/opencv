import cv2
from PIL.ImageOps import crop

cam = cv2.VideoCapture(0)

while True:
    ret , frame = cam.read()
    if ret:

        #tinh trong tam
        width = frame.shape[1]
        height = frame.shape[0]
        centre_x = width // 2
        centre_y = height // 2

        #tinh kich thuoc vung trung tam can lay
        crop_width = int(width * 0.2)
        crop_height = int(height * 0.2)

        left_top_x = centre_x - crop_width // 2
        left_top_y = centre_y - crop_height //2

        crop_frame = frame[left_top_y:left_top_y+crop_height,left_top_x:left_top_x+crop_height]

        cv2.imshow("crop",crop_frame)
        cv2.imshow("Cam",frame)

    if cv2.waitKey(1) == ord('q'):
        break



cv2.destroyAllWindows()
cam.release()
