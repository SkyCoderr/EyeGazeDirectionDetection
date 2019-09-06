import cv2
import os


eyeCascate = cv2.CascadeClassifier('/usr/local/lib/python3.7/site-packages/cv2/data/haarcascade_eye.xml')
DIR = '/Users/jayon/Desktop/ImageEvaluation'
EVADIR = '/Users/jayon/Desktop/ImageEvaluation_EyeStatus'
EVACLASSES = [0,30,60,90,120,150,180,-30,-60,-90,-120,-150]


def scaleEyes(frame):
    eyes = eyeCascate.detectMultiScale(frame, 1.05, 10)
    for (x, y, w, h) in eyes:
        # Draw rectangle around the eyes
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 255, 255), -1)


for integer in EVACLASSES:
    path = os.path.join(DIR, str(integer))
    new_path = os.path.join(EVADIR, str(integer))
    images = os.listdir(path)
    for image in images:
        im = cv2.imread(os.path.join(path, image), 1)
        scaleEyes(im)
        cv2.imwrite(os.path.join(new_path, image), im)
