import pygame

class Display:
    def __init__(self, screen, game_manager):
        self.screen = screen
        self.game_manager = game_manager
        self.clock = pygame.time.Clock()

    def run(self):
        running = True
        while running:
            self.clock.tick(60)
            self.screen.fill((255, 255, 255))  # Fondo blanco

            # Manejar eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    self.game_manager.check_hit(event.key)

            # Actualizar y dibujar notas
            self.game_manager.update_notes()
            for note in self.game_manager.notes:
                note.draw(self.screen)

            pygame.display.flip()
