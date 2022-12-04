# Benjamin Neuenschwander
# 5/22/2022
# Purpose: Allows the user to have a pre-scripted conversation with a computer, like a chatbot.

# Pseudocode:
# Computer gives an introduction
# Input: Computer asks for user's name
# Output: Computer greets the user with the inputted name
# Computer says it can do math
# Input: Computer asks what number should 8 be multiplied by
# Output: Computer displays the result of the inputted number * 8
# Input: Computer asks if you can find the word inside of crate
# Output: If user inputted "rat", the computer says good job! Otherwise, computer prints the word that was in "crate"
# Computer says goodbye and wishes the user well

import time


def main():
    print("Salutations! I'm your computer, and well, I'm talking to you! :)")

    time.sleep(1.5)

    name = input("So, what's your name, user? Input name: ")
    print("Wow! Cool name, " + name + "!")

    time.sleep(1)

    print("Did you know I can perform math at lightning-fast speeds?")

    num = None

    # While loop just stops the user from inputting a non-number and causing an error
    while True:
        num = input("I'll prove it! What number should I multiply 8 by? It can be anything! Input number: ")
        try:
            num = float(num)
            break
        except ValueError:
            print("Hey.. It must be a number! Try again :/")
            time.sleep(1)

    result = float(num) * 8
    print(str(result) + "! Boom, I told you.")

    time.sleep(1.5)

    guessingWord = "crate"
    word = input("Hey, can you find the word that's inside of \"crate\"? I'm curious if you can find it! Input word: ")

    if word.lower() == "rat":
        print("Look at you! You found the word! :)")
    else:
        print("Nice try! The word was \"" + guessingWord[1:4] + "\"! Do you see it now? :)")

    time.sleep(1)

    print("Whelp! It was fun talking to you, " + name + "! I hope you speak to you again soon, and perhaps when I have more interesting, non-preprogrammed responses! Ciao!")


main()
