import cv2


faceCascate = cv2.CascadeClassifier('/usr/local/lib/python3.7/site-packages/cv2/data/haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture('VideoRecord/0/0.avi')
index = 0


def record(path, face):
    cv2.imwrite(path, face)


def getFace(frame):
    faces = faceCascate.detectMultiScale(frame, 1.05, 10)
    for (x, y, w, h) in faces:
        face = frame[y:y + h, x:x + w]
        return face


while cap.isOpened():
    ret, frame = cap.read()
    path = 'VideoRecord/0/Frames/'
    if ret:
        face = getFace(frame)
        if face is None:
            continue
        else:
            face = cv2.resize(face, (300, 300))
            path = path+'{}.jpg'.format(index)
            record(path, face)
            index += 1
    else:
        break


cap.release()
cv2.destroyAllWindows()


print("Complete")