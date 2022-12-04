# Benjamin Neuenschwander
# 6/24/2022
# Purpose: This program determines whether someone is eligible to be admitted into the "debate club"

# Pseudocode:
# Greet user and tell them this is an entrance test for the debate club
# Ask 3 questions
# Q1 = Input: Are you able to form a coherent, objective argument without bias? (y/n)
# Q2 = Input: Are you confident with speaking/arguing with others? (y/n)
# Q3 = Input: Do you have a minimum of 1-2 hours of freetime to dedicate to the club? (y/n)
# Output: If at least 2 answers were yes, announce they're eligible. If more than 1 answer is no, announce they're not eligible

import time

MAX_WRONG = 1

def checkAnswers(answers: list):
    numWrong = 0

    for ans in answers:
        if ans != "y":
            numWrong += 1

    if numWrong <= MAX_WRONG:
        return True
    else:
        return False

def main():
    answersList = []
    q1 = "Are you able to form a coherent, objective argument without bias? (y/n)"
    q2 = "Are you confident with speaking/arguing with others? (y/n)"
    q3 = "Do you have a minimum of 1-2 hours of freetime to dedicate to the club? (y/n)"

    print("Salutations! This is an elgibility exam that determines whether you are eligible to enter into the debate club.")
    time.sleep(2)
    print("The debate club is a club that is focused around debating among club members about controversial topics to non-controversial ones.")
    time.sleep(2)
    print("Your eligibility to enter the club will be displayed at the end of the exam.")
    time.sleep(2)
    print("Answer each question honestly!")
    time.sleep(2)
    print("Type 'begin' to start the exam")
    time.sleep(0.1)

    while True:
        beginInput = input("")

        if beginInput.lower() == "begin":
            break
    
    answersList.append(input("\n" + q1 + "\n").strip().lower())
    answersList.append(input("\n" + q2 + "\n").strip().lower())
    answersList.append(input("\n" + q3 + "\n").strip().lower())

    print("\nProcessing...")
    time.sleep(2.5)

    if checkAnswers(answersList):
        print("Congratulations! You are elgible to be admitted into the debate club! Talk with the club leader now!")
    else:
        print("Sadly, you did not pass the eligibilty exam. Improve the skills that were asked about in this exam and try again later!")
    
    time.sleep(1.5)
    print("\nYour answers:")
    print(q1 + "\n" + answersList[0] + "\n" + q2 + "\n" + answersList[1] + "\n" + q3 + "\n" + answersList[2] + "\n")

main()