from pynput import keyboard
import time, sys
import pyautogui
def find(text, location):
    global contents 
    
    global position
    if text in contents:
        position = contents.find(text, location + 1)
        print("Found:" +str(text) + " at position " + str(position))
        return position
        
    else:
        print("Not found:", text)
        return False

def writeToFile(text):
    with open("C:\\Users\\nadinesyamat\\OneDrive\\Desktop\\Programs\\Facebook Post Summarizer\\formatedOutput.txt", "a", encoding="utf-8") as file:
        file.write(text)
        
def nextInput():
    writeToFile("|")

def findEnd(text, position):
    return contents.find(text, position) + len(text)

def nextCar():
    writeToFile("\n")


class Post(year, brand):
    def __init__(curr, name, breed):
        curr.name = name
        curr.breed = breed
        
    


def main_program():
    location = 0
    
    for i in range(1, 109, 1):
        print("To start Press = To start Press - to stop")
        print(location)
        
        #get Year made
        location = (findEnd("\n20", location)+1) - 3
        writeToFile(contents[location:contents.find(" ", location)])
        print(location)
        nextInput()

        #get Brand
        writeToFile(contents[location:contents.find(" ", location)])
        location = contents.find(" ", location)
        nextInput()
        print(location)

        #get name
        writeToFile(contents[location:contents.find("\n", location)])
        location = contents.find("\n", location)-1
        nextInput()
        print(location)

        #get Price
        writeToFile(contents[contents.find('$', location):contents.find("L", location)-1])
        location = contents.find("\n", location)
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
        writeToFile(contents[location:contents.find("\n", location)])
        nextInput()
        print(location)

        #get link
        location = findEnd("{", location)
        writeToFile(contents[location:contents.find("}", location)])
        location = find("}",location)-6
        nextInput()
        print(location)

        #nextcar
        nextCar()



position = 0
with open("C:\\Users\\nadinesyamat\\OneDrive\\Desktop\\Programs\\Facebook Post Summarizer\\rawoutput.txt", "r", encoding="utf-8") as file:
    global contents
    contents = file.read()
main_program()