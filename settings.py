class Settings:
    """ Класс для хранения всех настроек игры Alien Invasion """

    def __init__(self):
        """ Инцилизирует статические настройки игры """
        # параметры экрана
        self.screen_width = 1200
        self.screen_height = 700
        self.bg_color = (230, 230, 230)
        # настройки корабля
        self.ship_speed = 1.5
        self.ship_limit = 3
        # Параметры снаряда
        self.bullet_speed = 1.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (250, 0, 0)
        self.bullets_allowed = 3
        # Настройки пришельцев
        self.alien_speed = 0.05
        self.fleet_drop_speed = 10

        # Темп ускорения игры.
        self.speedup_scale = 1.1

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Инициализирует настройки, изменяющиеся в ходе игры."""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3.0
        self.alien_speed_factor = 1.0

        # fleet_direction = 1 обозначает движение в право; a -1 - влево.
        self.fleet_direction = 1

        # Подсчёт очков.
        self.alien_points = 50

    def increase_speed(self):
        """Увеличивает настройки скорости."""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
