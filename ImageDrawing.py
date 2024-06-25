import cv2
import numpy as np

img = np.zeros((1024, 1024, 3), np.uint8)
# Radius of the circle

r = 50
# Coordinates of the circle

cx = 512
cy = 512
while True:
    cv2.imshow('image', img)
    x = cv2.waitKey(0)
    if x == 27:
        break

    # Draw a circle in the image
    img = np.zeros((1024, 1024, 3), np.uint8)
    cv2.circle(
        img = img,
        center = (cx, cy),
        radius = r,
        color = (0, 0, 255),
        thickness = 2
    )
    # Increase the radius
    if x == ord('+'):
        r += 10
    # Decrease the radius
    elif x == ord('-'):
        r -= 10

    # Move the circle to the right
    elif x == ord('d'):
        cx += 10
    # Move the circle to the left
    elif x == ord('a'):
        cx -= 10
    # Move the circle up
    elif x == ord('w'):
        cy -= 10
    # Move the circle down
    elif x == ord('s'):
        cy += 10
    print(x)
cv2.destroyAllWindows()