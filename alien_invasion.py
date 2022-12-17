import sys
import pygame


class AlienInvasion:
    """ Класс для управления ресурсами и поведением игры. """

    def __init__(self):
        """ Инициализирует игру и создаёт игровые ресурсы. """
        pygame.init()

        self.screen = pygame.display.set_mode((1200, 700))
        pygame.display.set_caption('Alien Invasion')

    def run_game(self):
        """ Запуск основного цикла """
        while True:
        # отслеживание событий клавиатуры и мыши.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

        # Отображение последнего прорисованого экрана
            pygame.display.flip()


if __name__ == '__main__':
    # создание экземпляра и запуска игры.
    ai = AlienInvasion()
    ai.run_game()
