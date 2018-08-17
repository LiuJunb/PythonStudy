import sys

import pygame

from bullet import Bullet
from alien import Alien
from  time import  sleep

# 检查键盘事件
def check_events(ai_settings, screen, ship, bullets):
    """监听按键事件和鼠标事件"""
    for event in pygame.event.get():
        # print(event)
        # print(pygame.KEYDOWN, pygame.QUIT,  pygame.K_RIGHT)  # 2  12 275
        if event.type == pygame.QUIT:  # 是鼠标点击x
            sys.exit()
        elif event.type == pygame.KEYDOWN:  # 键盘按下
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:  # 键盘抬起
            check_keyup_events(event, ai_settings, screen, ship, bullets)


# 检查按钮按下
def check_keydown_events(event, ai_settings, screen, ship, bullets):
    if event.key == pygame.K_RIGHT:  # 按右键
        ship.move_right = True
    elif event.key == pygame.K_LEFT:  # 按左键
        ship.move_left = True
    elif event.key == pygame.K_SPACE:  # 按空格建
        # 发射子弹
        fire_bullet(ai_settings, screen, ship, bullets);


# 发射子弹
def fire_bullet(ai_settings, screen, ship, bullets):
    # 把子弹添加到编组（发射子弹）
    if len(bullets) < ai_settings.bullet_allowed:
        # 在飞船的旁边创建一个子弹
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


# 检查按钮抬起
def check_keyup_events(event, ai_settings, screen, ship, bullets):
    if event.key == pygame.K_RIGHT:
        ship.move_right = False
    elif event.key == pygame.K_LEFT:
        ship.move_left = False


# 更新屏幕(给屏幕绘制精灵)
def update_screen(ai_settings, screen, ship, bullets, aliens):
    """更新屏幕上的图像，并切换到新的屏幕"""
    # 每次循环时都重新绘制屏幕
    screen.fill(ai_settings.bg_color)

    # 在飞船和外星人底层重绘所有子弹
    for bullet in bullets.sprites():  # 拿到所有的子弹
        bullet.draw_bullet()  # 把子弹绘制出来

    # 把飞船画出来( 记住先画背景在画飞船) blit()
    ship.blitme()

    # 把外星人画出来
    # alien.blitme()
    aliens.draw(screen)

    # 让最近绘制的屏幕可见
    pygame.display.flip()


# 更新子弹
def update_bullets(ai_settings, screen, ship, bullets, aliens):
    # 调用每个子弹的update
    bullets.update()

    # 删除已经消失的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    # 检查是否有子弹击中外星人
    check_bullet_alien_collisions(ai_settings, screen, ship, bullets, aliens)


# 检查是否有子弹击中外星人
def check_bullet_alien_collisions(ai_settings, screen, ship, bullets, aliens):
    # 检查是否有子弹击中外星人
    # 如果时这样，就删除相应的子弹和外星人
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)

    if len(aliens) == 0:
        # 删除现有的子弹并新建一群外星人
        bullets.empty()
        create_fleet(ai_settings, screen, aliens, ship)


# 创建外星人群
def create_fleet(ai_settings, screen, aliens, ship):
    """创建外星人群"""
    # 创建一个外星人，并计算一行可容纳多少个外星人
    # 外星人间距为外星人宽度
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    number_aliens_x = get_number_alien_x(ai_settings, alien_width)
    number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)

    # print(number_aliens_x, range(number_aliens_x)[0])
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings, screen, aliens, alien_number, row_number)


# 拿到外星人个数
def get_number_alien_x(ai_settings, alien_width):
    """计算每一行可容纳多少个外星人"""
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x


# 创建外星人
def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    # 创建一个外星人并将其加入当前行
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    # 指定外星人的x轴
    alien.rect.x = alien.x
    # 指定外星人的y轴
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)


# 获取外星人显示的行数
def get_number_rows(ai_settings, ship_height, alien_height):
    """计算屏幕可容纳多少行外星人"""
    available_space_y = (ai_settings.screen_height -
                         (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows


# 更新外星人群众所有外星人的位置
def update_aliens(ai_settings, aliens, ship, stats, screen, bullets):
    """ 检查是否右外星人位于屏幕的边缘，并且更新整群外星人的位置"""
    check_fleet_edges(ai_settings, aliens)
    aliens.update()

    # 检查外星人以飞船的碰撞
    if pygame.sprite.spritecollideany(ship, aliens):
        print('ship hit !!!')
        ship_hit(ai_settings, aliens, ship, stats, screen, bullets)

    # 检查是否有外星人到达屏幕底端
    check_aliens_buttom(ai_settings, aliens, ship, stats, screen, bullets)


def check_fleet_edges(ai_settings, aliens):
    """有外星人到达边缘时采取相应的措施"""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break


# 将整个外星人下移，并改变它们的方向
def change_fleet_direction(ai_settings, aliens):
    """将整个外星人下移"""
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    # 并改变它们的方向
    ai_settings.fleet_direction *= -1


def ship_hit(ai_settings, aliens, ship, stats, screen, bullets):
    """响应被外星人撞到的飞船"""

    if stats.ships_left > 0:

        # 将ships_left减1
        stats.ships_left -= 1
        # 清空外星人列表和子弹列表
        aliens.empty()
        bullets.empty()

        # 创建一群新的外星人，并将飞船放到屏幕底端中央
        create_fleet(ai_settings, screen, aliens, ship)
        ship.center_ship()

        # 暂停
        sleep(ai_settings.sleep)

    else:
        stats.game_active = False


def check_aliens_buttom(ai_settings, aliens, ship, stats, screen, bullets):
    """检查是否有外星人到达了屏幕底端"""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            # 像飞船被撞到一样进行处理
            ship_hit(ai_settings, aliens, ship, stats, screen, bullets)
            break






