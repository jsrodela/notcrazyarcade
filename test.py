import random
import pygame as pg

#게임 초기화
pygame.init()

#디스플레이
screen_width = 1000
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Crazy Arcade by RoDeLa V7")

#변수설정
clock = pygame.time.Clock()
FPS = 30

title_font = pygame.font.Font(None,120)
menu_font = pygame.font.Font(None,70)

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)

#배경
background = pygame.image.load("./crazyarcade.image/Map.jpg")

#적
class Enemy:
    enemy = pygame.image.load("./crazyarcade.image/Badguy.png")
    enemy_caught = pygame.image.load("./crazyarcade.image/Captured.png")
    
    size = enemy.get_rect().size 
    width = size[0]
    height = size[1]
    
    x = None
    y = None
    
    speed = 3
    
    isAlive = True
    iscaught = False