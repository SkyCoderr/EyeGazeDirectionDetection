import cv2


cap = cv2.VideoCapture(0)
faceCascate = cv2.CascadeClassifier('/usr/local/lib/python3.7/site-packages/cv2/data/haarcascade_frontalface_default.xml')


def scaleFace(frame):
    faces = faceCascate.detectMultiScale(frame, 1.05, 10)
    for (x, y, w, h) in faces:
        # Draw rectangle around the face
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 255, 255), 1)


cap.set(cv2.CAP_PROP_FRAME_WIDTH, 100)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 100)


while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        frame = cv2.flip(frame, 1)
        scaleFace(frame)
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) == ord('q'):
            break
    else:
        break


cap.release()
cv2.destroyAllWindows()