import cv2
import numpy as np
#  Video Capture
cap = cv2.VideoCapture(1)

while True:
    ret, frame = cap.read()
    if ret == True:
        cv2.imshow('frame', frame)
        if cv2.waitKey(1)  == ord('q'):
            break
    else:
        break
    

cap.release()
cv2.destroyAllWindows()