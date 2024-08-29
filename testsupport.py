import random
import pygame
import sys
from pygame.locals import *

# 초기화
pygame.init()

# 화면 설정
screen_width = 1920
screen_height = 1080
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Crazy Arcade by RoDeLa")

# FPS 설정
clock = pygame.time.Clock()
FPS = 30
title_font = pygame.font.Font(None,120)
menu_font = pygame.font.Font(None,70)

# 배경 설정
background = pygame.image.load("./image/Map.jpg")
background = pygame.transform.scale(background, (screen_width, screen_height))

# 캐릭터 설정
character = pygame.image.load("./image/Bezzi.png")
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width / 2) - (character_width / 2)
character_y_pos = (screen_height / 2)

# 이동 좌표 초기화
to_x = 0
to_y = 0

# 게임 루프
is_game_running = True
while is_game_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_game_running = False
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT: 
                to_x -= 2 
            if event.key == pygame.K_RIGHT:
                to_x += 2  
            if event.key == pygame.K_UP:
                to_y -= 2 
            if event.key == pygame.K_DOWN: 
                to_y += 2  

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0

    # 캐릭터 위치 업데이트
    character_x_pos += to_x
    character_y_pos += to_y
    
    # 경계 넘어가면 나오게
    if character_x_pos <= 0:
        character_x_pos = 0
        character_x_pos = (screen_width / 2) - (character_width / 2)
        character_y_pos = (screen_height / 2)
        
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width
        character_x_pos = (screen_width / 2) - (character_width / 2)
        character_y_pos = (screen_height / 2)
        
    if character_y_pos <= 0:
        character_y_pos = 0
        character_x_pos = (screen_width / 2) - (character_width / 2)
        character_y_pos = (screen_height / 2)
        
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height
        character_x_pos = (screen_width / 2) - (character_width / 2)
        character_y_pos = (screen_height / 2)
        
#적 정의
class enemy:
    
    enemy = pygame.image.load("./image/Badguy.png")
    enemy_caught = pygame.image.load("./image/Captured.png")
    
    
    size = enemy.get_rect().size
    width = size[0]
    height = size[1]
    
    x = None
    y = None
    
    speed = random.randrange(-1,3,2)
    
    isAlive = True
    isCaught = False
    
    time = 5
    
    elapsed_time = 0
    start_ticks = None
    
    def __init__(self):
        self.x = random.randrange(-1,2,2)
        self.y = random.randrange(-1,2,2)
        
    def get_rect(self):
        rect_x = self.x + self.width / 8
        rect_y = self.y + self.width / 8
        
        rect = pygame.Rect(rect_x, rect_y, rect_width, rect_width)

        return rect
    
    def displayEnemy(self):
        if not self.isCaught:
            screen.blit(self.enemy,(self.x,self.y))
        else:
            screen.blit(self.enemy_caught, (self.x,self.y))
        
    def moveEnemy(self):
        if not self.isCaught:
            if random.randrange(70) == 0:
                self.x_direction *= -1
            if random.randrange(70) == 0:
                self.y_direction *= -1
                
            self.x += self.speed * self.x_direction
            self.y += self.speed * self.y_direction
            
            if self.x < 0 or self.x > screen_width - self.width:
                self.x_direction *= -1
            if self.y < 0 or self.y > screen_height - self.height:
                self.y_direction *= -1
                
    def reachBalloon(self):
        if not self.isCaught:
            self.start_ticks = pygame.time.get_ticks()
        
        
    def setStartTicks(self):
        if not self.isCaught:
            self.start_ticks = pygame.time.get_ticks()
            
    def countdown(self):
        if self.isCaught:
            self.elapsed_time = (pygame.time.get_ticks() - self.start_ticks) / 1000
            timer = self.time - self.elapsed_time
            if timer < 0:
                self.isCaught = False
    def killEnemy(self):
        self.kill_enemy.play()
        self.kill_enemy.play()
        self.isAlive = False

    def beCaught(self):
        self.setStartTicks()
        self.isCaught = True

    def showEnemy(self):
        self.displayEnemy()
        self.moveEnemy()
        self.countdown()
    
    
#물풍선 정의
class waterballoon:
    waterballoon = pygame.image.load("./image/Balloon.png")
    
    water_bottom = pygame.image.load("./image/water_bottom.png")
    water_center = pygame.image.load("./image/water_center.png")
    water_left = pygame.image.load("./image/water_left.png")
    water_right = pygame.image.load("./image/water_right.png")
    water_top = pygame.image.load("./image/water_top.png")    
    
    
    # 화면 그리기
    screen.blit(background, (0, 0))  # 배경 그리기
    screen.blit(character, (character_x_pos, character_y_pos))  # 캐릭터 그리기
    pygame.display.update()  # 화면 업데이트

# 게임 종료
pygame.quit()
sys.exit()