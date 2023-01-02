import pygame
import random
import time

pygame.init()

# Font
font = pygame.font.SysFont(None, 75, bold=55, italic=14)
smallFont = pygame.font.SysFont(None, 45, italic=25)

# All Colors Setting
lightgreen = (20, 239, 173)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
black = (0, 0, 0)
white = (255, 255, 255)
yellow = (232, 239, 20)

# Screen Setting
SCREENWIDTH = 800
SCREENHEIGHT = 600
screen = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
pygame.display.set_caption("Cars By WarishaMusharraf")
FBS = 42
clock = pygame.time.Clock()

# Game  Main Images
road = pygame.image.load("GreenRoad.jpg")
car1 = pygame.image.load("car1.png")
car2 = pygame.image.load("car2.png")
car3 = pygame.image.load("car3.png")
car4 = pygame.image.load("car4.png")
WelCar = pygame.image.load("WelCar.png")
crash = pygame.image.load("crash.png")
coin = pygame.image.load("gold.png")
finish = pygame.image.load("finish.png")
cars = pygame.image.load("CArs.png")
out = pygame.image.load("out.png")
bonus = pygame.image.load("bonus.png")

pygame.display.update()


# Crash Function for Game Over

def Crash():
    Text_Setting("You Crashed", black, 230, 120)
    pygame.mixer.music.load("over.mp3")
    pygame.mixer.music.play()

    pygame.display.update()
    pygame.display.update()
    time.sleep(2)

    OutScreen()


# Text Setting Funtion

def Text_Setting(text, color, x, y):
    text = font.render(text, True, color)
    screen.blit(text, [x, y])


def Small_Text(text, color, x, y):
    text = smallFont.render(text, True, color)
    screen.blit(text, [x, y])


# Look Setting When Game will Start
def welcomeScreen():
    pygame.mixer.music.load("Racing (1).ogg")
    pygame.mixer.music.play()

    screen.blit(road, (0, 0))
    """screen.blit(car1, (500, 200))
    screen.blit(car1, (300, 500))
    screen.blit(car2, (150, 200))
    screen.blit(car2, (240, 300))"""
    screen.blit(cars, (150, 20))

    Text_Setting("Cars Game", black, 230, 70)
    Small_Text("By Warisha Musharraf", red, 270, 120)
    while True:
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                pygame.quit()
                exit()
            if events.type == pygame.KEYDOWN:
                if events.key == pygame.K_RETURN:
                    mainGame()
        pygame.display.update()
        clock.tick(60)


# How's Screen Look like When Game is Over
def OutScreen():
    screen.blit(road, (0, 0))
    screen.blit(crash, (150, 200))
    """Text_Setting("Game Over", black, 235, 80)
    Small_Text("Press Enter",blue, 250, 130)"""
    screen.blit(out, (110, 20))
    while True:
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                pygame.quit()
                exit()
            if events.type == pygame.KEYDOWN:
                if events.key == pygame.K_RETURN:
                    welcomeScreen()
        pygame.display.update()
        clock.tick(60)


# Let's Start the Main Game
def mainGame():
    pygame.mixer.music.load("WelcomeCars (2).ogg")
    pygame.mixer.music.play()

    # GameOverVariable
    gameover = False
    gameexit = False
    # For Score
    score = 0

    # Cars Variables
    carX = (SCREENWIDTH * 0.45)
    carY = (SCREENHEIGHT * 0.8)
    velocityX = 0
    velocityY = 0

    # Road Variable
    roadx = 0
    roady = 0
    RoadVelocity = 0

    # For Level
    level = 1

    # Enemy Cars Variable setting
    enemy_width = 50
    enemy_heighy = 100

    # maincar setting
    carwidth = 50
    carheight = 100

    # Points Coin Setting
    coin_height = 120
    coin_width = 50
    coinX = random.randrange(300, SCREENWIDTH - 200)
    coinY = -600

    # Finishing level  line setting
    finishingX = 200
    finishingY = -1500
    finishingVelocity = 0

    # ENEMY CARS
    RandomCar1X = random.randrange(300, SCREENWIDTH - 200)
    RandomCar1Y = -600

    carVelocity = 0
    coinVelocity = 0

    # Game Loop
    while not gameexit:
        screen.fill(white)
        screen.blit(road, (roadx, roady))
        screen.blit(road, (roadx, roady - 600))
        screen.blit(finish, (finishingX, finishingY))

        screen.blit(car1, (carX, carY))
        # RANDOM CARS GENRATE
        screen.blit(car2, (RandomCar1X, RandomCar1Y - 200))
        screen.blit(coin, (coinX, coinY - 200))
        # for Score

        Text_Setting("Score : " + str(score), black, 10, 10)
        Text_Setting("Level : " + str(level), black, 530, 10)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameexit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    velocityX += 3
                    velocityY = 0

                if event.key == pygame.K_LEFT:
                    velocityX = - 3
                    velocityY = 0
                if event.key == pygame.K_UP:
                    RoadVelocity = 4
                    carVelocity = -8
                    coinVelocity = -8
                    finishingVelocity = -4

        carX = carX + velocityX
        carY = carY + velocityY
        roady = roady + RoadVelocity
        RandomCar1Y = RandomCar1Y - carVelocity
        finishingY = finishingY - finishingVelocity

        coinY = coinY - coinVelocity

        # If Else Changing Statements for control the game
        if roady == 600:
            roady = 0
        if RandomCar1Y > 1000:
            RandomCar1Y = 0
            RandomCar1X = random.randrange(300, SCREENWIDTH - 200)
        if finishingY > 1000:
            finishingY = -2000
        if carY == finishingY:
            pygame.mixer.music.load("background.ogg")
            pygame.mixer.music.play()

            level += 1
            score += 10
        if carY == finishingY or carY < finishingY:
            screen.blit(bonus, (150, 10))

        # Car Crash Settings

        if carY + 220 < RandomCar1Y + enemy_heighy:
            if carX > RandomCar1X and carX < RandomCar1X + enemy_width or carX + carwidth > RandomCar1X and carX + carwidth < RandomCar1X + enemy_width:
                Crash()
        if carX > 570 or carX < 0:
            Crash()

        # Points Setting

        if carY + 190 < coinY + coin_height:
            if carX > coinX and carX < coinX + coin_width or carX + 20 + coin_width > coinX and carX + 20 + carwidth < coinX + coin_width:
                score += 1
                pygame.mixer.music.load("score.mp3")
                pygame.mixer.music.play()
                coinY = 0
                coinX = random.randrange(300, SCREENWIDTH - 200)

        pygame.display.update()
        clock.tick(FBS)
    pygame.quit()
    exit()


welcomeScreen()
mainGame()
