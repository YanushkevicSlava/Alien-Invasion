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
