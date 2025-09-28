
import time, sys
import pyautogui
import pyperclip
import os
from pynput import keyboard
from pynput.keyboard import Key, Controller as KeyboardController
from pynput.mouse import Button, Controller as MouseController
keyboard_controller  = KeyboardController()
mouse_controller = MouseController()

carnum = 0

#stop and start button
def on_press(key):
    global run
    try:
        if key.char == '=':
            run = True
        if key.char == '-':
            run = False
    except AttributeError:
        pass



# Define postionholder as a list of lists before using it
postionholder = [[170, 620], [533, 633], [929, 625], [143, 1180], [530, 1183], [930, 1180]]

def post_clicker(i):
    pyautogui.click(*postionholder[i])
    time.sleep(4)


def copy():
    keyboard_controller.press(Key.ctrl)
    keyboard_controller.tap("c")
    keyboard_controller.release(Key.ctrl)


def writeToFile(text):
    with open("rawoutput.txt", "a", encoding="utf-8") as file:
        file.write(text)

def clipBoardtoFile():
    text = pyperclip.paste()
    writeToFile(text)

def main_program():
    print("To start Press = To start Press - to stop")
    global run
    global carnum
    print("running ")


    while True:
        if run:
            print("running run loop")
            for i in range (6):
                if run:
                    #click on of the post
                    post_clicker(i)
                    print("clicked post")

                    # Ctrl A
                    keyboard_controller.press(Key.ctrl)
                    keyboard_controller.tap("a")
                    keyboard_controller.release(Key.ctrl)
                    print("pressed ctrl a") 
                    time.sleep(.1)

                    # Copying and pasting the post
                    copy()
                    time.sleep(.1)
                    carnum += 1
                    writeToFile("["+str(carnum)+"]")
                    clipBoardtoFile()
                    time.sleep(.1)
                    print("copied and pasted post")

                    # Copying and pasting the Link
                    pyautogui.click(280,100)
                    copy()
                    time.sleep(.1) 
                    writeToFile("\n{")
                    clipBoardtoFile()
                    writeToFile("}\n\n\n")

                    time.sleep(.1)
                    print("copied and pasted link")

                    # Going back to main page 
                    time.sleep(1)
                    pyautogui.click(30,96)
                    time.sleep(.1)
                    print("went back to main page" + str(i))
            run = False



        time.sleep(.1)
        
listener = keyboard.Listener(on_press=on_press) 
listener.start()
run = False
main_program()




