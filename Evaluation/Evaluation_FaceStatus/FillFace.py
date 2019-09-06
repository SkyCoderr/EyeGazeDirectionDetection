import cv2
import os


eyeCascate = cv2.CascadeClassifier('/usr/local/lib/python3.7/site-packages/cv2/data/haarcascade_eye.xml')
DIR = '/Users/jayon/Desktop/ImageEvaluation'
EVADIR = '/Users/jayon/Desktop/ImageEvaluation_FaceStatus'
EVACLASSES = [0,30,60,90,120,150,180,-30,-60,-90,-120,-150]


def scaleEyes(image):
    areas = eyeCascate.detectMultiScale(image, 1.05, 10)
    eyes = []
    for (x, y, w, h) in areas:
        eye = image[y:y+h, x:x+w]
        eyes.append([x, y, w, h, eye])
    return eyes


for integer in EVACLASSES:
    path = os.path.join(DIR, str(integer))
    new_path = os.path.join(EVADIR, str(integer))
    images = os.listdir(path)
    for image in images:
        source = cv2.imread(os.path.join(path, image), 1)
        eyes = scaleEyes(source)
        destination = cv2.imread('/Users/jayon/Desktop/0.jpg', 1)
        for (x, y, w, h, eye) in eyes:
            destination[y:y+h, x:x+w] = eye
        cv2.imwrite(os.path.join(new_path, image), destination)
