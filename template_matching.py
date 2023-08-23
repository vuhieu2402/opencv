import cv2

img1 = cv2.imread('beauty.jpg')
img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)

img2 = cv2.imread('cat.png')
img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)

method = eval('cv2.TM_CCOEFF')
res = cv2.matchTemplate(img1,img2, method)




min_value, max_value, min_loc, max_loc = cv2.minMaxLoc(res)

if method in [cv2.TM_SQDIFF_NORMED, cv2.TM_SQDIFF] :
    top_left = min_loc
else:
    top_left = max_loc

height, width, channel = img2.shape
bottom_right = (top_left[0]+width, top_left[1]+height)
cv2.rectangle(img1, top_left, bottom_right, (255,0,0), 1)

cv2.imshow("anh",img1)


cv2.waitKey()

cv2.destroyAllWindows()