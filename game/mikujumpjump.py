"""
version: 2.0
author: kriss-spy
feature: using square to represent real avatar, instead of modeling the picture
date: 7/16
bug:
"""

def play_mikujumpjump():
    # start the game in "game/mikujumpjump.py"
    from game import mikujumpjump


import pygame
import sys
import random
import pygame.font
import os

# 游戏状态
STATE_START_SCREEN = 0
STATE_GAME_PLAYING = 1
STATE_GAME_OVER = 2
game_state = STATE_START_SCREEN


# 开始游戏界面绘制
def draw_start_screen():
    start_text = font.render("Press SPACE to Start", True, WHITE)
    start_rect = start_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
    screen.blit(start_text, start_rect)


# 游戏结束界面绘制
def draw_game_over_screen():
    game_over_text = font.render("Game Over - Press SPACE to Restart", True, WHITE)
    game_over_rect = game_over_text.get_rect(
        center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
    )
    screen.blit(game_over_text, game_over_rect)


# 初始化pygame
pygame.init()

# 初始化字体
font = pygame.font.Font(None, 36)  # 使用默认字体，设置字号为36

# 设置窗口大小
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 500
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# 设置游戏时钟
clock = pygame.time.Clock()

# 定义颜色
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GROUND_COLOR = (150, 75, 0)

# 载入背景图
background = pygame.image.load("game/resources/background2.jpg")

# 地面位置
GROUND_LEVEL = SCREEN_HEIGHT - 40
scroll_position = 0


# compensate for using square image for character
TOLERANCE = 30

# 设置角色属性
player_image = pygame.image.load("game/resources/negi-miku.png").convert_alpha()
PLAYER_HEIGHT = player_image.get_height()
PLAYER_WIDTH = player_image.get_width() - TOLERANCE
PLAYER_SIZE = PLAYER_HEIGHT
player_pos = [PLAYER_WIDTH, GROUND_LEVEL - PLAYER_HEIGHT]
player_velocity = 0
jump_status = 0
# 0: not jumping
# 1: jumping
# 2: double jumping

player_rect = player_image.get_rect()
player_rect.topleft = player_pos


# 设置障碍属性
obstacle_image = pygame.image.load("game/resources/3barbed-wires.png").convert_alpha()
OBSTACLE_HEIGHT = obstacle_image.get_height()
OBSTACLE_WIDTH = obstacle_image.get_width()
OBSTACLE_SIZE = OBSTACLE_HEIGHT

OBSTACLE_MIN_NUM = 1
OBSTACLE_MAX_NUM = 3
obstacles = []
OBSTACLE_SPACING = 600  # 障碍物之间的距离
OBSTACLE_COUNT = 0


MOVING_SPEED = 8
JUMP_SPEED = 18


def reset_status_variables():
    global player_pos, player_velocity, jump_status, obstacles, OBSTACLE_COUNT, MOVING_SPEED, JUMP_SPEED, player_rect

    player_pos = [PLAYER_WIDTH, GROUND_LEVEL - PLAYER_HEIGHT]
    player_velocity = 0
    jump_status = 0
    obstacles = []
    OBSTACLE_COUNT = 0
    MOVING_SPEED = 8
    JUMP_SPEED = 18

    player_rect = player_image.get_rect()
    player_rect.topleft = player_pos


def log2txt(filename):
    # open filename as log file
    # write all defined global variables to log file
    # close
    with open(filename, "w") as f:
        for key, value in globals().items():
            f.write(f"{key}: {value}\n")


music_folder = r"music/resources"
music_name = "hibana"
music_name = music_name + ".mp3"
music_path = os.path.join(music_folder, music_name)
pygame.mixer.music.load(music_path)
pygame.mixer.music.play()



