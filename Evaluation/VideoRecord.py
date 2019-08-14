import cv2


cap = cv2.VideoCapture(0)
k = 0


codec = cv2.VideoWriter_fourcc(*'MJPG')
fps = 20.0
size = (1280, 720)
out = cv2.VideoWriter('VideoRecord/0/0.avi', codec, fps, size)


while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        m = cv2.waitKey(20)
        if m == ord('q') or m == ord('s'):
            k = m
        frame = cv2.flip(frame, 1)
        cv2.imshow('frame', frame)
        if k == ord('s'):
            out.write(frame)
        elif k == ord('q'):
            break
        else:
            continue
    else:
        break


cap.release()
out.release()
cv2.destroyAllWindows()