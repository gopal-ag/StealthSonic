import cv2
import numpy as np
import serial
import pyautogui
# ser = serial.Serial('/dev/cu.usbmodem1101',9600)

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)
d = 69

while True:
    
    _, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    
    if d != '0':
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
            cv2.putText(img, f'Intusion detected', (x, y-8), color=(0, 0, 255), fontFace=cv2.FONT_HERSHEY_DUPLEX, fontScale=1)
    cv2.imshow('Image', img)
    # ss = pyautogui.screenshot()
    # ss = cv2.cvtColor(np.array(ss), cv2.COLOR_RGB2BGR)
    # cv2.imwrite("ss1.png", ss)
    k = cv2.waitKey(30) & 0xff
    if k==27:
        break
cap.release()