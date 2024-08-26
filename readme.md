##테스트용##
python -m pygame.examples.aliens

문제발견:: pygame 익스텐션을 pygame.py로 설정해서 충돌

파이게임 테스트: python testzone.py

testzone.py에서 실행 완료되면 crazyarcade.py에 옮길 예정

수정 4차:
testzone.py는 원인 모를 크래쉬로 인해 안쓸 예정


아래는 test.py의 수정본 (chatgpt 문법검사)

##########################


import random
import pygame
from pygame.locals import *

# 게임 초기화
pygame.init()

# 디스플레이
screen_width = 1000
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Crazy Arcade by RoDeLa V7")

# 변수 설정
clock = pygame.time.Clock()
FPS = 30

WHITE = (255, 255, 255)

# 배경
background = pygame.image.load("./image/Map.jpg")

# 캐릭터 이미지
character = pygame.image.load("./image/Bezzi.png")
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]

# 캐릭터의 기준 좌표
character_x_pos = (screen_width / 2) - (character_width / 2)  # 화면 중앙
character_y_pos = (screen_height / 2) - (character_height / 2)

# 캐릭터 이동 좌표
to_x = 0
to_y = 0

# 캐릭터 이동 속도 변수
character_speed = 1

# 적 클래스
class Enemy:
    def __init__(self):
        self.image = pygame.image.load("./image/Badguy.png")
        self.size = self.image.get_rect().size
        self.width = self.size[0]
        self.height = self.size[1]
        self.x = random.randint(0, screen_width - self.width)
        self.y = 0  # 적은 화면 위에서 생성
        self.speed = random.randint(1, 3)  # 속도를 1에서 3까지 랜덤하게 설정
        self.direction_x = random.choice([-1, 1])
        self.direction_y = 1
    
    # 적의 위치 업데이트
    def update(self):
        self.x += self.direction_x * self.speed
        self.y += self.direction_y * self.speed
        
        # 적이 화면 경계를 넘어가지 않게 처리
        if self.x <= 0 or self.x >= screen_width - self.width:
            self.direction_x *= -1
        
        # 적 그리기
        screen.blit(self.image, (self.x, self.y))
    
    # 충돌 감지
    def collide(self, player_rect):
        enemy_rect = pygame.Rect(self.x, self.y, self.width, self.height)
        return enemy_rect.colliderect(player_rect)

# 적 리스트
enemies = []
enemy_spawn_timer = 0

# 이벤트 루프
running = True
while running:
    dt = clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed
            elif event.key == pygame.K_DOWN:
                to_y += character_speed
            elif event.key == pygame.K_UP:
                to_y -= character_speed

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0

    # 캐릭터 위치 업데이트
    character_x_pos += to_x * dt
    character_y_pos += to_y * dt

    # 경계 처리 (캐릭터가 화면 밖으로 나가지 않게)
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height

    # 적 생성 (3초마다)
    enemy_spawn_timer += dt
    if enemy_spawn_timer >= 3000:  # 3000ms (3초)마다 적 생성
        enemies.append(Enemy())
        enemy_spawn_timer = 0

    # 배경 그리기
    screen.blit(background, (0, 0))

    # 캐릭터 그리기
    character_rect = pygame.Rect(character_x_pos, character_y_pos, character_width, character_height)
    screen.blit(character, (character_x_pos, character_y_pos))

    # 적 업데이트 및 충돌 검사
    for enemy in enemies:
        enemy.update()
        if enemy.collide(character_rect):  # 충돌 시 게임 종료
            running = False

    # 화면 업데이트
    pygame.display.update()

# 게임 종료 처리
pygame.quit()
sys.exit()