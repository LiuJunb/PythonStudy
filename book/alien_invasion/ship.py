import pygame


class Ship:

    def __init__(self, screen, ai_settings):
        """初始化飞船并设置其初始化位置"""
        self.screen = screen
        self.ai_settings = ai_settings

        # 加载飞船图片并获取其外接矩形
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        # print('self.rect:')
        # print(self.rect)  # <rect(0, 0, 60, 48)>
        # print('self.screen_rect:')
        # print(self.screen_rect)  # <rect(0, 0, 1200, 800)>
        # (600, 400) 600 800
        # print(self.screen_rect.center, self.screen_rect.centerx, self.screen_rect.bottom)
        # 0 48 60 0
        # print(self.rect.top, self.rect.bottom, self.rect.right, self.rect.left)

        # 将每艘飞船放在屏幕的底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # 752 800  570 630
        print(self.rect.top, self.rect.bottom, self.rect.left, self.rect.right)

        # 在飞船的属性center中存储小数值
        self.center = float(self.rect.centerx)

        # 飞船移动的标志
        self.move_right = False
        self.move_left = False

    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)

    def update(self):

        """根据移动标志调整飞船的位置,更新的是center 而不是centerx"""
        if self.move_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.move_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor
        # 根据self.center更新rect对象
        self.rect.centerx = self.center

    def center_ship(self):
        """让飞船在屏幕上剧中"""
        self.center = self.screen_rect.centerx