import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """ Класс для управлениия снарядами. """

    def __init__(self, ai_game):
        """ Создаёт обьект снарядов в текущей позиции корабля. """
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color
        # Создание снаряда в позции (0,0) и назначение правильной позиции.
        self.rect = pygame.Rect(0, 0, self.settings.screen_width, self.settings.screen_height)
        self.rect.midtop = ai_game.ship.rect.midtop
        # позиция снаряда хранится в вещественном формате.
        self.y = float(self.rect.y)

    def update(self):
        """ Перемещает снаряд вверх по экрану """
        # обновление позиции снаряда в вещественном формате.
        self.y -= self.settings.bullet_speed
        # Обновление позиции прямоугольника
        self.rect.y = self.y

    def draw_bullet(self):
        """ Выыод снаряда на экран """
        pygame.draw.rect(self.screen, self.color, self.rect)
