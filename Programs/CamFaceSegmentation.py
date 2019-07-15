import cv2


cap = cv2.VideoCapture(0)
faceCascate = cv2.CascadeClassifier('/usr/local/lib/python3.7/site-packages/cv2/data/haarcascade_frontalface_default.xml')
index = 0


# Detect the face in an image and segment it
def getFace(frame):
    faces = faceCascate.detectMultiScale(frame, 1.05, 10)
    for (x, y, w, h) in faces:
        face = frame[y:y + h, x:x + w]
        return face

# Store the face image to a certain path with the index specified
def record(face, index):
    path = 'ImageData/Left/{}.jpg'.format(index)
    cv2.imwrite(path, face)


# If the key pressed is s, the face in the frame is saved, if it's q, the camera closes and the exits the system
while cap.isOpened():
    ret, frame = cap.read()
    filename = 0
    if ret:
        cv2.imshow('frame', frame)
        k = cv2.waitKey(1)
        if k == ord('s'):
            face = getFace(frame)
            if face is None:
                continue
            else:
                face = cv2.resize(getFace(frame), (300, 300))
                face = cv2.flip(face, 1)
            record(face, index)
            index += 1
        elif k == ord('q'):
            break
    else:
        break


cap.release()
cv2.destroyAllWindows()