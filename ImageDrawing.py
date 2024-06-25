import cv2
import numpy as np

img = np.zeros((1024, 1024, 3), np.uint8)
r = 50
while True:
    cv2.imshow('image', img)
    x = cv2.waitKey(0)
    if x == 27:
        break

    # Draw a circle in the image
    img = np.zeros((1024, 1024, 3), np.uint8)
    cv2.circle(
        img = img,
        center = (512, 512),
        radius = r,
        color = (0, 0, 255),
        thickness = 2
    )
    if x == ord('+'):
        r += 10
    elif x == ord('-'):
        r -= 10
    print(x)
cv2.destroyAllWindows()