# 游戏主循环
while True:
    if game_state == STATE_START_SCREEN:
        screen.fill(BLACK)
        draw_start_screen()
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_state = STATE_GAME_PLAYING
                # 重置游戏变量
                reset_status_variables()

    elif game_state == STATE_GAME_PLAYING:
        
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                if jump_status < 2:
                    player_velocity = -JUMP_SPEED
                    jump_status += 1

        # 更新角色位置
        if jump_status != 0:
            player_pos[1] += player_velocity
            player_velocity += 1  # 重力加速度
            if player_pos[1] >= GROUND_LEVEL - PLAYER_HEIGHT:
                player_velocity = 0
                jump_status = 0
                player_pos[1] = GROUND_LEVEL - PLAYER_HEIGHT
            player_rect.topleft = player_pos
        
        # increase MOVING_SPEED every 5 obstacles
        MOVING_SPEED += OBSTACLE_COUNT // 5
        OBSTACLE_COUNT = OBSTACLE_COUNT % 5

        # 更新障碍位置
        for obstacle in obstacles:
            obstacle[0] -= MOVING_SPEED  # 障碍物移动速度

        # 移除屏幕外的障碍
        obstacles = [obs for obs in obstacles if obs[0] + obs[2] > 0]

        # 添加新障碍
        if len(obstacles) == 0 or obstacles[-1][0] < SCREEN_WIDTH - OBSTACLE_SPACING:
            num = random.randint(OBSTACLE_MIN_NUM, OBSTACLE_MAX_NUM)
            obstacles.append(
                [
                    SCREEN_WIDTH,
                    GROUND_LEVEL - OBSTACLE_HEIGHT * num,
                    OBSTACLE_WIDTH,
                    num,
                ]
            )
            OBSTACLE_COUNT += 1
            OBSTACLE_SPACING = random.randint(400, 600) + MOVING_SPEED * 20

        # 检测碰撞
        for obstacle in obstacles:
            # left side of obstale
            if (
                player_pos[0] + PLAYER_WIDTH > obstacle[0]
                and player_pos[0] < obstacle[0]
                and player_pos[1] + PLAYER_HEIGHT > obstacle[1]
                or
                # upper side of obstacle
                player_pos[0] < obstacle[0] + obstacle[2]
                and player_pos[0] + PLAYER_WIDTH > obstacle[0]
                and player_pos[1] + PLAYER_HEIGHT > (obstacle[1] + TOLERANCE)
            ):
                game_state = STATE_GAME_OVER
                pygame.mixer.music.stop()  # 停止播放

        # 创建表示MOVING_SPEED的文本
        speed_text = font.render(f"MOVING_SPEED: {MOVING_SPEED}", True, BLACK)
        speed_text_rect = speed_text.get_rect()
        speed_text_rect.topright = (SCREEN_WIDTH - 10, 10)  # 设置文本位置在右上角

        # 绘制背景
        screen.blit(background, (0, 0))

        screen.blit(speed_text, speed_text_rect)  # 绘制MOVING_SPEED文本

        # 绘制地面
        ground_rect = pygame.Rect(
            -scroll_position,
            GROUND_LEVEL,
            SCREEN_WIDTH * 2,
            SCREEN_HEIGHT - GROUND_LEVEL,
        )
        pygame.draw.rect(screen, GROUND_COLOR, ground_rect)

        # 游戏主循环中绘制角色
        screen.blit(player_image, player_rect)

        # 绘制障碍
        for obstacle in obstacles:
            for i in range(obstacle[3]):
                screen.blit(
                    obstacle_image,
                    [obstacle[0], GROUND_LEVEL - OBSTACLE_HEIGHT * (i + 1)],
                )

        # 更新滚动位置
        scroll_position = (scroll_position + 5) % SCREEN_WIDTH

        # 设置帧率
        clock.tick(30)

    elif game_state == STATE_GAME_OVER:
        screen.fill(BLACK)
        draw_game_over_screen()
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_state = STATE_GAME_PLAYING
                # 重置游戏变量
                reset_status_variables()
                
                # 绘制背景
                screen.blit(background, (0, 0))

                screen.blit(speed_text, speed_text_rect)  # 绘制MOVING_SPEED文本

                # 绘制地面
                ground_rect = pygame.Rect(
                    -scroll_position,
                    GROUND_LEVEL,
                    SCREEN_WIDTH * 2,
                    SCREEN_HEIGHT - GROUND_LEVEL,
                )
                pygame.draw.rect(screen, GROUND_COLOR, ground_rect)

                screen.blit(player_image, player_rect)
                
                pygame.mixer.music.load(music_path)
                pygame.mixer.music.play()


    pygame.display.flip()
