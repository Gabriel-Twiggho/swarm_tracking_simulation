import pygame
from GlobalScreen import screen
from GameObject import GameObject
from Target import Target

class Agent(GameObject):
    def __init__(self, x: float, y: float):
        super().__init__(x, y)
        #self.velocity_x = velocity_x
        #self.velocity_y = velocity_y
        self._losRange=100

    def Update(self):
        #self.x += self.velocity_x
        #self.y += self.velocity_y
        self.CanSeeTarget()


    def Draw(self):
        if self.CanSeeTarget():
            color = (255, 255, 0)
        else:
            color=(255, 255, 255)
        pygame.draw.circle(screen, color, (int(self.x), int(self.y)), 5)

    def CanSeeTarget(self):
        target=Target.get_instance()
        if(self._losRange**2>(self.x-target.x)**2+(self.y-target.y)**2):
            return True
        else:
            return False