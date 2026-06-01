import time
from datetime import datetime
from playsound import playsound

# ask the user for alarm time
alarm_time = input("Enter alarm time (HH:MM, e.g. 06:30): ")
print("Alarm set for", alarm_time)

while True:
    now = datetime.now().strftime("%H:%M")  # current time
    if now == alarm_time:
        print("\n⏰ WAKE UP! Time is", now)
        for i in range(5):   # repeat 5 times
            playsound("alarm.wav")  # make sure your file is correct
        break
    time.sleep(1) # prevents CPU for overuse

