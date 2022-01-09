#Welcome to the Automated Legendary Shiny Hunt script, created by shadowcage72

#To use this script, you will need python3, NXBT, and a USB Bluetooth adapter. This allows the computer to control the Nintendo witch.
#You will also need a Master Ball in order to reliably catch the pokemon.

#To use this code, follow the following steps:

#1. Make sure text speed is set to "fast", Send to Boxes is set to "Automatic", "Give Nicknames" is set to "Don't give", and Autosave is set to "Off"
#3. Go into your bag, set the Master Ball as your only favorite item, then sort the bag by favorites.
#2. Ensure that all pokemon in your party will not level up after catching the pokemon. This creates additional text boxes that makes the code fail.
#3. Ensure that the first move of your first pokemon is set to a move that will not kill the opposing pokemon, and that your first Pokemon does not have an ability triggering a text box before the fight
#4. Ensure that you have at least 2 pokemon in your party, and that there is an empty spot in your party for the pokemon to go to.
#5. Enter the sanctuary where the legendary pokemon resides. This will create a backup save to go back to in case the code fails. Place the stale in the slot.
#6. Save right in front of the legendary pokemon so that pressing "A" will start the encounter.



#From here, edit the following variables to your needs

webpage="Google Chrome" #Name of the web browswer you are using.

waittime=18.4 #Time in seconds for the code to wait before entering the battle menu. This is dependant of the pokemon youre catching and their ability. For Rayquaza, 18.4 is a good number. For other Pokemon without an ability causing a textbox, the ideal number is about 15.
              #I suggest testing this number yourself multiple times yourself to find a number you are comfortable with.



#I suggest testing that this code works both ways: that is to say to test that it will not catch the pokemon if it is not shiny, and that it will catch it if it is.
#To test that it will catch a shiny legendary, put a shiny pokemon as your first pokemon. This will display the same animation that would have played if the encountered pokemon were shiny. Close the program before the game saves (Or if you're feeling daring, allow it to save to ensure the entire process works, and revert back to your backup save. I do not reccomend this.)
#Remember that it is possible that an animation before the battle showing your avatar's face could show when beginning the battle. Make sure the timing works for if this animation shows and the pokemon isn't shiny, and for if this animation doesn't show and the pokemon is shiny.

#If the game saves after catching a nonshiny Pokemon:
#Don't worry! There exists a backup save. At the title screen, input up+X+B. This will prompt you to reset your save to when you entered the initial room, before encountering the legendary.
#DO NOT LEAVE THE ROOM. This may delete your backup save, leaving you stuck with a nonshiny pokemon.

#Feel free to and share this script and improve it!! If you would like to add more tips or clarify the tips I have given, please do! The code itself is simple and could be improved and optimised so feel free to do so if you wish. Personally, I chose to focus on reliability rather than optimization.





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



wsh= comclt.Dispatch("WScript.Shell") # Allow the script to automatically change to the correct tab



keyboard = Controller() # Initialize the keyboard to use as a Controller

print("Starting in 3")
time.sleep(1)
print("2")
time.sleep(1)
print("1")
time.sleep(1)
print("live")


wsh.AppActivate(webpage)#Switch to the correct tab


for i in range(0, 10000):
    print(i)

    Key_Press_Twice('l')#Encounter the Pokemon

    time.sleep(1)
    Key_Press_Twice('l')#Advance Dialogue Box

    time.sleep(waittime)
    Key_Press_Twice('l')#Opens the attack menu if the Pokemon is not shiny

    time.sleep(.1)
    Key_Press_Once(']')#Take a Screenshot

    time.sleep(5)
    Key_Press_Twice('i')#Open Poke ball menu if shiny

    time.sleep(1)
    Key_Press_Twice('l')#Use ball if shiny

    time.sleep(16)
    Key_Press_Twice('l')#Advance experience added text box


    time.sleep(2)
    Key_Press_Twice('l')#Skip text box, added in to ensure the game progresses through all text boxes

    time.sleep(1)
    Key_Press_Twice('l')#Skip Added to Pokedex Text Box

    time.sleep(2)
    Key_Press_Twice('l')#Exit Pokedex Entry

    time.sleep(1)
    Key_Press_Twice('l')#Confirm Pokedex Entry

    time.sleep(2)
    Key_Press_Twice('l')#Add Pokemon to your party

    time.sleep(20)
    Key_Press_Twice('l')#Enter battle menu again if not shiny

    time.sleep(1)

    Save()#Save the game if shiny

    Key_Press_Twice('l')#Skip text box, added in to ensure the game progresses through all text boxes

    time.sleep(.5)
    Key_Press_Twice('[')#Open home menu

    time.sleep(1)
    Key_Press_Twice('i')#Close the game

    time.sleep(1)
    Key_Press_Twice('l')#Confirm Close


    #This section is added again to ensure the game actually closes

    time.sleep(.5)
    Key_Press_Twice('[')#Open home menu

    time.sleep(1)
    Key_Press_Twice('i')#Close the game

    time.sleep(1)
    Key_Press_Twice('l')#Confirm Close


    time.sleep(1)
    Key_Press_Twice('l')#Open Game

    time.sleep(1)
    Key_Press_Twice('l')#Select Profile

    time.sleep(.1)
    keyboard.press(']')
    time.sleep(2)
    keyboard.release(']')# Take a video. A video will not be taken if everything went right. If something went wrong, this may record what happened

    time.sleep(25)
    Key_Press_Twice('l')#Skip opening credit screen

    time.sleep(3)
    Key_Press_Twice('l')#Skip Title Screen

    time.sleep(15)
