import pygame


class Note:
    def _init_(self, x, y, width, height, color):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.hit = False

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)

    def move(self, speed):
        self.rect.y += speed

    def is_off_screen(self, screen_height):
        return self.rect.y > screen_height
