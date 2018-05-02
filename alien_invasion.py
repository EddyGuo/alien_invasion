# Author: EddyGuo
# Version: 0.1
# Update: 2018/5/2
# Environment: Windows 7&10
#              PyCharm 2018.1.1 (Community Edition)
#              Anaconda3-5.1.0-Windows-x86_64
#############################
import pygame

from alien_invasions.settings import Settings
from alien_invasions.ship import Ship
import alien_invasions.game_function as gf
from alien_invasions.game_stats import GameStats
from alien_invasions.button import Button
from alien_invasions.scoreboard import Scoreboard
from pygame.sprite import Group


def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    play_button = Button(ai_settings, screen, "Play")
    stats = GameStats(ai_settings)
    score_board = Scoreboard(ai_settings, stats, screen)

    # 创建一艘飞船，一个存储子弹的编组，一个外星人编组
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()

    # 创建外星人群
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # 开始游戏主循环
    while True:

        # 监视键盘和鼠标事件
        gf.check_events(ai_settings, stats, screen, score_board, ship, aliens, bullets, play_button)

        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, stats, screen, score_board, ship, bullets, aliens)
            gf.update_aliens(ai_settings, stats, screen, score_board,  ship, aliens, bullets)

        gf.update_screen(ai_settings, stats, screen, score_board, ship, aliens, bullets, play_button)


run_game()


