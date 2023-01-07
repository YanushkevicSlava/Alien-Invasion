import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """ Класс представляющий одного пришельца """
    def __init__(self, ai_game):
        """ Инициализирует пришельца и задаёт ег начальную позицию """
        super().__init__()
        self.screen = ai_game.screen

        # Загрузка изображения пришельца и назначение атрибута rect.
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # каждый новый пришелец появляется в левом верхнемуглу экрана.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # сохранение точной горизонтальной позиции пришельца.
        self.x = float(self.rect.x)