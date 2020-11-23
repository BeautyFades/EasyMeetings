import schedule
import datetime
import time
import threading
import webbrowser
import cv2
import numpy as np
import pyautogui as pgui

class Clock():
    def __init__(self, formatting='normal'):
        self.formatting = formatting

    def startClock(self):
        while True:
            currentTime = datetime.datetime.now()
            dateTime = ''
            if self.formatting == 'normal':
                dateTime = currentTime.strftime("%d/%m/%Y, %H:%M:%S\n")
            elif self.formatting == 'murica':
                dateTime = currentTime.strftime("%m/%d/%Y, %H:%M:%S\n")

            print(dateTime)
            time.sleep(1)

clock = Clock()

clockThread = threading.Thread(target=clock.startClock, daemon=True)
clockThread.start()


meetingUrl = 'https://meet.google.com/gvc-jtay-oox'
chromePath = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
firefoxPath = ''
edgePath = ''
webbrowser.get(chromePath).open(meetingUrl)

trigger = cv2.imread("joinButton.png")
method = cv2.TM_SQDIFF_NORMED
sizeX, sizeY = pgui.size()
method = cv2.TM_SQDIFF_NORMED  # Method to use when comparing captures

currentCapture = pgui.screenshot('currentCapture.png', region=(0, 0, sizeX, sizeY))
currentCapture = cv2.cvtColor(np.array(currentCapture), cv2.COLOR_RGB2BGR)
result = cv2.matchTemplate(trigger, currentCapture, method)
cv2.imshow('result', result)
confidence = round((1 - np.amin(result)) * 100, 4)

print(confidence)











