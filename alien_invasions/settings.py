class Settings:
    """存储《外星人侵略》游戏的所有配置"""

    def __init__(self):
        """初始化游戏设置"""
        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.screen_bg_color = (30, 30, 30)

        # 飞船设置
        self.ship_speed_factor = 1.5

        #  子弹设置
        self.bullet_speed_factor = 1.5
        self.bullet_width = 5
        self.bullet_height = 20
        self.bullet_color = (200, 200, 200)
