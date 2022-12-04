# Benjamin Neuenschwander
# 6/24/2022
# Purpose: Encodes a quote into ASCII and asks the user to try and solve the quote

# Pseudocode:
# Introduction to program
# Display the random encoded message in ASCII
# Input: Ask the user if they'd like to solve it letter by letter
# If yes, loop through each character in the list and have the user try and solve it (provide an ascii table) link: ("https://upload.wikimedia.org/wikipedia/commons/1/1b/ASCII-Table-wide.svg")
# If no, just display the message

import random
import time

SECRET_QUOTES = ["Success is a lousy teacher. It seduces smart people into thinking they can’t lose. - Bill Gates", "You can't just ask customers what they want and then try to give that to them. By the time you get it built, they'll want something new. - Steve Jobs", "The only source of knowledge is experience. - Albert Einstein", "Not only is the Universe stranger than we think, it is stranger than we can think. - Werner Heisenberg"]

def createAsciiTable(msg: str):
    tempTable = []
    
    for c in msg:
        tempTable.append(ord(c))

    return tempTable

def decodeQuote(msgTable: list):
    gaveUp = False
    currentMsg = ""

    print("You've chosen to try and decode the message! You'll need this ASCII table to perform the conversions: https://upload.wikimedia.org/wikipedia/commons/1/1b/ASCII-Table-wide.svg \nGood luck!")
    print("Type 'giveup' at any time to quit the translation process.")
    time.sleep(2)

    while True:
        for num in msgTable:
            while True:
                userTranslation = input("\nConvert " + str(num) + " from ASCII: ")

                if userTranslation == chr(num): # User translated correctly
                    currentMsg += userTranslation
                    print("That was correct! Here is the message so far:\n" + currentMsg)
                    time.sleep(.75)
                    break
                elif userTranslation == "giveup":
                    gaveUp = True
                    break
                else:
                    print("Hmm, that wasn't the correct character. Try again.")
                    time.sleep(.75)

            if gaveUp:
                break
        
        if gaveUp:
            translatedMsg = ""
            for num in msgTable:
                translatedMsg += chr(num)

            print("Sadly, you've given up. Here is the translated message:\n" + translatedMsg)
            break
        else:
            print("Congratulations! You decoded the message! Here is the complete message:\n" + currentMsg)
            break

def main():
    chosenQuote = random.choice(SECRET_QUOTES)
    asciiTable = createAsciiTable(chosenQuote)
    formattedMsg = ""

    for num in asciiTable:
        formattedMsg += str(num) + " "

    print("Greetings! This program will have you try to decode a random famous quote that has been converted into ASCII!\nAn ASCII table will be provided if you opt to try and translate the quote. Otherwise, the translated quote will be displayed.")
    time.sleep(3.5)
    print("Here is the encoded message: \n" + formattedMsg)
    time.sleep(1.5)
    ynInput = input("Would you like to try and decode the message? (y/n)\n").strip().lower()

    if ynInput == "y":
        decodeQuote(asciiTable)
    else:
        print("That's ok, here is the translated quote:\n" + chosenQuote)

main()