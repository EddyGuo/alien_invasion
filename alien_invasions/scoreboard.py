import pygame.font
from pygame.sprite import Group
from alien_invasions.ship import Ship


class Scoreboard:
    """得分信息"""

    def __init__(self, ai_settings, stats, screen):
        """初始化得分"""
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats

        # 得分信息字体
        self.font_color = ai_settings.font_color
        self.font_size = ai_settings.font_size
        self.font = pygame.font.SysFont(None, self.font_size)
        self.level_font = pygame.font.SysFont(None, self.font_size + 20)

        # 准备得分图像
        self.prep_top_score()
        self.prep_score()
        # 剩余飞船
        self.prep_ships_left()
        # 等级图像
        self.prep_level()

    def prep_score(self):
        """将得分渲染为图像"""
        round_score = int(self.stats.score)
        score_str = "{:,}".format(round_score)
        self.score_image = self.font.render(score_str, True, self.font_color)

        # 将得分放在最高得分下方
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = self.screen_rect.top + self.top_score_rect.height + 30

    def prep_top_score(self):
        """最高得分"""
        round_top_score = int(self.stats.top_score)
        top_score_str = "{:,}".format(round_top_score)
        self.top_score_image = self.font.render(top_score_str, True, self.font_color)

        # 将最高分放在右上
        self.top_score_rect = self.top_score_image.get_rect()
        self.top_score_rect.right = self.screen_rect.right - 20
        self.top_score_rect.top = self.screen_rect.top + 20

    def prep_level(self):
        """等级"""
        level_str = "LEVEL: %s" % str(self.stats.level)
        self.level_image = self.level_font.render(level_str, True, self.font_color)

        # 将等级放在中上
        self.level_rect = self.level_image.get_rect()
        self.level_rect.centerx = self.screen_rect.centerx
        self.level_rect.top = self.screen_rect.top + 20

    def prep_ships_left(self):
        """剩余飞船"""
        self.ships_left = Group()
        for ship_number in range(self.stats.ships_left):
            ship_left = Ship(self.ai_settings, self.screen, 0.5)
            ship_left.rect.x = 20 + ship_number * (ship_left.rect.width + 5)
            ship_left.rect.y = 20
            self.ships_left.add(ship_left)

    def show_score(self):
        """显示分数面板"""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.top_score_image, self.top_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.ships_left.draw(self.screen)


