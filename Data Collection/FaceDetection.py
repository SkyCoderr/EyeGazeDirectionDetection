import cv2


faceCascate = cv2.CascadeClassifier('/usr/local/lib/python3.7/site-packages/cv2/data/haarcascade_frontalface_default.xml')
image = cv2.imread('/Users/jayon/Desktop/IMG.jpg', 0)
image = cv2.resize(image, (100, 100))


faces = faceCascate.detectMultiScale(image, 1.1, 5)
for (x, y, w, h) in faces:
    # Draw rectangle around the face
    cv2.rectangle(image, (x, y), (x+w, y+h), (255, 255, 255), 1)


cv2.imshow('face', image)
cv2.waitKey(0)
cv2.destroyAllWindows()