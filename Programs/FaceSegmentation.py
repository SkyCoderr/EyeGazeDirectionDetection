import cv2


faceCascate = cv2.CascadeClassifier('/usr/local/lib/python3.7/site-packages/cv2/data/haarcascade_frontalface_default.xml')
image = cv2.imread('/Users/jayon/Desktop/IMG.jpg', 0)
image = cv2.resize(image, (100, 100))


faces = faceCascate.detectMultiScale(image, 1.05, 10)
for (x, y, w, h) in faces:
    # Extract the face from the original image
    face = image[y:y+h, x:x+w]
    # Draw rectangle around the face
    cv2.rectangle(image, (x, y), (x+w, y+h), (255, 255, 255), 1)


cv2.imshow('face', face)
cv2.waitKey(0)
cv2.destroyAllWindows()