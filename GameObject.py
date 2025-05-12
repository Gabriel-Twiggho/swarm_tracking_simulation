from abc import ABC, abstractmethod

class GameObject(ABC):
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    @abstractmethod
    def Update(self):
        pass

    @abstractmethod
    def Draw(self, screen):
        pass