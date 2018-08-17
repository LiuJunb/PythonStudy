# 推出系统
import sys
# 游戏开发模块
import pygame
# 导入配置文件
from settings import Settings
# 导入飞船
from ship import Ship
# 导入 game_function模块
import game_function as gf
# 导入子弹编组
from pygame.sprite import Group
# 导入游戏状态
from  game_stats import GameStats


def run_game():
    # 初始化游戏,并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display\
        .set_mode((ai_settings.screen_width,
                   ai_settings.screen_height))  # 窗口宽高
    pygame.display.set_caption(ai_settings.alien_caption)  # 窗口title

    # 创建一个统计用于存储游戏统计信息的实例
    stats = GameStats(ai_settings)

    # 创建飞船
    ship = Ship(screen, ai_settings)
    # 创建一个用于子弹的编组
    bullets = Group()
    # 创建外星人编组
    aliens = Group()
    # 创建外星人人群
    gf.create_fleet(ai_settings, screen, aliens, ship)

    # 开始有些的主循环
    while True:

        # 监听键盘和鼠标事件
        gf.check_events(ai_settings, screen, ship, bullets)

        # 如果在游戏中
        if stats.game_active:
            # 调用每个飞船的update:
            ship.update()

            # 更新bullets
            gf.update_bullets(ai_settings, screen, ship, bullets, aliens)

            # 外星人移动
            gf.update_aliens(ai_settings, aliens, ship, stats, screen, bullets)

        # 更新屏幕
        gf.update_screen(ai_settings, screen, ship, bullets, aliens)


run_game()

