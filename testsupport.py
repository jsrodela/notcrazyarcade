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


    
    # 화면 그리기
    screen.blit(background, (0, 0))  # 배경 그리기
    screen.blit(character, (character_x_pos, character_y_pos))  # 캐릭터 그리기
    pygame.display.update()  # 화면 업데이트

# 게임 종료
pygame.quit()
sys.exit()