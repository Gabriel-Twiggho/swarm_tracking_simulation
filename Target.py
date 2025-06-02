import pygame
import Globals
from GameObject import GameObject
import math

class Target(GameObject):
    _instance = None  # Static variable to hold the singleton instance

    # Static method to get the singleton instance
    @staticmethod
    def get_instance(x: float = None, y: float = None):
        if Target._instance is None:
            # Use default initial positions from Globals if not provided
            if x is None:
                x = Globals.TARGET_AUTO_PATH_RECT["initial_x"]
            if y is None:
                y = Globals.TARGET_AUTO_PATH_RECT["initial_y"]
            Target._instance = Target(x, y)
        return Target._instance

    def __init__(self, x: float, y: float):
        if Target._instance is not None:
            raise Exception("This class is a singleton!")
        super().__init__(x, y)
        self.dx: float = 0.0
        self.dy: float = 0.0
        self.speed: float = 2.0  # Movement speed per frame

        #automated path attributes
        self.control_mode = Globals.TARGET_CONTROL_MODE # Set initial control mode
        self._path_points: list[tuple[float, float]] = []
        self._current_path_target_index: int = 0

        if self.control_mode == "AUTO":
            rect_details = Globals.TARGET_AUTO_PATH_RECT
            self.set_rectangular_path(
                rect_details["x"],
                rect_details["y"],
                rect_details["width"],
                rect_details["height"]
            )

    def set_rectangular_path(self, top_left_x: float, top_left_y: float, width: float, height: float):
        """Sets up a rectangular path for the target and switches to AUTO mode."""
        self._path_points = [
            (top_left_x, top_left_y),                            # Top-left
            (top_left_x + width, top_left_y),                    # Top-right
            (top_left_x + width, top_left_y + height),           # Bottom-right
            (top_left_x, top_left_y + height)                    # Bottom-left
        ]
        self._current_path_target_index = 0
        #start of the path
        if self._path_points:
            self.x, self.y = self._path_points[0]

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

    def _move_automated(self):

        target_x, target_y = self._path_points[self._current_path_target_index]

        #calc distance to target location
        dir_x = target_x - self.x
        dir_y = target_y - self.y
        
        distance_to_target = math.sqrt(dir_x**2 + dir_y**2)

        # Check if close enough to the target point
        if distance_to_target < self.speed: # If closer than one step, snap and switch
            self.x = target_x
            self.y = target_y
            self._current_path_target_index = (self._current_path_target_index + 1) % len(self._path_points)
        else:
            #move towards the target point
            self.dx = (dir_x / distance_to_target) * self.speed
            self.dy = (dir_y / distance_to_target) * self.speed
            self.x += self.dx
            self.y += self.dy
    
    def _enforce_bounds(self):
        #clamp x positio
        if self.x < Globals.TOPLEFT_X:
            self.x = Globals.TOPLEFT_X
        elif self.x > Globals.BOTTOMRIGHT_X:
            self.x = Globals.BOTTOMRIGHT_X
        
        #clamp y position
        if self.y < Globals.TOPLEFT_Y:
            self.y = Globals.TOPLEFT_Y
        elif self.y > Globals.BOTTOMRIGHT_Y:
            self.y = Globals.BOTTOMRIGHT_Y

    def Update(self):
        if self.control_mode == "MANUAL":
            self.input_handler()
            self.Move()
        elif self.control_mode == "AUTO":
            self._move_automated()
        
        self._enforce_bounds() 

    def Draw(self):
        pygame.draw.circle(Globals.screen, (255, 0, 0), (int(self.x), int(self.y)), 7)

        # Optional: Draw the automated path for debugging
        if self.control_mode == "AUTO" and self._path_points:
            pygame.draw.lines(Globals.screen, (100, 100, 100), True, self._path_points, 1)