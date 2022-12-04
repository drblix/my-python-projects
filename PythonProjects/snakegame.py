# Benjamin Neuenschwander
# 6/29/2022
# Purpose: Play a simple game of snake

# Credit to pygame.org for a quick refresher of how the pygame module works :)

# Requirements:
# Maximum of Python 3.9, minimum of Python 3.0
# Must not be used in the FLVS IDLE
# Must be run with Python interpreter versions as stated above
# Pygame module required (instructions on https://www.pygame.org/wiki/GettingStarted)

# Pseudocode:
# Fetch pygame module (must download first)
# Initialize game window and needed constants
# Create snake body and head using int vector 2's
# Create display score function that calls every frame displaying score
# Create game over function that calls when snake collides with edge of screen or itself and quits game
# Create main function that loops constantly (where rendering and drawing will be done)

import pygame
import time
import random

# basically the FPS of the game; Example: 20 = 20 frames per second
# recommended: 15-25
SNAKE_SPEED = 15
FONT_AA = False # anti-aliasing
GAME_FONT = "comic sans" # because why not

# Window size parameters
WINDOW_X = 500 # default of 500, can be changed as needed
WINDOW_Y = 500 # default of 500, can be changed as needed

# Pre-defined colors
green = pygame.Color(0, 255, 0)
red = pygame.Color(255, 0, 0)
black = pygame.Color(0, 0, 0)

# Initialization
pygame.init()

# Creating window
pygame.display.set_caption("Snake Game by Benjamin Neuenschwander")
gameWindow = pygame.display.set_mode((WINDOW_X, WINDOW_Y))

# Handling FPS via pygame clock
fps = pygame.time.Clock()

# Creating snake body
snakePos = [100, 50]
snakeBody = [
    [100, 50],
    [90, 50],
    [80, 50],
    [70, 50]
]

# Fruit set up
fruitPos = [
    random.randrange(1, (WINDOW_X // 10)) * 10,
    random.randrange(1, (WINDOW_Y // 10)) * 10,
]

fruitSpawned = True

# Snake direction initialization
snakeDirection = "RIGHT"

# Starting score
score = 0

def displayScore(color, size):
    # Create font obj
    scoreFont = pygame.font.SysFont(GAME_FONT, size)
    # Renders font obj
    scoreSurface = scoreFont.render("Score: " + str(score), FONT_AA, color)
    # Gets render rect
    scoreRect = scoreSurface.get_rect()
    # Renders text to game window
    gameWindow.blit(scoreSurface, scoreRect)


def gameOver():
    global score
    # Creates font obj
    gameOverFont = pygame.font.SysFont(GAME_FONT, 50)
    scoreFont = pygame.font.SysFont(GAME_FONT, 25)
    # Renders font obj
    gameOverSurface = gameOverFont.render("Game Over", FONT_AA, red)
    scoreSurface = scoreFont.render("Your finishing score was: " + str(score), FONT_AA, red)
    # Creates rect
    gameOverRect = gameOverSurface.get_rect()
    scoreRect = scoreSurface.get_rect()
    # Sets position of text
    gameOverRect.midtop = [WINDOW_X / 2, WINDOW_Y / 3]
    scoreRect.midtop = [gameOverRect.midtop[0], gameOverRect.midtop[1] + 60]
    # Renders text to game window
    gameWindow.blit(gameOverSurface, gameOverRect)
    gameWindow.blit(scoreSurface, scoreRect)

    pygame.display.flip()

    time.sleep(3.5)

    # Quits program and deactivates module
    pygame.quit()
    quit()


def main():
    while True:
        # Global keyword prevents the "local variable referenced before assignment" error
        global snakeDirection
        global fruitPos
        global fruitSpawned
        global score

        # Loop for checking events and key presses
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and snakeDirection != "DOWN":
                    snakeDirection = "UP"
                elif event.key == pygame.K_RIGHT and snakeDirection != "LEFT":
                    snakeDirection = "RIGHT"
                elif event.key == pygame.K_DOWN and snakeDirection != "UP":
                    snakeDirection = "DOWN"
                elif event.key == pygame.K_LEFT and snakeDirection != "RIGHT":
                    snakeDirection = "LEFT"
            elif event.type == pygame.QUIT:
                # Ends game early
                pygame.quit()
                quit()

        # Snake movement
        if snakeDirection == "UP":
            snakePos[1] -= 10
        elif snakeDirection == "RIGHT":
            snakePos[0] += 10
        elif snakeDirection == "DOWN":
            snakePos[1] += 10
        elif snakeDirection == "LEFT":
            snakePos[0] -= 10

        # Grows snake
        snakeBody.insert(0, list(snakePos))

        if snakePos[0] == fruitPos[0] and snakePos[1] == fruitPos[1]:
            score += 10
            fruitSpawned = False
        else:
            snakeBody.pop()

        # Spawning fruit if no fruit
        if not fruitSpawned:
            fruitPos = [
                random.randrange(1, (WINDOW_X // 10)) * 10,
                random.randrange(1, (WINDOW_Y // 10)) * 10,
            ]

        fruitSpawned = True
        gameWindow.fill(black)

        # Draws snake body
        for position in snakeBody:
            pygame.draw.rect(gameWindow, green, pygame.Rect(position[0], position[1], 10, 10))

        # Draws fruit
        pygame.draw.rect(gameWindow, red, pygame.Rect(fruitPos[0], fruitPos[1], 10, 10))

        # Game over checking
        if snakePos[0] < 0 or snakePos[0] > WINDOW_X - 10:
            gameOver()
        elif snakePos[1] < 0 or snakePos[1] > WINDOW_Y - 10:
            gameOver()

        # Check if head hits snake body
        # The '1:' prevents head from colliding with itself
        for snakeBlock in snakeBody[1:]:
            if snakePos[0] == snakeBlock[0] and snakePos[1] == snakeBlock[1]:
                gameOver()

        # Show score
        displayScore(red, 20)

        pygame.display.update()
        fps.tick(SNAKE_SPEED)

# Starts game
main()