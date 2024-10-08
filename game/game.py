import pygame

from logic.gameManager import GameManager
from ui.display import Display


class Game:
    def _init_(self):
        pygame.init()
        self.screen_width = 800
        self.screen_height = 600
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.game_manager = GameManager(
            screen_width=self.screen_width, screen_height=self.screen_height, speed=5
        )
        self.display = Display(self.screen, self.game_manager)

    def run(self):
        self.display.run()
        pygame.quit()


# if __name__ == "__main__":
#     game = Game()
#     game.run()