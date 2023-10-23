import cv2
import mediapipe as mp
cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()

    cv2.imshow('image',img)
    if cv2.waitKey(5) & 0XFF == ord('q'):
        break
