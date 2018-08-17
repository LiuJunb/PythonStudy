class Settings:
    """存储《外星人入侵》的所有的设置类"""
    def __init__(self):
        """初始化游戏的设置"""
        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        self.alien_caption = '外星人入侵'

        # 飞船的设置
        self.ship_speed_factor = 5.5  # 飞船移动速度
        self.ship_limit = 3

        self.sleep = 1  # 新增飞船的时间
        # 子弹设置
        self.bullet_speed_factor = 10
        self.bullet_width = 10
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullet_allowed = 3

        # 外星人
        self.alien_spend_factor = 1
        self.fleet_drop_speed = 100

        # fleet_direction为1表示向右移动，为-1表示向左
        self.fleet_direction = 1










