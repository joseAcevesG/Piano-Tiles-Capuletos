import pygame

from logic.gameManager import GameManager


class Display:
    def _init_(self, screen, game_manager):
        self.screen = screen
        self.game_manager = game_manager
        self.clock = pygame.time.Clock()
        self.running = True
        self.font = pygame.font.Font(None, 48)
        self.state = "start"  # Estados: 'start', 'playing', 'game_over'

    def draw_lines(self):
        for i in range(1, 4):
            pygame.draw.line(
                self.screen,
                (200, 200, 200),
                (i * self.game_manager.note_width, 0),
                (i * self.game_manager.note_width, self.game_manager.screen_height),
                2,
            )

    def show_start_screen(self):
        self.screen.fill((255, 255, 255))
        title_text = self.font.render("Piano Tiles", True, (0, 0, 0))
        instruction_text = self.font.render(
            "Presiona cualquier tecla para comenzar", True, (0, 0, 0)
        )
        self.screen.blit(
            title_text,
            (
                self.screen.get_width() // 2 - title_text.get_width() // 2,
                self.screen.get_height() // 2 - 60,
            ),
        )
        self.screen.blit(
            instruction_text,
            (
                self.screen.get_width() // 2 - instruction_text.get_width() // 2,
                self.screen.get_height() // 2,
            ),
        )
        pygame.display.flip()

    def show_game_over_screen(self):
        self.screen.fill((255, 255, 255))
        game_over_text = self.font.render("¡Juego Terminado!", True, (255, 0, 0))
        score_text = self.font.render(
            f"Puntaje final: {self.game_manager.score}", True, (0, 0, 0)
        )
        instruction_text = self.font.render(
            "Presiona cualquier tecla para reiniciar", True, (0, 0, 0)
        )
        self.screen.blit(
            game_over_text,
            (
                self.screen.get_width() // 2 - game_over_text.get_width() // 2,
                self.screen.get_height() // 2 - 60,
            ),
        )
        self.screen.blit(
            score_text,
            (
                self.screen.get_width() // 2 - score_text.get_width() // 2,
                self.screen.get_height() // 2,
            ),
        )
        self.screen.blit(
            instruction_text,
            (
                self.screen.get_width() // 2 - instruction_text.get_width() // 2,
                self.screen.get_height() // 2 + 60,
            ),
        )
        pygame.display.flip()

    def run(self):
        while self.running:
            self.clock.tick(60)
            if self.state == "start":
                self.show_start_screen()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.running = False
                    if event.type == pygame.KEYDOWN:
                        self.state = "playing"
            elif self.state == "playing":
                self.screen.fill((255, 255, 255))
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.running = False
                    if event.type == pygame.KEYDOWN:
                        self.game_manager.check_hit(event.key)

                self.game_manager.update_notes()
                if self.game_manager.game_over:
                    self.state = "game_over"
                else:
                    for note in self.game_manager.notes:
                        note.draw(self.screen)

                    self.draw_lines()

                    score_text = self.font.render(
                        f"Puntaje: {self.game_manager.score}", True, (0, 0, 0)
                    )
                    self.screen.blit(score_text, (10, 10))

                    pygame.display.flip()
            elif self.state == "game_over":
                self.show_game_over_screen()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.running = False
                    if event.type == pygame.KEYDOWN:
                        # Reiniciamos el GameManager y volvemos al estado 'playing'
                        self.game_manager = GameManager(
                            screen_width=self.game_manager.screen_width,
                            screen_height=self.game_manager.screen_height,
                            speed=self.game_manager.speed,
                        )
                        self.state = "playing"
            else:
                self.running = False