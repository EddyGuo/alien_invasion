import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """创建单个外星人"""

    def __init__(self, ai_settings, screen):
        """初始化外星人设置"""
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # 加载外星人
        self.image = pygame.image.load('images/alien/alien.png')
        self.rect = self.image.get_rect()

        # 将每个外星人先放在左上角
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # 用小数存储外星人位置
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def blitme(self):
        """在指定位置绘制外星人"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """向左或右移动外星人"""
        self.x += self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction
        self.rect.x = self.x

    def check_edges(self):
        """如果有外星人位于屏幕边缘，则返回True"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True
