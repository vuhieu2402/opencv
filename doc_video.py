
import cv2


video_file = "anh\\video1.mp4"
video = cv2.VideoCapture(video_file)



while True:

    ret , frame = video.read()

    if ret:
        cv2.imshow("video",frame)

    phim_bam = cv2.waitKey(1)
    if phim_bam == ord('q'):
        break

video.release()
cv2.destroyAllWindows()
