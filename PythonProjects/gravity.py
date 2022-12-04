# Benjamin Neuenschwander
# 6/28/2022
# Purpose: Calculate the estimated gravitional force between two objects by inputting their masses and distance using Newton's Law of Universal Gravitation

# Pseudocode:
# Formula: G * ((m1 * m2) / r^2)
# Input: Ask for mass of first object (in kg)
# Input: Ask for mass of second object (in kg)
# Input: Ask for the distance between the two objects (in km)
# Output: Display the calculated gravitional force between the two objects at that point in time

G = 6.67430 # Approximate, not exact


def calculateForce(mass1: float, mass2: float, distance: float):
    return (G * ((mass1 * mass2) / pow(distance, 2)))


def main():
    while True:
        try:
            m1 = float(input("\nEnter mass of the first object (in kilograms): "))
            break
        except ValueError:
            print("That is not a numerical value.")

    while True:
        try:
            m2 = float(input("\nEnter mass of the second object (in kilograms): "))
            break
        except ValueError:
            print("That is not a numerical value.")

    while True:
        try:
            mDistance = float(input("\nEnter the distance between the two objects (in kilometers): "))
            break
        except ValueError:
            print("That is not a numerical value.")

    force = calculateForce(m1, m2, mDistance)

    print("\nThe gravitional force between these two bodies is: " + str(force) + " newtons!")


main()