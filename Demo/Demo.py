import cv2
import numpy as np
import tensorflow as tf
from tkinter import *
import PIL.ImageTk as Tk
import PIL.Image as im



faceCascate = cv2.CascadeClassifier('/usr/local/lib/python3.7/site-packages/cv2/data/haarcascade_frontalface_default.xml')
model = tf.keras.models.load_model('model1.h5')
CATEGORY = ['Left','Right','Origin']
k = -1
direction = 'origin'


# Detect the face in an image and segment it
def getFace(frame):
    faces = faceCascate.detectMultiScale(frame, 1.05, 10)
    for (x, y, w, h) in faces:
        face = frame[y:y + h, x:x + w]
        return face


root = Tk()
root.title('Demonstration')


def display():
    cap = cv2.VideoCapture(0)
    while k != ord('q'):
        ret, frame = cap.read()
        if ret:
            k = cv2.waitKey(50)
            frame = cv2.flip(frame,1)
            cv2.imshow('frame', frame)
            face = cv2.cvtColor(cv2.resize(getFace(frame), (100,100)),cv2.COLOR_RGB2GRAY)
            face = np.array(face).reshape(100, 100, 1)
            direction = CATEGORY[model.predict(face)]
            photo = Tk.PhotoImage(im.fromarray(frame))
            display = Label(root, photo, 1500, 1500)
            display.grid(0, 0)
            display.pack()
        else:
            continue
    cap.release()
    cv2.destroyAllWindows()


start = Button(root, 'Display', display)
root.mainLoop()