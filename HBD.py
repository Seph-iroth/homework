from datetime import datetime
import time
import sys
from playsound import playsound

# datetime object containing current date and time

haha = 'HAPPY BRITHDAY MY FRIEND !!'
rmtime = [5,9,5,5,9,5,5,5,9,5,5,5,9,5,5,9,9,9,9,9,9,9,9,9,7,7,7]

count = 0
now = datetime.now()
# dd/mm/YY H:M:S
date = now.strftime("%m-%d")
clock = now.strftime("%H:%M:%S")

age = 16
while date != "04-07":

    now = datetime.now()
    time.sleep(1)
    clock = now.strftime("%H:%M:%S")
    date = now.strftime("%m-%d")
    print(date,"   ",clock)
    if (date == "04-06") & (clock == '23:59:55'):
        for i in range(5, 0, -1):
            print(i)
            time.sleep(1)
        time.sleep(1)
        for char in haha:
            print(char, end="")
            time.sleep(rmtime[count]/15)
            count += 1
        time.sleep(1)
        time.sleep(1)
        age += 1
        break
