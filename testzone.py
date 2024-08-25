import pygame
import random
import sys
from pygame.locals import *

#Pygame 초기화
pygame.init()

#화면
screen_width = 1000  # 가로
screen_height = 800  # 세로
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Crazy Arcade by RoDeLa")

#FPS
clock = pygame.time.Clock()
FPS = 30

#글뜰
title_font = pygame.font.Font(None,120)
menu_font = pygame.font.Font(None,70)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)

#이미지 로드
def load_image(filename):
    try:
        return pygame.image.load(filename)
    except pygame.error as e:
        print(f"이미지를 로드할 수 없습니다 {filename}: {e}")
        return None

#이미지 로딩 22
background_img = pygame.image.load("Map.jpg")
player_img = pygame.image.load("Bezzi.png")
player_rect = player_img.get_rect()
player_rect.topleft = (100,100)
badguy_img = pygame.image.load("Badguy.jpg")
waterballoon_img = pygame.image.load("Waterballoon.png")

#게임 동작 동안 이벤트
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen 
    pygame.display.update()

#플레이어 
player_speed = 5
player_pos = [screen_width // 2, screen_height // 2]
player_rect = player_img.get_rect(center=player_pos)

#물풍선
balloons = []  #물풍선리스트
balloon_timer = 0  #물풍선 타이머
BALLON_LIFETIME = 90  # 물풍선 지속 시간 (3초)
BALLON_DELAY = 30  # 물풍선 재사용 대기 시간

# 악당 관련 변수
badguys = []
BADGUY_COUNT = 3
BADGUY_SPEED = 2
BADGUY_TIMER = 0
BADGUY_DELAY = 60  

# 게임 상태
game_over = False
last_balloon_time = pygame.time.get_ticks()  #마지막 물풍선 관련 시간

def spawn_badguys():
    for _ in range(BADGUY_COUNT):
        x = random.randint(0, WIDTH - badguy_img.get_width())
        y = random.randint(0, HEIGHT - badguy_img.get_height())
        badguy = pygame.Rect(x, y, badguy_img.get_width(), badguy_img.get_height())
        badguys.append(badguy)

def move_badguys():
    for badguy in badguys:
        direction = random.choice([(-1, 0), (1, 0), (0, -1), (0, 1)])
        badguy.x += direction[0] * BADGUY_SPEED
        badguy.y += direction[1] * BADGUY_SPEED
        # 화면 경계 검사
        if badguy.left < 0 or badguy.right > WIDTH:
            badguy.x -= direction[0] * BADGUY_SPEED
        if badguy.top < 0 or badguy.bottom > HEIGHT:
            badguy.y -= direction[1] * BADGUY_SPEED

def check_collision(rect1, rect2):
    return rect1.colliderect(rect2)

#초기 악당 생성
spawn_badguys()
    
    #악당
    if BADGUY_TIMER <= 0:
        spawn_badguys()  #
        BADGUY_TIMER = BADGUY_DELAY  
    else:
        BADGUY_TIMER -= 1

    move_badguys()
#메인 루프
while not game_over:
    #이벤트 처리
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key == K_SPACE:
                if pygame.time.get_ticks() - last_balloon_time > BALLON_DELAY * 1000:  # 물풍선 재사용 대기 시간 확인
                    last_balloon_time = pygame.time.get_ticks()
                    # 물풍선 추가
                    balloons.append([player_pos[0], player_pos[1], BALLON_LIFETIME])
    
    # 키 입력 처리
    keys = pygame.key.get_pressed()
    if keys[K_LEFT]:
        player_pos[0] -= player_speed
    if keys[K_RIGHT]:
        player_pos[0] += player_speed
    if keys[K_UP]:
        player_pos[1] -= player_speed
    if keys[K_DOWN]:
        player_pos[1] += player_speed
    
    # 플레이어 위치 업데이트
    player_rect.center = player_pos
    
    # 물풍선 업데이트
    for balloon in balloons[:]:
        balloon[2] -= 1  # 물풍선 타이머 감소
        if balloon[2] <= 0:
            balloons.remove(balloon)  # 물풍선 삭제
        else:
            screen.blit(waterballoon_img, (balloon[0], balloon[1]))  #물풍선 이미지 표시


    
    #화면 채우기
    screen.blit(background_img, (0, 0))
    
    #물풍선 그리기
    for balloon in balloons:
        screen.blit(waterballoon_img, (balloon[0], balloon[1]))
    
    #플레이어 그리기
    screen.blit(player_img, player_rect)
    
