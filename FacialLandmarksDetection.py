from dlib import shape_predictor
from dlib import get_frontal_face_detector
import cv2

imgFile = "data/group.jpg"
img = cv2.imread(imgFile)
img = cv2.resize(img, (500, 500))
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

detectFace = get_frontal_face_detector()
detectLMs = shape_predictor("shape_predictor_68_face_landmarks.dat")

bound = detectFace(imgGray)
z
    x1 = i.left()
    y1 = i.top()
    x2 = i.right()
    y2 = i.bottom()

    cv2.rectangle(img, (x1, y1), (x2, y2), (0, 0, 255), 2)

    lm = detectLMs(img, i)

    for n in range(0, 68):
        x, y = lm.part(n).x, lm.part(n).y

        cv2.circle(img, (x, y), 2, (0, 255, 0), -1)

cv2.imshow("Image 1", img)
cv2.waitKey(0)