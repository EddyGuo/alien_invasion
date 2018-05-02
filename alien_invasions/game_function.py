import sys
import pygame
from time import sleep
from alien_invasions.bullet import Bullet
from alien_invasions.alien import Alien


def check_aliens_bottom(ai_settings, stats, screen, score_board, ship, aliens, bullets):
    """检测是否有外星人到达屏幕底端"""
    screen_rect = screen.get_rect()
    for alien in aliens:
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(ai_settings, stats, screen, score_board, ship, aliens, bullets)


def ship_hit(ai_settings, stats, screen, score_board, ship, aliens, bullets):
    """响应飞船与外星人相撞"""
    if stats.ships_left > 0:
        # 将ships_left减1
        stats.ships_left -= 1
        score_board.prep_ships_left()

        # 清空外星人和子弹
        aliens.empty()
        bullets.empty()

        # 创建一群新的外星人
        create_fleet(ai_settings, screen, ship, aliens)

        #  将飞船移到中心
        ship.center_ship()

        # 暂停0.5秒
        sleep(0.5)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)


def check_keydown_events(event, ai_settings, stats, screen, score_board, ship, aliens, bullets):
    """响应按键按下事件"""
    # 只有当游戏开始时，才激活游戏按键
    if stats.game_active:
        if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
            # 向右移动飞船
            ship.moving_right = True
        elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
            # 向左移动飞船
            ship.moving_left = True
        elif event.key == pygame.K_SPACE:
            # 发射子弹
            fire_bullets(ai_settings, screen, ship, bullets)

    if event.key == pygame.K_ESCAPE:
        sys.exit()
    elif event.key == pygame.K_RETURN:
        game_start(ai_settings, stats, screen, score_board, ship, aliens, bullets)


def check_keyup_events(event, ship):
    """响应按键释放事件"""
    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
        ship.moving_left = False


def check_events(ai_settings, stats, screen, score_board, ship, aliens, bullets, play_button):
    """响应按键和鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, stats, screen, score_board, ship, aliens, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, stats, screen, score_board, ship, aliens, bullets,
                              play_button, mouse_x, mouse_y)


def check_play_button(ai_settings, stats, screen, score_board, ship, aliens, bullets, play_button, mouse_x, mouse_y):
    """玩家单击play开始游戏"""
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked:
        game_start(ai_settings, stats, screen, score_board, ship, aliens, bullets)


def game_start(ai_settings, stats, screen, score_board, ship, aliens, bullets):
    """游戏开始初始化"""
    if not stats.game_active:
        # 重置游戏信息
        stats.reset_stats()
        stats.game_active = True
        # 重置计分
        score_board.prep_top_score()
        score_board.prep_score()
        score_board.prep_level()
        score_board.prep_ships_left()

        # 清空外星人和子弹
        aliens.empty()
        bullets.empty()
        # 创建一群新的外星人
        create_fleet(ai_settings, screen, ship, aliens)

        #  将飞船移到中心
        ship.center_ship()

        # 隐藏光标
        pygame.mouse.set_visible(False)

        # 初始化游戏节奏
        ai_settings.initialize_dynamic_settings()


def update_screen(ai_settings, stats, screen, score_board, ship, aliens, bullets, play_button):
    """更新屏幕"""
    screen.fill(ai_settings.screen_bg_color)

    # 在飞船和外星人后面重绘所有子弹
    for bullet in bullets.sprites():  # 返回一个列表，包含编组的所有精灵
        bullet.draw_bullet()

    ship.blitme()
    aliens.draw(screen)

    # 显示得分
    score_board.show_score()

    # 如果游戏处于非活跃状态则显示play
    if not stats.game_active:
        play_button.draw_button()

    # 让最近绘制的屏幕可见
    pygame.display.flip()


def update_bullets(ai_settings, stats, screen, score_board, ship, bullets, aliens):
    """更新子弹"""
    bullets.update()

    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    check_bullet_alien_collisions(ai_settings, stats, screen, score_board, ship, bullets, aliens)


def check_bullet_alien_collisions(ai_settings, stats, screen, score_board, ship, bullets, aliens):
    """子弹碰撞检测"""
    collisions = pygame.sprite.groupcollide(bullets, aliens, ai_settings.bullets_vanish , True)

    # 计分
    if collisions:
        for aliens in collisions.values():
            stats.score += ai_settings.alien_points * len(aliens)
            score_board.prep_score()
        # 最高得分
        check_top_score(stats, score_board)

    # 删除现有子弹并新建一群外星人
    if (len(aliens)) == 0:
        # 如果消灭一群敌人，等级提升
        stats.level += 1
        score_board.prep_level()

        bullets.empty()
        ai_settings.increase_speed()
        create_fleet(ai_settings, screen, ship, aliens)


def update_aliens(ai_settings, stats, screen, score_board, ship, aliens, bullets):
    """更新外星人"""
    check_fleet_edges(ai_settings, aliens)
    aliens.update()

    # 飞船碰撞检测
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, stats, screen, score_board, ship, aliens, bullets)

    # 检测是否有外星人到达屏幕底端
    check_aliens_bottom(ai_settings, stats, screen, score_board, ship, aliens, bullets)


def fire_bullets(ai_settings, screen, ship, bullets):
    """发射子弹"""
    # 创建一颗子弹，并将其加入到编组
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


def create_fleet(ai_settings, screen, ship, aliens):
    """创建外星人群"""
    # 创建一个外星人并计算能容纳多少个外星人
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien_height = alien.rect.height
    ship_height = ship.rect.height
    number_aliens_x = get_number_alien_x(ai_settings, alien_width)
    number_rows = get_number_rows(ai_settings, alien_height, ship_height)

    # 创建外星人群
    for row_number in range(number_rows):
        # 创建第一行外星人
        for alien_number in range(number_aliens_x):
            # 创建一个外星人，并加入当前行
            create_alien(ai_settings, screen, aliens, alien_width, alien_height, alien_number, row_number)


def get_number_alien_x(ai_settings, alien_width):
    """计算每行能容纳多少个外星人"""
    # 外星人间距为外星人宽度
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x


def get_number_rows(ai_settings, alien_height, ship_height):
    """计算能容纳几行外星人"""
    available_space_y = ai_settings.screen_height - 3 * alien_height - ship_height
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows


def create_alien(ai_settings, screen, aliens, alien_width, alien_height, alien_number, row_number):
    """创建一个外星人并加入当前行"""
    alien = Alien(ai_settings, screen)
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.y = alien_height + 2 * alien_height * row_number
    alien.rect.y = alien.y
    aliens.add(alien)


def check_fleet_edges(ai_settings, aliens):
    """响应外星人到达边缘"""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break


def change_fleet_direction(ai_settings, aliens):
    """碰撞改变方向"""
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1


def check_top_score(stats, score_board):
    if stats.score > stats.top_score:
        stats.top_score = stats.score
        score_board.prep_top_score()
