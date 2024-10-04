import pygame


class Game:
    # attributes
    screen = None
    clock = None
    running = None

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((720, 1280))
        self.clock = pygame.time.Clock()
        self.running = True

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.screen.fill("black")

            pygame.display.flip()
            self.clock.tick(60)
