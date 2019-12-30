from pynput.keyboard import Key, Controller
import time

keyboard = Controller()
for i in range(10):
    print("This app will start autotyping in",10 - i,"second(s).",end='\r')
    i-=1
    time.sleep(1)
print("Autotyping has started. Please close this window to stop autotyping!")
# Open text from text.txt file
f = open('data.txt','r')
typeString = f.read()
f.close

for char in typeString:
    if char == '\n':
        keyboard.type("\n")    
        time.sleep(0.12)
    else:
        keyboard.press(char)
        keyboard.release(char)
        time.sleep(0.12)
