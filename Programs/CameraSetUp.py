import cv2 as cv

cap = cv.VideoCapture(0)

print(cap.get(cv.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv.CAP_PROP_FRAME_HEIGHT))

cap.set(cv.CAP_PROP_FRAME_WIDTH, 5000)
cap.set(cv.CAP_PROP_FRAME_HEIGHT, 5000)

print(cap.get(cv.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv.CAP_PROP_FRAME_HEIGHT))

while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        cv.imshow('frame', frame)
        if cv.waitKey(50) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
cv.destroyAllWindows()
