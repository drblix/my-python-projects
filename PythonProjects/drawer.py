# Benjamin Neuenschwander
# 6/6/2022
# Purpose: Draws a bunch of small buildings (amount inputted by player) and then a sun

# Pseudocode:
# Input: Get num of buildings to make
# Compute how to create these buildings
# Draw the buildings
# Draw a sun
# Output: Display the image that was created

import random
import turtle
import time


def drawWindow(tur, x, y, color):
    tur.goto(x, y)
    tur.pendown()
    tur.color(color)
    tur.begin_fill()

    for i in range(4):
        tur.forward(10)
        tur.left(90)

    tur.end_fill()
    tur.penup()


def drawBuilding(tur, x, y, height, color, windowcolor):
    tur.goto(x, y)
    tur.pendown()
    tur.color(color)
    tur.begin_fill()

    tur.forward(50)
    tur.left(90)
    tur.forward(height)
    tur.left(90)
    tur.forward(50)
    tur.left(90)
    tur.forward(height)

    tur.end_fill()

    # Some random things I put together using algebra
    # I dunno why it works, but it does
    l1 = height / 4
    l2 = height / (20 / 11)
    l3 = height / (20 / 17)

    drawWindow(tur, x + 30, y + l1, windowcolor)
    drawWindow(tur, x + 10, y + l1, windowcolor)
    drawWindow(tur, x + 30, y + l2, windowcolor)
    drawWindow(tur, x + 10, y + l2, windowcolor)
    drawWindow(tur, x + 30, y + l3, windowcolor)
    drawWindow(tur, x + 10, y + l3, windowcolor)
    tur.left(90)  # Resets orientation otherwise building will be drawn rotated


def drawSun(tur, x, y, color):
    tur.goto(x, y)
    tur.color(color)
    tur.begin_fill()
    tur.circle(45)
    tur.end_fill()


def main():
    garry = turtle.Turtle()
    garry.penup()

    while True:
        try:
            numBuildings = int(input("Enter how many buildings you want created (max 20): "))
            break
        except ValueError:
            print("Not an integer")
            time.sleep(0.2)

    if numBuildings > 20:
        numBuildings = 20

    baseValue = int(((numBuildings * 50) / 2))

    start = -baseValue
    end = baseValue

    garry.speed(10)

    for x in range(start, end, 50):
        drawBuilding(garry, x, 0, random.randint(60, 230), "gray", "light blue")

    drawSun(garry, 250, 250, "yellow")
    print("What a cute little city with " + str(numBuildings) + " building(s) :)")
    time.sleep(3)


main()
