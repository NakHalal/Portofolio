import pyautogui
import time

message = "p"
n = 100


print("START")

count = 5
while(count != 0) :
    time.sleep(1)
    count -= 1

print("\n COMPLETE")

for i in range(0, int(n)):
    pyautogui.typewrite(message + '\n')