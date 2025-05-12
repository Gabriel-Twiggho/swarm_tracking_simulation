import pygame
from GlobalScreen import screen
from GameObject import GameObject

class Target(GameObject):
    _instance = None  # Static variable to hold the singleton instance

    # Static method to get the singleton instance
    @staticmethod
    def get_instance(x: float = None, y: float = None):
        if Target._instance is None:
            if x is None or y is None:
                raise ValueError("You must provide initial coordinates the first time.")
            Target._instance = Target(x, y)
        return Target._instance

    def __init__(self, x: float, y: float):
        if Target._instance is not None:
            raise Exception("This class is a singleton!")
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
        self.input_handler()
        self.Move()

    def Draw(self):
        pygame.draw.circle(screen, (255, 0, 0), (int(self.x), int(self.y)), 7)
