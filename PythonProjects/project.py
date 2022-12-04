# Benjamin Neuenschwander
# 5/25/2022
# Purpose: Allows the user to select from a variety of menu options, create a meal, and choose a tip rate. At the end,
# the subtotal is calculated and the entire meal is displayed.

# Pseudocode:
# Welcome user to the online ordering service
# Input: Ask for name on the order
# Input: Ask if it's take-out order or dine-in
# Output: Display all information entered
# Input: Ask if all info is correct
# If user types "yes", the program continues, otherwise, program loops back.
# Ordering section:
# Input: Ask for appetizer order (displays choices alongside it)
# Input: Ask for entrée order (displays choices alongside it)
# Input: Ask for drink order (displays choices alongside it)
# Input: Ask for dessert order (displays choices alongside it)
# Input: Ask for tip percent
# Output: Display entire order, including name etc.

import time

def itemInList(item: str, menuList: list):
    # Loops through the inputted list and checks and returns true if the supplied item is in the list
    for i in menuList:
        if item.lower() == i.lower():
            return True

    return False


def getItemPrice(item: str):
    # I hate this but it works
    if item.lower() == "cheese bread":
        return 4.29
    elif item.lower() == "bread sticks":
        return 4.99
    elif item.lower() == "chips and salsa":
        return 4.99
    elif item.lower() == "hamburger":
        return 3.99
    elif item.lower() == "hotdog":
        return 2.99
    elif item.lower() == "fried shrimp":
        return 5.49
    elif item.lower() == "wings":
        return 6.99
    elif item.lower() == "tomato soup":
        return 3.49
    elif item.lower() == "coca-cola":
        return 1.99
    elif item.lower() == "water":
        return 0.99
    elif item.lower() == "iced tea":
        return 1.49
    elif item.lower() == "alcohol":
        return 2.49
    elif item.lower() == "lemonade":
        return 1.49
    elif item.lower() == "ice cream":
        return 2.49
    elif item.lower() == "cheesecake":
        return 4.49
    elif item.lower() == "chocolate cake":
        return 3.99
    elif item.lower() == "sundae":
        return 3.99
    elif item.lower() == "frozen yogurt":
        return 1.99


def main():
    appetizers = ["Cheese bread", "Bread sticks", "Chips and salsa"]
    entrees = ["Hamburger", "Hotdog", "Fried shrimp", "Wings", "Tomato soup"]
    drinks = ["Coca-Cola", "Water", "Iced tea", "Alcohol", "Lemonade"]
    desserts = ["Ice cream", "Cheesecake", "Chocolate cake", "Sundae", "Frozen yogurt"]

    print("Welcome to Big Ben's Restaurant online ordering service! This process will guide you on creating an online order, either for take-out or dine-in.")

    time.sleep(1)

    while True:
        orderName = input("Enter name to be put on the order: ")
        time.sleep(0.5)

        while True:
            orderType = input("Enter whether this is a take-out or dine-in order (type \"take-out\" or \"dine-in\": ")

            if orderType.lower() == "take-out" or orderType.lower() == "dine-in":
                break
            else:
                print("Incorrect order type! Try again.")

        print("\nOrder Name: " + orderName)
        print("Order Type: " + orderType)

        time.sleep(0.5)

        validationReply = input("\nIs all this information correct? (type \"yes\" or \"no\") \n")

        if validationReply.lower() == "yes":
            break

    while True:
        print("")
        for i in appetizers:
            print(str(i) + ": " + "$" + str(getItemPrice(str(i))))

        time.sleep(1)

        chosenAppetizer = input("Select an appetizer to add to your order: ")

        if itemInList(chosenAppetizer, appetizers):
            appPrice = getItemPrice(chosenAppetizer)
            break
        else:
            print("Chosen item is not in the list. Try again.")

    while True:
        print("")
        for i in entrees:
            print(str(i) + ": " + "$" + str(getItemPrice(str(i))))

        time.sleep(1)

        chosenEntree = input("Select an entree to add to your order: ")

        if itemInList(chosenEntree, entrees):
            entreePrice = getItemPrice(chosenEntree)
            break
        else:
            print("Chosen item is not in the list. Try again.")

    while True:
        print("")
        for i in drinks:
            print(str(i) + ": " + "$" + str(getItemPrice(str(i))))

        time.sleep(1)

        chosenDrink = input("Select a drink to add to your order: ")

        if itemInList(chosenDrink, drinks):
            drinkPrice = getItemPrice(chosenDrink)
            break
        else:
            print("Chosen item is not in the list. Try again.")

    while True:
        print("")
        for i in desserts:
            print(str(i) + ": " + "$" + str(getItemPrice(str(i))))

        time.sleep(1)

        chosenDessert = input("Select an appetizer to add to your order: ")

        if itemInList(chosenDessert, desserts):
            dessertPrice = getItemPrice(chosenDessert)
            break
        else:
            print("Chosen item is not in the list. Try again.")

    while True:
        time.sleep(0.5)
        try:
            tipAmount = float(input("\nChoose an amount to tip (amount must be between 0.15 & 0.75): "))
            if 0.15 < tipAmount < 0.75:
                break
        except ValueError:
            print("Invalid tip amount!")

    subTotal = appPrice + entreePrice + drinkPrice + dessertPrice
    total = round(subTotal + (subTotal * tipAmount) + (subTotal * 0.065), 2)

    time.sleep(1.5)

    print("\nOrder summary:")
    print("\nName on order: " + orderName.capitalize())
    print("Item       Price")
    print(chosenAppetizer.capitalize() + "       " + "$" + str(appPrice))
    print(chosenEntree.capitalize() + "       " + "$" + str(entreePrice))
    print(chosenDrink.capitalize() + "       " + "$" + str(drinkPrice))
    print(chosenDessert.capitalize() + "       " + "$" + str(dessertPrice))
    print("--------------------------------")
    print("Order Type:        " + orderType.capitalize())
    print("Subtotal:        " + "$" + str(subTotal))
    print("Tax:        " + "$" + str(round(subTotal * 0.065, 2)))
    print("Tip:        " + "$" + str(round(subTotal * tipAmount, 2)))
    print("Total:        " + "$" + str(total))


main()
