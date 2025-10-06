import time
import pyautogui
import pyperclip
from pynput import keyboard
import keyboard as key
from pynput.keyboard import Key, Controller as KeyboardController
from pynput.mouse import Controller as MouseController
#I am going to give you raw information and you are going to process it in to groups(Link, Car, Total, Miles, MPG, Year, Price, Fees, Damage)

keyboard_controller  = KeyboardController()
mouse_controller = MouseController()
carnum = 0

#stop and start button
def on_press(key):
    time.sleep(.1)
    global run
    try:
        if key.char == '=':
            run = True
        elif key.char == '-':
            run = False
    except AttributeError:
        pass


def copy_selectedText():
    keyboard_controller.press(Key.ctrl)
    keyboard_controller.tap("c")
    keyboard_controller.release(Key.ctrl)

def writeToFile(text):
    with open("rawoutput.txt", "a", encoding="utf-8") as file:
        file.write(text)

def clipBoardtoFile():
    text = pyperclip.paste()
    writeToFile(text)

def previuosPage():
    keyboard_controller.press(Key.alt)
    keyboard_controller.tap(Key.left)
    keyboard_controller.release(Key.alt)

def control_Plus_Key(key):
    keyboard_controller.press(Key.ctrl)
    keyboard_controller.tap(key)
    keyboard_controller.release(Key.ctrl)

def get_Positions_USER(run_once):
    space_was_pressed = False
    positionholder = []
    while True:
        time.sleep(.02)
        if key.is_pressed("shift"):
            if not space_was_pressed: #preventing holding
                tempX, tempY = pyautogui.position()
                print("Position ["+str(len(positionholder)+1) +"] = {" + str(tempX)+", "+ str(tempY)+"}")
                positionholder.append([tempX, tempY]) 
                space_was_pressed = True
                if run_once:
                    return positionholder
        else:
            space_was_pressed = False
        
        if key.is_pressed("esc") and not run_once:
            return positionholder

    



def main_program():
    global run
    global carnum

    #introduction
    print("This program requires you to open Facebook Marketplace and set the positions of each post, once that is done it will automate the rest\nPress SHIFT on the location of each post and Press ESC= when you are done.")
    
    #Gets Post Positions
    positionholder = get_Positions_USER(False) #stores as ([x,y],[x,y],ect)
    time.sleep(.1)

    #give user info of how to use
    print("\n\nNow we have to positions of the post saved ")
    print("run the program when ready")
    print("To start Press = To start Press - to stop")
    

    #AUTO-Post-clicker
    while True:  
        for i in range(len(positionholder)):
            #Check if running
            if not run:
                break

            #click on of the post          
            pyautogui.click(*positionholder[i])
            print("clicked post")

            #time to wait for link to load
            time.sleep(4)


            # Copying post
            control_Plus_Key("a")         #Ctrl A
            print("pressed ctrl a") 
            time.sleep(.05)
            copy_selectedText()
  
            #Pasting Post
            carnum += 1
            writeToFile("["+str(carnum)+"]")
            clipBoardtoFile()
            print("copied and pasted post")

            # Copying and pasting the Link
            control_Plus_Key("l")
            copy_selectedText()
            time.sleep(.1) 
            writeToFile("\n{")
            clipBoardtoFile()
            writeToFile("}\n\n\n")

            print("copied and pasted link")

            #back To previous Page
            previuosPage()
            print("went back to main page" + str(i))

        run=False 

listener = keyboard.Listener(on_press=on_press) 
listener.start()

run = False
main_program()



