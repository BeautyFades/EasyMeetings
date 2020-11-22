import schedule
import datetime
import time
import threading

class Clock():
    def __init__(self, formatting='normal'):
        self.formatting = formatting

    def startClock(self):
        while True:
            now = datetime.datetime.now()
            if self.formatting == 'normal':
                date_time = now.strftime("%d/%m/%Y, %H:%M:%S\n")
            elif self.formatting == 'murica':
                date_time = now.strftime("%m/%d/%Y, %H:%M:%S\n")

            print(date_time)
            time.sleep(1)

clock = Clock()

clockThread = threading.Thread(target=clock.startClock, daemon=True)
clockThread.start()






