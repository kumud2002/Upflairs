# IN GRAY SCALE (Black - White)--

import cv2 as cv
import skimage as ski
import matplotlib.pyplot as plt


vid = cv.VideoCapture(0)
while True:
    flag , img = vid.read()
    if flag:
        # Processing Code (image came here)
        img_gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
        th , img_bw = cv.threshold(img_gray,170,255,cv.THRESH_BINARY)
        cv.imshow('Preview',img_bw)
        key = cv.waitKey(1)
        if key == ord('c'):
            break
    else:
        print('No Frames')
        break
vid.release()
cv.destroyAllWindows()