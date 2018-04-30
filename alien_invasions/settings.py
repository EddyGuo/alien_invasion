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
        self.bullet_width = 3
        self.bullet_height = 20
        self.bullet_color = (200, 200, 200)
        self.bullets_allowed = 10

        # 外星人设置
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        # -1表示向左移，1表示向右移
        self.fleet_direction = 1

