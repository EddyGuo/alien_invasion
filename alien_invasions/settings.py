class Settings:
    """存储《外星人侵略》游戏的所有配置"""

    def __init__(self):
        """初始化游戏设置"""
        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.screen_bg_color = (30, 30, 30)
        self.ship_speed_factor = 1.5
