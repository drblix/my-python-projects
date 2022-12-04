# Benjamin Neuenschwander
# 6/13/2022
# Purpose: A little mini-game that has the player guess a number between 1-100; there are 5 correct numbers that
# the player can guess. The player has 3 tries before the numbers are scrambled again.

# Pseudocode:
# Pick 5 numbers between 1-100, repicking any that are already chosen and adding them to a list
# Input: Have the player try to guess my 5 favorite numbers, losing a life each time a guess is incorrect
# Output: If the guessed number is correct, print saying the player won! If the player loses all their lives, new numbers will be
# created and added to the list

import random
import string
import time

def parseToInt(text: string):
    try:
        return int(text)
    except ValueError:
        return None

def main():
    correctNumbers = []
    livesAmount = 5
    playerWon = False

    print("Welcome to the my favorite number guessing game 2000!")
    time.sleep(1.5)
    print("In this game you will attempt to guess 1 of the 5 chosen favorite numbers in the range of 1-100.")
    time.sleep(1.5)
    print("You have 5 lives for each guessing round!")
    time.sleep(1.5)
    print("\nMy favorite numbers will now be chosen!")

    time.sleep(0.5)

    while True:
        correctNumbers = [] # correctNumbers.clear() (.clear isn't supported in Python 2, had to reintialize the list instead)
        for x in range(5):
            newNum = random.randint(1, 100)
            for x in correctNumbers:
                if x == newNum:
                    newNum = random.randint(1, 100)

        correctNumbers.append(newNum)

        print("\nMy favorite numbers have changed!")

        for x in range(livesAmount):
            playerNum = None
            while playerNum == None:
                playerNum = parseToInt(input("\nPick an integer between 1 and 100: "))
        
            for x in correctNumbers:
                if x == playerNum:
                    playerWon = True
                    print("\nCongratulations, you guessed a number correctly! \n You win!")
                    break

            if not playerWon:
                print("\nHmmm, that wasn't a correct number...")
            else:
                break
            
            time.sleep(0.25) # Prevents FLVS IDLE from hiding text
        
        if playerWon:
            break


main()