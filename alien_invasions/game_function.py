import sys
import pygame
from alien_invasions.bullet import Bullet


def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """响应按键按下事件"""
    if event.key == pygame.K_RIGHT:
        # 向右移动飞船
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        # 向右移动飞船
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        # 创建一颗子弹，并将其加入到编组
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


def check_keyup_events(event, ship):
    """响应按键释放事件"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def check_events(ai_settings, screen, ship, bullets):
    """响应按键和鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def update_screen(ai_settings, screen, ship, bullets):
    """更新屏幕"""
    screen.fill(ai_settings.screen_bg_color)

    # 在飞船和外星人后面重绘所有子弹
    for bullet in bullets.sprites():  # 返回一个列表，包含编组的所有精灵
        bullet.draw_bullet()
    ship.blitme()

    # 让最近绘制的屏幕可见
    pygame.display.flip()
