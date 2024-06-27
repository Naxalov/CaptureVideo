import cv2


# Load the Cascade Classifier
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_extended.xml')

# Load the image
img = cv2.imread('noble.jpg')

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detect the faces
faces = face_cascade.detectMultiScale(
     image=gray,
     scaleFactor=1.1,
     minNeighbors=5,
    
)
# Print shape of faces
print(faces)

# Draw the rectangle around each face
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

# Display
cv2.imshow('img', img)

# Stop if escape key is pressed
k = cv2.waitKey(0)

# Close all windows
cv2.destroyAllWindows()