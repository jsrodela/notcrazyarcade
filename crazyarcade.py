import sys
import pygame
from pygame.locals import *

# 파이게임 시작
pygame.init()

# 초당 프레임 설정: 30
FPS = 30
FramePerSec = pygame.time.Clock()

# 컬러 세팅
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# 화면 크기 설정
WIDTH, HEIGHT = 640, 480
GameDisplay = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Circle Drawing")

# 메인 루프
running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    # 화면을 흰색으로 채움
    GameDisplay.fill(WHITE)

    # 검은색 원 그리기
    pygame.draw.circle(GameDisplay, BLACK, (100, 50), 30)

    # 화면 업데이트
    pygame.display.update()

    # FPS 설정
    FramePerSec.tick(FPS)

# 파이게임 종료
pygame.quit()
sys.exit()