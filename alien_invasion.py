import sys
import pygame
from settings import Settings


class AlienInvasion:
    """ Класс для управления ресурсами и поведением игры. """

    def __init__(self):
        """ Инициализирует игру и создаёт игровые ресурсы. """
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        pygame.display.set_caption('Alien Invasion')

        # назначение цвета фона
        self.bg_color = (230, 230, 230)

    def run_game(self):
        """ Запуск основного цикла """
        while True:
        # отслеживание событий клавиатуры и мыши.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # При каждом проходе цыкла перерисовывается экран
            self.screen.fill(self.settings.bg_color)

            # Отображение последнего прорисованого экрана
            pygame.display.flip()


if __name__ == '__main__':
    # создание экземпляра и запуска игры.
    ai = AlienInvasion()
    ai.run_game()
