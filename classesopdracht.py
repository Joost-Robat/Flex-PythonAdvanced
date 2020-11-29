from time import sleep
import sys, os, time, pygame
clear = lambda: os.system('cls')
from pygame._sdl2 import *
from pygame import mixer
from pygame.locals import *

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
    _speed = 60
    _invSpace = 20
    _magicPower = 30
    _physicalPower = 90
    _points = 100

def ultraPunch():
    write("Roger The Kangaroo used his trump card: Ultra Punch!", 0.08)
    time.sleep(2)
    write("Ultra punch consumed 10 points...", 0.08)
    rogerTheKangaroo._points -= 10
    write("You have ", rogerTheKangaroo._points + "left...", 0.08)

kangaroo0 = rogerTheKangaroo()

while game:
    KEYS_DOWN = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

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
