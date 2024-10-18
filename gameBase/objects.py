import pygame


class GameObject:
    def __init__(self, x, y, width, height, color):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color

    def update(self, dt):
        pass

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)