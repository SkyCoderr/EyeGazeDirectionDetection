import cv2
import os


DIR = '/Users/jayon/Desktop/ImageEvaluation'
EVADIR = '/Users/jayon/Desktop/ImageEvaluation_EyeFaceRelativePosition'
EVACLASSES = [0,30,60,90,120,150,180,-30,-60,-90,-120,-150]


for integer in EVACLASSES:
    path = os.path.join(DIR, str(integer))
    new_path = os.path.join(EVADIR, str(integer))
    images = os.listdir(path)
    for image in images:
        im = cv2.imread(os.path.join(path, image), 1)
        im = cv2.flip(im, -1)
        cv2.imwrite(os.path.join(new_path, image), im)