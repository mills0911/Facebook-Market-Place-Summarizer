from pynput import keyboard
import time, sys
import pyautogui
import os

def find(text, location):
    global contents 
    #find text starting from location 
    position = contents.find(text, location + 1)
    if position == -1:
        print(str(text)+"NOT FOUND")
        return location
    else:
        print("Found:" +str(text) + " at position " + str(position))
        return position
        

def writeToFile(text):
    global formatfile
    with open(formatfile, "a", encoding="utf-8") as file:
        file.write(text)
        
def nextInput():
    writeToFile("|")

def findEnd(text, position):
    return contents.find(text, position) + len(text)

def nextCar():
    writeToFile("\n")

"""""
class Post(year, brand):
    def __init__(curr, name, breed):
        curr.name = name
        curr.breed = breed
        """""
    


def main_program():
    location = 0 #before text location
    locationend = 0 #after text location
    global rawfile, formatfile
    
    #get dir of current file 
    base_path = os.path.dirname(os.path.abspath(__file__))   
    
    #set location of file
    rawfile = os.path.join(base_path, "rawoutput.txt")
    formatfile = os.path.join(base_path, "formatedOutput.txt")

    #get raw file
    with open(rawfile, "r", encoding="utf-8") as file:
        global contents
        contents = file.read()
    i=1
    while (contents.find(f'[{i}]', location) != -1):
        location+=1
        print(location)
        
        #get Year made
        location = contents.find(']', location)+1
        locationend = contents.find(" ", location)
        writeToFile(contents[location:locationend])
        print(location)
        nextInput()
        

        #get Brand
        location = contents.find(" ", location)+1
        locationend = contents.find(" ", location)
        writeToFile(contents[location:locationend])
        nextInput()
        print(location)

        #get name
        location = locationend+1
        writeToFile(contents[location:contents.find("\n", location)])
        location = contents.find("\n", location)-1
        nextInput()
        print(location)

        #get Price
        location = contents.find('$', location)
        locationend = contents.find("\n", location)
        writeToFile(contents[location:locationend])
        nextInput()
        print(location)

        #get Mileage
        location = findEnd("Driven ", location)
        writeToFile(contents[location:contents.find(" ", location)])
        nextInput() 
        print(location)

        #get Exterior color
        location = findEnd("Exterior color: ", location)
        writeToFile(contents[location:contents.find(" ", location)])
        nextInput()
        print(location)

        #get Interior color
        location = findEnd("Interior color:", location)+1
        locationend = contents.find("\n", location)
        writeToFile(contents[location:locationend])
        nextInput()
        print(location)

        #get link
        location = findEnd("{", location)
        locationend =contents.find("}", location)
        writeToFile(contents[location:locationend])
        
        nextInput()
        print(location)

        #nextcar
        nextCar()
        i+=1



position = 0


main_program()
