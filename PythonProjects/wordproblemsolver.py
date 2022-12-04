# Benjamin Neuenschwander
# 5/24/2022
# Purpose: A word problem solver that has the user manually input the values into the equation

# Pseudocode:
# Word problem is displayed, deals with calculating the volume and surface area of a sphere
# Sphere formulas = Surface area: 4πr^2 || Volume: (4.0/3.0) πr^3
# Ask for user's help
# Input: Ask for radius of sphere
# Output: Display surface area and volume of sphere

import math
import random
import time


def calculateVolume(radius: float):
    volume = (4.0 / 3.0) * (math.pi * math.pow(radius, 3))  # Applies sphere volume formula
    volume = round(volume, 2)  # Rounds to the 2nd decimal place
    return str(volume)  # Returns result as a string


def calculateSA(radius: float):
    surfaceArea = 4 * (math.pi * math.pow(radius, 2))  # Applies sphere surface area formula
    surfaceArea = round(surfaceArea, 2)  # Rounds to the 2nd decimal place
    return str(surfaceArea)  # Returns result as a string


def main():
    diameter: int = random.randint(4, 18)  # Selects diameter of the bowling ball randomly (range from 4 to 18)

    print("Devon is measuring bowling balls in order to find the most optimal ball for his upcoming bowling tournament.")
    time.sleep(2)
    print("Currently, Devon has found a ball with a diameter of " + str(diameter) + " units, he needs to find the surface area and volume of the bowling ball.")
    time.sleep(1.5)

    # While loop to prevent a ValueError if user inputs a non-numerical value
    while True:
        try:
            radius = float(input("\nHe needs your help! Find the radius of the bowling ball with the given information: "))

            if radius != float(diameter) / 2:  # If input is not equal to the diameter divided by 2, repeat
                print("Hmm, that's not the correct radius. Try again. Remember to utilize the information on the diameter!")
                time.sleep(2)
            else:
                break

        except ValueError:
            print("Hmm, that's not a numerical value. Try again.")
            time.sleep(2)

    volume: str = calculateVolume(radius)  # Gets value from function
    surfaceArea: str = calculateSA(radius)  # Gets value from function

    print("Great job! Devon calculated the volume of the bowling ball and ended up with approximately " + volume + " units cubed.")
    time.sleep(1)
    print("Devon also calculated the surface area of the bowling ball and ended up with approximately " + surfaceArea + " units squared.")
    time.sleep(1)
    print("\nThanks to your help, Devon has chosen this bowling ball as his one to use for the tournament!")
    input()  # Stops console window from being closed quickly


main()
