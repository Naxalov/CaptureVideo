import cv2


# Load the Cascade Classifier
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# From Camera
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    # Convert to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect the faces
    faces = face_cascade.detectMultiScale(
        image=gray,
        scaleFactor=1.1,
        minNeighbors=5,
       
    )
    print((faces))

    # Draw the rectangle around each face
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

    # Display
    cv2.imshow('frame', frame)

    # Stop if escape key is pressed
    k = cv2.waitKey(30) & 0xff
    if k==27:
        break

# Release the VideoCapture object
cap.release()
# Destroy all the windows
cv2.destroyAllWindows()
