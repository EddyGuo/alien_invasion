import os

class GameStats():
    """跟踪统计信息"""

    def __init__(self, ai_settings):
        """初始化统计信息"""
        self.ai_settings = ai_settings
        self.game_active = False
        self.top_score = 0
        self.data_read()
        self.reset_stats()

    def reset_stats(self):
        """重置统计信息"""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1

    def data_read(self):
        """读取游戏数据"""
        # 判断数据文件是否存在，若存在读取数据，若不存在，写入初始数据
        if os.path.isfile('data.txt'):
            with open('data.txt', 'r', encoding='utf-8') as data_file:
                data = data_file.read()
                self.top_score = int(data)
        else:
            with open('data.txt', 'w', encoding='utf-8') as data_file:
                data_file.write(str(self.top_score))
