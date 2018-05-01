class Settings:
    """存储《外星人侵略》游戏的所有配置"""

    def __init__(self):
        """初始化游戏静态设置"""
        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.screen_bg_color = (30, 30, 30)

        # 字体设置
        self.score_font_color = (255, 255, 255)
        self.level_font_color = (255, 255, 255)

        self.score_font_size = 48
        self.level_font_size = 56

        # 飞船设置
        self.ship_limit = 1

        #  子弹设置
        self.bullet_width = 8
        self.bullet_height = 20
        self.bullet_color = (200, 200, 200)
        self.bullets_allowed = 10
        self.bullets_vanish = False

        # 外星人设置
        self.fleet_drop_speed = 10

        # 游戏节奏
        self.speedup_scale = 1.2
        # 外星人点数提高速度
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """初始化随游戏进行而变化的设置"""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 2
        self.alien_speed_factor = 1
        # -1表示向左移，1表示向右移
        self.fleet_direction = 1

        # 计分
        self.alien_points = 10

    def increase_speed(self):
        """提高速度和外星人点数"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points *= self.score_scale


