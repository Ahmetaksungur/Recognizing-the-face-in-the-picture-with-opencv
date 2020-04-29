import cv2

eyes_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

img = cv2.imread('indir.jpg')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = eyes_cascade.detectMultiScale(gray, 1.1, 4)

for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 4)

cv2.imshow('Yuz Tanima', img)
cv2.waitKey()
