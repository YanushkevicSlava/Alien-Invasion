class Settings():
    """ Класс для хранения всех настроек игры Alien Invasion """

    def __init__(self):
        """ Инцилизирует настройки игры """
        # параметры экрана
        self.screen_width = 1200
        self.screen_height = 700
        self.bg_color = (230, 230, 230)
        # настройки корабля
        self.ship_speed = 1.5
        # Параметры снаряда
        self.bullet_speed = 2
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (250, 0, 0)
        self.bullets_allowed = 3
