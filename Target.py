import pygame
from GlobalScreen import screen
from GameObject import GameObject

class Target(GameObject):
    def __init__(self, x: float, y: float):
        super().__init__(x, y)
        self.dx: float = 0.0
        self.dy: float = 0.0
        self.speed: float = 1.0  # Movement speed per frame

    def input_handler(self):
        keys = pygame.key.get_pressed()
        self.dx = 0.0
        self.dy = 0.0
        if keys[pygame.K_LEFT]:
            self.dx = -self.speed
        if keys[pygame.K_RIGHT]:
            self.dx = self.speed
        if keys[pygame.K_UP]:
            self.dy = -self.speed
        if keys[pygame.K_DOWN]:
            self.dy = self.speed

    def Move(self):
        self.x += self.dx
        self.y += self.dy

    def Update(self):
        self.Move()

    def Draw(self):
        pygame.draw.circle(screen, (255, 0, 0), (int(self.x), int(self.y)), 7)