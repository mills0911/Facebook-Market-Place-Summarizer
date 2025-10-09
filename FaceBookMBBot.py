
import time
import subprocess
import pyautogui
import pyperclip
import os
from pynput import keyboard
import keyboard as key
from pynput.keyboard import Key, Controller as KeyboardController
from pynput.mouse import Controller as MouseController


keyboard_controller  = KeyboardController()
mouse_controller = MouseController()


#stop and start button
def on_press(key):
    global run, shiftIsPressed
    try:
        if hasattr(key, 'char'):
            if key.char == '=':
                run = True
            elif key.char == '-':
                run = False

        if key == Key.shift:
            shiftIsPressed = True


    except AttributeError:
        pass


def on_release(key):
    global shiftIsPressed, exit
    try: 
        if key == Key.shift:
            shiftIsPressed = False
        if key == Key.esc:
            exit = True
    except AttributeError:
        pass



def copy_selectedText():
    keyboard_controller.press(Key.ctrl)
    keyboard_controller.tap("c")
    keyboard_controller.release(Key.ctrl)

def writeToFile(text):
    with open(rawfile_txt, "a", encoding="utf-8") as file:
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
    global shiftIsPressed, exit
    hasRanOnce = False
    positionholder = []
    while True:
        time.sleep(.02)
        if shiftIsPressed:
            if not hasRanOnce: #preventing holding
                tempX, tempY = pyautogui.position()
                print("Position ["+str(len(positionholder)+1) +"] = {" + str(tempX)+", "+ str(tempY)+"} (ESC When Finished)" )
                positionholder.append([tempX, tempY]) 
                hasRanOnce = True
                if run_once:
                    return positionholder
        else:
            hasRanOnce = False
        
        if exit and not run_once:
            exit = False
            return positionholder

    



def main_program():
    global run, exit, rawfile_txt, shiftIsPressed
    run = False
    exit = False
    shiftIsPressed = False
    carnum = 0

    #get dir of current file 
    base_path = os.path.dirname(os.path.abspath(__file__))   
    
    #set location of file
    rawfile_txt = os.path.join(base_path, "rawoutput.txt")
    decoder_exe = os.path.join(base_path, "FaceBookMBBotDecoder.py")

    #clearing text file
    temp = open(rawfile_txt, "w", encoding="utf-8") #clears txt file 
    temp.close()                                    #closes 


    #introduction
    print("This program requires you to open Facebook Marketplace and set the positions of each post, once that is done it will automate the rest\nPress SHIFT on the location of each post and Press ESC when you are done.")
    
    #Gets Post Positions
    positionholder = get_Positions_USER(False) #stores as ([x,y],[x,y],ect)
    time.sleep(.1)

    #give user info of how to use
    print("\n\nNow we have to positions of the post saved ")
    print("run the program when ready")
    print("To start Press = To start Press - to stop")
    

    #AUTO-Post-clicker
    while True and (not exit):  
        for i in range(len(positionholder)):
            #Check if running
            if not run:
                break

            #Showing Car Num
            print("\n\nCar Number: " + str(carnum+1) +"\nPress ESC when finished ")

            #click on of the post          
            pyautogui.click(*positionholder[i])
            print("    Clicked Post: "+str(i+1)+"")

            #time to wait for link to load
            time.sleep(4)

            # Copying post
            control_Plus_Key("a")
            print("    Pressed ctrl a") 
            time.sleep(.1)
            copy_selectedText()
  
            # Pasting Post
            carnum += 1
            writeToFile(("["+str(carnum)+"]"))
            time.sleep(.1)
            clipBoardtoFile()
            print("    Copied and pasted post")

            # Copying and pasting the Link
            time.sleep(.2) 
            control_Plus_Key("l")
            time.sleep(.2) 
            copy_selectedText()
            time.sleep(.1) 
            writeToFile("\n{")
            clipBoardtoFile()
            writeToFile("}\n\n\n")
            print("    Copied and pasted link")

            #back To previous Page
            previuosPage()
            print("    Went back to main page" )

            

        run=False
    
    #Stopping Program Cleanup
    listener.stop() 
    #Running Decoder
    subprocess.run(["python", decoder_exe], check=True)

listener = keyboard.Listener(on_press=on_press, on_release=on_release)
listener.start()
main_program()



