# Benjamin Neuenschwander
# 6/26/2022
# Purpose: Demonstrates the creation of a 'Supervillian' class along with the properties that can be modified, as well as method that can be called

# Pseudocode:
# Create supervillian via supervillian class
# Supervillian will be Dr. Octopus with a starting strength and evil of 5
# Have a momentary run-in with Spiderman
# Gain both strength and evil from the encounter
# Display stats at the end

import time

MAX_STAT = 10
MIN_STAT = 1

class Supervillain:
    def __init__(self, name: str, strength: int, evilAmnt: int):
        Supervillain.name = name
        Supervillain.strength = strength
        Supervillain.evilAmnt = evilAmnt
        self.strength = max(min(self.strength, MAX_STAT), MIN_STAT) # Clamps between 1-10
        self.evilAmnt = max(min(self.evilAmnt, MAX_STAT), MIN_STAT) # Clamps between 1-10

    def displayStats(self):
        if not self.name.endswith("s"):
            print("\nThese are " + self.name + "'s stats:")
        else:
            print("\nThese are " + self.name + "' stats:")

        print("Strength (1-10): " + str(self.strength) + "\nEvil amount (1-10): " + str(self.evilAmnt))

    def changeStrength(self, amnt: int):
        self.strength += amnt
        self.strength = max(min(self.strength, MAX_STAT), MIN_STAT) # Clamps between 1-10
        print("\nNew strength amount is: " + str(self.strength))

    def changeEvil(self, amnt: int):
        self.evilAmnt += amnt
        self.evilAmnt = max(min(self.evilAmnt, MAX_STAT), MIN_STAT)
        print("\nNew evil amount is: " + str(self.evilAmnt))


def main():
    drOctopus = Supervillain("Dr. Octopus", 5, 5)
    print("This is a story about a supervillain named " + drOctopus.name + "! May of heard that name a few times.")
    time.sleep(3)
    print("While strolling through the streets of New York, " + drOctopus.name + " runs into Peter Parker! (Spiderman)")
    time.sleep(3)
    print("The two have a momentary battle in the middle of the street, with the result coming to a draw.")
    time.sleep(2)
    print(drOctopus.name + " is damaged in the fight, but gains a more prevalent lust for Spiderman's defeat in the process: this leads to him increasing in both his strength and evil amount!")
    time.sleep(3.5)
    drOctopus.changeStrength(2)
    drOctopus.changeEvil(3)
    drOctopus.displayStats()

main()