# Gunnar Landström
# Datateknik - DT201G
# 2025-12-17
# Labb 4

from threading import Thread, Semaphore, Lock
from datetime import datetime

import time
import random

readerSemaphore = Semaphore(3);
writerSemaphore = Semaphore(2);
resourceLock = Lock();

global_datetime = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')

class readCurrentDate(Thread):
    def run(self):
        global global_datetime
        while True:
            if (writerSemaphore._value == 2):
                readerSemaphore.acquire()
                print("Reader acquiring resource")
                print("Current date and time: " + global_datetime +"\n")
                readerSemaphore.release()
                print("Reader released resource")
                time.sleep(.2)

class writeCurrentDate(Thread):
    def run(self):
        count = 0
        global global_datetime
        while True:

            if (count == 0):
                writerSemaphore.acquire()
                count += 1
            while(readerSemaphore._value != 3):
                pass
            if (readerSemaphore._value == 3):
                with resourceLock:
                    print("Writer acquiring resource")
                    while(readerSemaphore._value != 0):
                        readerSemaphore.acquire()
                    print(global_datetime)
                    global_datetime = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
                    print(global_datetime)
                    while(readerSemaphore._value != 3):
                        readerSemaphore.release()
                    print("Writer released resource")
                    writerSemaphore.release()
                    count -= 1
                time.sleep(.1)
                
class writeCurrentDateReversed(Thread):
    def run(self):
        count = 0
        global global_datetime
        while True:
            if(count == 0):
                writerSemaphore.acquire()
                count += 1
            while(readerSemaphore._value != 3):
                pass
            if (readerSemaphore._value == 3):
                with resourceLock:
                    print("Reverse writer acquiring resource")
                    while(readerSemaphore._value != 0):
                        readerSemaphore.acquire()
                    print(global_datetime)
                    global_datetime = datetime.utcnow().strftime('%S:%M:%H %d-%m-%Y')
                    print(global_datetime)
                    while(readerSemaphore._value != 3):
                        readerSemaphore.release()
                    print("Reverse write released resource")
                    writerSemaphore.release()
                    count -= 1
                time.sleep(.1)

readerOne = readCurrentDate()
readerTwo = readCurrentDate()
readerThree = readCurrentDate()
writerOne = writeCurrentDate()
writerTwo = writeCurrentDateReversed()

readerOne.start()
readerTwo.start()
readerThree.start()
writerOne.start()
writerTwo.start()