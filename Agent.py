import pygame
import Globals
from GameObject import GameObject
from Target import Target


class Agent(GameObject):
    tmem=300
    def __init__(self, x: float, y: float):
        super().__init__(x, y)
        #self.velocity_x = velocity_x
        #self.velocity_y = velocity_y
        self._losRange=100
        self.lsx=None#last sighting x position
        self.lsy=None#last sighting y postion
        self.lst=None#last sighting time

    def Update(self):
        #self.x += self.velocity_x
        #self.y += self.velocity_y
        self.CanSeeTarget()


    def Draw(self):
        if self.CanSeeTarget():
            color = (255, 255, 0)
        else:
            color=(255, 255, 255)
        pygame.draw.circle(Globals.screen, color, (int(self.x), int(self.y)), 5)
        my_font = pygame.font.Font(None, 30)
        text_surface = my_font.render(f"{self.lsx}, {self.lsy},{self.lst}", True, (255, 255, 255))
        Globals.screen.blit(text_surface, (0, 0))

    def CanSeeTarget(self):
        target=Target.get_instance()
        if(self._losRange**2>(self.x-target.x)**2+(self.y-target.y)**2):
            self.lsx=target.x
            self.lsy=target.y
            self.lst=Globals.frame_count
            return True
        else:
            return False