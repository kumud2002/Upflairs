import plotly
import cv2 as cv
import plotly.express as px
import skimage

vid = cv.VideoCapture(0)
while True:
    flag,img = vid.read()
    if flag:
        img  = cv.cvtColor(img,cv.COLOR_BGR2RGB) # Extra Step
        im_p = cv.subtract(img[:,:,-1],cv.cvtColor(img,cv.COLOR_RGB2GRAY)) #other librarys show in RGB-
        th, img_p2 = cv.threshold(im_p,60,255,cv.THRESH_BINARY)
        img_p3 = skimage.morphology.remove_small_objects(img_p2.astype(bool),50)    # To grow the circle
        img_p4 = cv.dilate(img_p3.astype('uint8'),cv.getStructuringElement(cv.MORPH_ELLIPSE,(20,20))).astype(bool) 
        img_p5 = skimage.morphology.remove_small_objects(img_p4,500)
        rp = skimage.measure.regionprops(skimage.measure.label(img_p5))
        img_preview = img.copy()
        if len(rp)>0:
            (y1,x1,y2,x2) = rp[0].bbox
            cv.rectangle(img_preview,pt1=(x1,y1),pt2=(x2,y2),color = (0,150,255),thickness=8)
        cv.imshow('Preview',img_preview[:,:,::-1])
        key = cv.waitKey(1)
        if key == ord('c'):vbnm,
            break

cv.destroyAllWindows()
cv.waitKey(1)
vid.release()