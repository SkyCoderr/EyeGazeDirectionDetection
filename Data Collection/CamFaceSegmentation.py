import cv2


cap = cv2.VideoCapture(0)
faceCascate = cv2.CascadeClassifier('/usr/local/lib/python3.7/site-packages/cv2/data/haarcascade_frontalface_default.xml')
# faceCascate = cv2.CascadeClassifier('/Users/jayon/Desktop/face.xml')
index = 0
k = -1


# Detect the face in an image and segment it
def getFace(frame):
    faces = faceCascate.detectMultiScale(frame, 1.05, 10)
    for (x, y, w, h) in faces:
        face = frame[y:y + h, x:x + w]
        return face


# Store the face image to a certain path with the index specified
def record(face, index):
    path = 'ImageData/Origin/{}.jpg'.format(index)
    cv2.imwrite(path, face)


# Press s then it starts recording, then press any key other than q to stop recording. Press q to stop the program.
while k != ord('q'):
    ret, frame = cap.read()
    if ret:
        # First flip the image horizontally
        frame = cv2.flip(frame, 1)
        cv2.imshow('frame', frame)
        m = cv2.waitKey(50)
        if m != -1:
            k = m
        if k == ord('s'):
            face = getFace(frame)
            # If for one frame in which the face isn't recognized
            if face is None:
                continue
            # If a face is recognized
            else:
                face = cv2.resize(getFace(frame), (300, 300))
            record(face, index)
            index += 1
        else:
            continue
    else:
        break


cap.release()
cv2.destroyAllWindows()