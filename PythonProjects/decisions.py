# Benjamin Neuenschwander
# 6/10/2022
# Purpose: Permits the user to control a turtle by allowing them choose what command and how much to move, etc.

# Pseudocode:
# Initialize the turtle
# Create an infinite loop that breaks only when the user decides to stop controlling the turtle
# Gather input from the user that permits them to control the turtle
# If statement chain that processes the command (Going to be some string splitting to get the number amounts in each command)

import string
import turtle
import time

def processInput(userTurtle: turtle.Turtle, command: string):
    global num

    if "forward" in command:
        cmdList = command.split()

        if cmdList[1]:
            num = float(cmdList[1])
            userTurtle.forward(num)

        return "Your turtle has moved forward " + str(num) + " units!"
    elif "backward" in command:
        cmdList = command.split()

        if cmdList[1]:
            num = float(cmdList[1])
            userTurtle.backward(num)

        return "Your turtle has moved backwards " + str(num) + " units!"
    elif "right" in command:
        cmdList = command.split()
        
        if cmdList[1]:
            num = float(cmdList[1])
            userTurtle.right(num)

        return "Your turtle has rotated right " + str(num) + " units!"
    elif "left" in command:
        cmdList = command.split()

        if cmdList[1]:
            num = float(cmdList[1])
            userTurtle.left(num)

        return "Your turtle has rotated left " + str(num) + " units!"
    elif "color" in command:
        cmdList = command.split()

        if cmdList[1]:
            try:
                userTurtle.color(cmdList[1])
            except turtle.TurtleGraphicsError:
                return "That was an invalid color, try again!"

        return "Your turtle has changed to the color of " + cmdList[1] + "!"
    elif "circle" in command:
        cmdList = command.split()

        if cmdList[1]:
            num = float(cmdList[1])
            userTurtle.circle(num)

        return "Your turtle has created a circle with a radius of " + str(num) + " units!"
    else:
        return "Either your input was invalid or an error has occurred. Try again."


def commandList():
    print("\n||-|| Turtle Command List ||-||")
    print("\nCommands:")
    print("forward [num]\nbackward [num]\nright [num]\nleft [num]\ncolor [str]\ncircle [num]\nfinish")
    print("The square brackets are numbers or strings you must input!")


def main():
    # Initializes the turtle
    usersTurtle = turtle.Turtle()

    while True:
        commandList()
        time.sleep(0.01)  # Stops FLVS IDLE from hiding the command list
        userCmd = input("\nEnter a command for your turtle: ")

        if userCmd.lower() == "finish":
            break

        print(processInput(usersTurtle, userCmd))

        time.sleep(2)

    print("Look at that masterpiece!")


main()
