import cv2 as cv
from time import sleep
import numpy as  np

fd = cv.CascadeClassifier(cv.data.haarcascades+'haarcascade_frontalface_default.xml')
sd = cv.CascadeClassifier(cv.data.haarcascades+'haarcascade_smile.xml')
vid = cv.VideoCapture(0)
notcaptuerd = True 
while notcaptuerd:
    flag , img = vid.read()
    if flag:
        # Processing Code (image came here)
        faces = fd.detectMultiScale(img,scaleFactor= 1.1,minNeighbors=5,minSize=(50,50))
        np.random.seed(50)
        colors = np.random.randint(0,255,(len(faces),3)).tolist()
        i=0
        for x,y,w,h in faces:
            face = img[y:y+h,x:x+w,:].copy()
            smiles = sd.detectMultiScale(face,scaleFactor= 1.1,minNeighbors=5,minSize=(50,50))
            if len(smiles)==1:
                cv.imwrite('my.png',img)
                notcaptuerd=False
                break
            cv.rectangle( img , pt1=(x,y), pt2=(x+w,y+h), color=colors[i],thickness=8 )  
            i=i+1
        cv.imwrite('myfile.png',img)
        cv.imshow('Preview',img)
        key = cv.waitKey(1)
        if key == ord('c'):
            break
    else:
        print('No frames')
        break
    sleep(0.1)
vid.release()
cv.destroyAllWindows()