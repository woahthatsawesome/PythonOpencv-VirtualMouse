import cv2
import math
import numpy as np
import functools
from random import randint
import pyautogui
pyautogui.FAILSAFE = False
tracker_types = ['BOOSTING', 'MIL', 'KCF','TLD', 'MEDIANFLOW', 'GOTURN', 'MOSSE', 'CSRT']

tracker = cv2.TrackerMIL_create()
tracker1 = cv2.TrackerMedianFlow_create()
cap = cv2.VideoCapture(0)
ret, frame = cap.read()

bboxes = []
colors = []

while True:
 bbox = cv2.selectROI('select your ROI', frame)
 bboxes.append(bbox)
 colors.append((randint(0, 255), randint(0, 255), randint(0, 255)))
 print('Press q after selecting what you want to track. Tracking will then activate.')
 print('Press any other key to quit.')
 k = cv2.waitKey(0) & 0xFF
 if k==ord('q'):
   break
print('Selected bounding boxes {}'.format(bboxes))

trackertype = "MOSSE"
multiTracker = cv2.TrackerMOSSE_create()
lol = multiTracker.init(frame, bbox)
def left():
    angle = x / y
    print('Angles is:', angle)
    if angle > 1.19:
     print('Angle is:', angle)
     print('Left is clicked')
     pyautogui.click(button='left')

def right():
    #I need a way to do right clicks, anyone got ideas?#
    '''pyautogui.click(button='right')'''
while cap.isOpened():
 ret, frame = cap.read()
 lol, boxes = multiTracker.update(frame)

 if 1<2:
    newbox = boxes
    print("boxes=", boxes)
    p1 = (int(boxes[0]), int(boxes[1]))
    p2 = (int(newbox[0] + newbox[2]), int(newbox[1] + newbox[3]))
    r = cv2.rectangle(frame, p1, p2,(255, 0, 0), 2, 1)
    print(p1)
    print(p2)
    res1 = functools.reduce(lambda sub, ele: sub * 10 + ele, p1)
    res2 = functools.reduce(lambda sub, ele: sub * 10 + ele, p2)
    print(res1)
    print(res2)
    cv2.imshow('Tracking is happening!!!!!!', frame)
    frame_flip = cv2.flip(frame, 1)
    cv2.imshow('Mouse activated', frame_flip)
    x1 = (int(newbox[0]))
    x2 = (int(newbox[1]))
    y1 = (int(newbox[2]))
    y2 = (int(newbox[3]))
    print("The coordinates for mouse are:",x1, x2, y1, y2)
    x = (x1 +x2) * 2
    y = (y1 + x2) * 2
    print("mouse is moving to:",x, y)
    pyautogui.moveTo(x, y)
    left()
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cap.release()
        cv2.destroyAllWindows()
        if cv2.waitKey(7000000) & 0xFF == ord('q'):
            cv2.destroyAllWindows()

 if lol != lol:
     print('Tracking Failure')
     cv2.putText(frame, "Tracking failure detected", (100, 80), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 0, 255), 2)

cv2.imshow('Tracking is happening!!!!!!', frame)
if cv2.waitKey(1) & 0xFF == ord('q'):
 cap.release()
 cv2.destroyAllWindows()
