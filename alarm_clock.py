#alarm_sound
from playsound import playsound
import time

#ansi
CLEAR = "\033[2J" #clear the terminal
CLEAR_AND_RETURN = "\033[H" #Adjust to the data gets updating on the same line

def alarm(secs):
    time_elapsed = 0
    print(CLEAR)
    while time_elapsed < secs:
        time.sleep(1)
        time_elapsed +=1
        time_left = secs - time_elapsed
        minutes_left = time_left // 60
        seconds_left = time_left % 60
        print(f"{CLEAR_AND_RETURN}{minutes_left:02d}:{seconds_left:02d}")
    playsound("alarm_sound.mp3")



minutes = input("How many minutes do you want to set the alarm: ")
seconds = input("How many seconds do you want to set the alarm: ")
if minutes.isdigit() and seconds.isdigit():
    minutes = int(minutes) * 60
    seconds = int(seconds)
    total_time = minutes + seconds
    if total_time > 0:
        alarm(total_time)
    else:
        print("Please set a number greater than 0")
else:
    print("Please set a valid number")


