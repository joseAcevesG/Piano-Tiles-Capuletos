import pygame


class Note:
    def __init__(self, rect, color):
        """
        Inicializa una nota con un rectángulo y un color específicos.
        :param rect: pygame.Rect, define la posición y tamaño de la nota.
        :param color: tuple, define el color de la nota como una tupla RGB.
        """
        self.rect = rect  # Rectángulo definido por pygame.Rect
        self.color = color  # Color de la nota, ejemplo: (255, 0, 0) para rojo

    def draw(self, screen):
        """
        Dibuja la nota en la pantalla proporcionada.
        :param screen: Superficie de pygame donde se dibujará la nota.
        """
        pygame.draw.rect(screen, self.color, self.rect)

    def move(self, speed):
        """
        Mueve la nota hacia abajo según la velocidad especificada.
        :param speed: int, velocidad con la que la nota se mueve hacia abajo.
        """
        self.rect.y += speed  # Mueve la nota hacia abajo en la pantalla


# Ejemplo de uso:
def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    clock = pygame.time.Clock()

    # Crear una nota, especificando posición inicial, tamaño y color
    note = Note(pygame.Rect(100, 0, 50, 150), (255, 0, 0))

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0, 0, 0))  # Limpia la pantalla con color negro
        note.draw(screen)  # Dibuja la nota
        note.move(5)  # Mueve la nota hacia abajo en la pantalla a una velocidad de 5
        pygame.display.flip()  # Actualiza el contenido de la pantalla
        clock.tick(30)  # Mantiene el juego a 30 fps

    pygame.quit()


if __name__ == "__main__":
    main()
