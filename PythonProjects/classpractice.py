import math

class Book:
    def __init__(self, name: str, genre: str, pages: int):
        self.name = name
        self.genre = genre
        self.pages = pages

    def __str__(self):
        return f"Title = {self.name}; Genre = {self.genre}; Page amount = {self.pages}"
    
    def findMidpoint(self):
        print("The midpoint of this book is: " + str(math.floor(self.pages / 2)))

harryPotter = Book("Harry Potter: The Sorcerer's Stone", "Fantasy", 99)
print(harryPotter)
del harryPotter

orwell1984 = Book("1984", "Dystopian", 286)
print(orwell1984)
orwell1984.findMidpoint()
del orwell1984