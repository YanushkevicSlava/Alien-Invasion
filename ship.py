import pygame



class Ship():
    """ Класс для управления кораблём. """
    def __init__(self, ai_game):
        """ Иницилизиирует корабль и задаёт его начальную позицию. """
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # загружает изображение корабля и получает прямоугольник.
        self.image = pygame.image.load('images/rocket.bmp')
        self.rect = self.image.get_rect()
        # Каждый новый корабль появляется у нижнего края экрана.
        self.rect.midbottom = self.screen_rect.midbottom
        # Сохранение вещественной координаты центра коробля.
        self.x = float(self.rect.x)
        # флаг перемещения
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """ Обновляет позцию корабля с учётом флага. """

        # Обновляется атрибут х, не rect.
        if self.moving_right:
            self.rect.x += self.settings.ship_speed
        if self.moving_left:
            self.rect.x -= self.settings.ship_speed
        # # Обновление атрибута rect на основании self.x.
        # self.rect.x = self.x

    def blitme(self):
        """ Рисует корабль в текущей позиции. """
        self.screen.blit(self.image, self.rect)

