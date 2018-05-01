import pygame.font


class Scoreboard:
    """得分信息"""

    def __init__(self, ai_settings, stats, screen):
        """初始化得分"""
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats

        # 得分信息字体
        self.font_color = ai_settings.score_font_color
        self.font_size = ai_settings.score_font_size
        self.font = pygame.font.SysFont(None, self.font_size)
        self.level_font_color = ai_settings.level_font_color
        self.level_font_size =  ai_settings.level_font_size
        self.level_font = pygame.font.SysFont(None, self.level_font_size)

        # 准备得分图像
        self.prep_top_score()
        self.prep_score()
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
        self.level_image = self.level_font.render(level_str, True, self.level_font_color)

        # 将等级放在中上
        self.level_rect = self.level_image.get_rect()
        self.level_rect.centerx = self.screen_rect.centerx
        self.level_rect.top = self.screen_rect.top + 20

    def show_score(self):
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.top_score_image, self.top_score_rect)
        self.screen.blit(self.level_image, self.level_rect)


