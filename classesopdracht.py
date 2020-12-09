from time import sleep
import sys, os, time, pygame
clear = lambda: os.system('cls')
from pygame._sdl2 import *
from pygame import mixer
from pygame.locals import *
import random

mixer.init(devicename='Headset Earphone (HyperX Virtual Surround Sound)') #run de audio.py in cmd voor uw huidige audiodevice

def write(text, speed):
    for x in text:
        print(x, end='')
        sys.stdout.flush()
        sound = mixer.Sound("blop.mp3")
        sound.play()
        sound.set_volume(0.5)
        sleep(speed)
    print("\n")


pygame.init()

KEYS_DOWN = []
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_SIZE = [SCREEN_WIDTH, SCREEN_HEIGHT]
SCREEN = pygame.display.set_mode(SCREEN_SIZE)

CLOCK = pygame.time.Clock()
FPS = 30

playerSprite = pygame.image.load("kangaroo.png")
playerRect = playerSprite.get_rect()
playerSpeed = 5

BG_COLOUR = [0, 0, 0]
game = True

class rogerTheKangaroo :
    def __init__(self):
        write("Roger the Kangaroo has arrived!", 0.08)
    #Base stats
    _strength = 80
    _lifepoints = 150
    _speed = 60
    _invSpace = 20
    _magicPower = 30
    _physicalPower = 90
    _points = 100

def ultraPunch():
    write("Roger The Kangaroo used his trump card: Ultra Punch!", 0.08)
    time.sleep(2)
    num2 = 0
    num2 = random.randrange(1, 11)
    if num2 == 10:
        write("Roger The Kangaroo's Ultra Punch was a critical hit! It's damage doubled to 250!")
        enboss0._lifepoints -= 250
        rogerTheKangaroo._points -= 30
        write("Ultra punch consumed 30 points...", 0.08)
        time.sleep(0.5)
        write("You have ", rogerTheKangaroo._points + "left...", 0.08)

    else:
        write("Roger The Kangaroo's Ultra Punch was a solid hit! It did 125 damage!")
        rogerTheKangaroo._points -=30
        endboss0._lifepoints -= 125
        write("Ultra punch consumed 30 points...", 0.08)
        time.sleep(0.5)
        write("You have ", rogerTheKangaroo._points + "left...", 0.08)

def upperCut():
    write("Roger used an upperCut...", 0.08)
    num0 = 0
    num0 = random.randrange(1,11)
    if num0 == 1:
        write("Roger landed a critical hit! It inflicted 100 damage...", 0.08)
        Endboss._lifepoints -= 100
        rogerTheKangaroo._points -=10
        write("Upper Cut consumed 10 points...", 0.08)
        time.sleep(0.5)
        write("You have ", rogerTheKangaroo._points + "left...", 0.08)
    else:
        write("Roger landed a solid hit! It inflicted 50 damage...", 0.08)
        Endboss._lifepoints -= 50
        write("Upper Cut consumed 10 points...", 0.08)
        time.sleep(0.5)
        write("You have ", rogerTheKangaroo._points + "left...", 0.08)



class Endboss(rogerTheKangaroo) :
    _strength = 150
    _lifepoints = 1000
    _smash = 100

def smash() :
    write("The Endboss used it's powerfull fist to SMASH!", 0.04)
    if _smash != 0:
        if KEYDOWN != K_RIGHT or KEYDOWN != K_LEFT:
            character0._lifepoints =- 25
            Endboss._smash -= 25
    else:
        write("The endboss tried to use SMASH! Yet it's taken a toll on it's stamina...", 0.08)
        time.sleep(0.5)
        write("You have 20 seconds of time before the endboss can fight again...", 0.08)
        time.sleep(20)
        _smash = 100

kangaroo0 = rogerTheKangaroo()
endboss0 = Endboss()

while game:
    KEYS_DOWN = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

    if (KEYS_DOWN[K_SPACE]):
        if kangaroo0._points < 9:
            kangaroo0.upperCut()
        else:
            write("You dont have enough attack points!", 0.08)

    if (KEYS_DOWN[K_q]):
        if kangaroo0._points < 29:
            ultraPunch()
        else:
            write("You dont have enough attack points!")

    if endboss0._lifepoints == 0:
        write("You have defeated the boss! Congratulations!", 0.08)
        game = False

    num1 = 0
    num1 = random.randrange(1, 301)
    if num1 == 300:
        write("The enboss used smash! Quick dodge!", 0.04)
        time.sleep(0.3)
        smash()
        write("You have gained 10 attack points your current is " + kangaroo0._lifepoints)
        kangaroo0._lifepoints += 10


    if (KEYS_DOWN[K_UP]):
        playerRect.y -= playerSpeed
    elif (KEYS_DOWN[K_DOWN]):
        playerRect.y += playerSpeed

    if (KEYS_DOWN[K_LEFT]):
        playerRect.x -= playerSpeed
    elif (KEYS_DOWN[K_RIGHT]):
        playerRect.x += playerSpeed

    SCREEN.fill(BG_COLOUR)
    SCREEN.blit(playerSprite, playerRect)

    pygame.display.flip()

    CLOCK.tick(FPS)
