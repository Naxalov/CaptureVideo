import cv2
import numpy as np
# Print opencv version
print(cv2.__version__)

# Create a white image with 3 channels size 512x512 using numpy
img = np.ones((512, 512, 3), np.uint8) * 255

# Show the image
cv2.imshow('image', img)

# Wait for any key to be pressed
k=cv2.waitKey(0)
print(k)
