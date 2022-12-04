# Benjamin Neuenschwander
# 6/1/2022
# The Amazing Polygon creator 5000
# Purpose: This tool aims to create a polygon with the provided number of sides that the user inputs

# Pseudocode:
# Input: Ask how many sides user wants for their shape
# Calculate the total angle measure of the requested polygon
# Find each angle measure of the requested polygon
# Create a turtle and loop the amount of sides that were requested
# Output: Display the polygon that was created

import random
import time
import turtle

colors = ["red", "blue", "green", "purple", "pink", "lime"]


def getEachAngle(sides: int):
    totalMeasures = (sides - 2) * 180  # Calculates the sum of all angle measures in the polygon
    eachAngle = totalMeasures / sides  # Calculates the value of each angle in the polygon
    return eachAngle


def main():
    while True:
        try:
            totalSides = int(input("Input the amount of sides you want on your shape: "))
            break
        except ValueError:
            print("Not an integer, try again!")
            time.sleep(0.1)

    eachAngle = getEachAngle(totalSides)

    timothy = turtle.Turtle()
    timothy.color(random.choice(colors))  # Choice random color from array
    timothy.begin_fill()

    for x in range(totalSides):
        timothy.forward(25)
        timothy.right(180 - eachAngle)

    timothy.end_fill()
    print("I call this one a " + str(totalSides) + "-sided shape!")
    time.sleep(3)


main()
