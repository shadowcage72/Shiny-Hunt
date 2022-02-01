#This code is still in testing, not ready for use


webpage="Google Chrome" #Name of the web browswer you are using.


eggcylces=10 #Right now can only handle multiples of 5. I have not tested if it will work otherwise, so test yourself to see.
#Ensure you account for Flame Body before chaning this number (ie 10 if there are 20 egg cycles with Flame Body)


from pynput.keyboard import Key, Controller
import time
import win32com.client as comclt

#Define function to press a key twice. This is the primarily used function to avoid missing a button press
def Key_Press_Twice(key):
    keyboard.press(key)

    time.sleep(.1)
    keyboard.release(key)

    time.sleep(.1)

    keyboard.press(key)

    time.sleep(.1)
    keyboard.release(key)

#Define function to press a key once.
def Key_Press_Once(key):
    keyboard.press(key)

    time.sleep(.1)
    keyboard.release(key)

def Key_Hold(key,holdtime):
    keyboard.press(key)
    time.sleep(holdtime)
    keyboard.release(key)

#Function utilized to open the menu and save the game
def Save():
    Key_Press_Twice('i')
    # print("Menu")

    time.sleep(1)

    Key_Press_Twice('9')
    # print("Save")

    time.sleep(3)

    Key_Press_Twice('l')
    # print("Confirm")

    time.sleep(3)

def Fly_To_PC():
    Key_Press_Twice('i')
    time.sleep(1)

    Key_Press_Twice('l')
    time.sleep(2)

    Key_Press_Twice('l')
    time.sleep(1)

    Key_Press_Twice('l')
    time.sleep(7)

def Move_To_Man(i):
    Key_Hold('a',.8)
    Key_Hold('w',1.25)
    Key_Hold('a',.7)
    for x in range(0, 10):
        Key_Press_Once('l')
        Key_Hold('d',2)
        Key_Hold('a',.1)

    for x in range(0, i%5+1):
        Key_Press_Once('s')
        time.sleep(2)
    Key_Press_Once('l')
    time.sleep(2)
    Key_Press_Once('l')
    time.sleep(2)
    Key_Press_Once('l')
    time.sleep(2)
    Key_Press_Once('l')


def Go_In_A_Circle():
    Key_Hold('s',.1)
    Key_Hold('d',.5)
    Key_Hold('w',.1)
    Key_Hold('a',.5)

def Walk_256():
    for x in range(0,17):
        Go_In_A_Circle()


wsh= comclt.Dispatch("WScript.Shell") # Allow the script to automatically change to the correct tab



keyboard = Controller() # Initialize the keyboard to use as a Controller

print("Starting in 3")
time.sleep(1)
print("2")
time.sleep(1)
print("1")

wsh.AppActivate(webpage)#Switch to the correct tab

time.sleep(1)
print("live")


Key_Press_Once('9')
time.sleep(.5)
Key_Press_Once('9')
time.sleep(.5)
Key_Hold('w',.3)
Key_Hold('a',.6)
Key_Press_Once('l')
time.sleep(.5)
Key_Press_Once('9')
time.sleep(.5)


for i in range(1, 10000):
    print(i)

    Fly_To_PC()
    Move_To_Man(i)

    Key_Hold('d',2)
    Key_Hold('w',2)

    Key_Press_Once('7')
    time.sleep(.5)
    Key_Press_Once('9')
    time.sleep(.5)
    Key_Press_Once('l')
    time.sleep(.5)
    Key_Press_Once('9')
    time.sleep(.5)

    for x in range(0,eggcylces/5):
        Walk_256()
    time.sleep(2)

    Key_Press_Once('l')
    time.sleep(2)
    Key_Press_Once('l')
    time.sleep(20)
    Key_Press_Once('l')
    time.sleep(2)
    Key_Press_Once('l')
    time.sleep(2)
