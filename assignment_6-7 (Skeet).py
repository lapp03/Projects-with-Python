"""
File: assignment_6-7.py
Student: Alfredo Pena
Original Author: Br. Burton

This program implements an awesome version of skeet.
"""

import arcade
import math
import random
from abc import ABC
from abc import abstractmethod  

# These are Global constants to use throughout the game
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 500

RIFLE_WIDTH = 100
RIFLE_HEIGHT = 20
RIFLE_COLOR = arcade.color.DARK_RED

BULLET_RADIUS = 3
BULLET_COLOR = arcade.color.BLACK_OLIVE
BULLET_SPEED = 10

TARGET_RADIUS = 20
TARGET_COLOR = arcade.color.CARROT_ORANGE
TARGET_SAFE_COLOR = arcade.color.AIR_FORCE_BLUE
TARGET_SAFE_RADIUS = 15


class Point:
    #Initilizes the point at 0.0 (float)
    def __init__(self): 
       self.x = 0.0
       self.y = 0.0
       
       
class Velocity:
    #Initializes velocity at 0.0 (float)
    def __init__(self): 
       self.dx = 0.0
       self.dy = 0.0

class Rifle:
    """
    The rifle is a rectangle that tracks the mouse.
    """
    #Initializes the rifle at a 45 degree angle in the bottom left corner. 
    def __init__(self):
        self.center = Point()
        self.center.x = 0
        self.center.y = 0

        self.angle = 45
        
    #It draws the rifle on the screen. 
    def draw(self):
        arcade.draw_rectangle_filled(self.center.x, self.center.y, RIFLE_WIDTH, RIFLE_HEIGHT, RIFLE_COLOR, self.angle)


class FlyingObject (ABC):
    """
    Anything that moves across the screenplay.
    """
    
    def __init__(self):
        self.center = Point()
        self.velocity = Velocity()
        self.radius = TARGET_RADIUS
        self.alive = True
        
    #It moves the flying object according to its velocity. 
    def advance(self): 
        self.center.x += self.velocity.dx
        self.center.y += self.velocity.dy
    
    @abstractmethod 
    def draw(self):
        pass
    
    #Checks if the flying object is off screen limits and kills it. 
    def is_off_screen(self, screen_width, screen_height):
        if self.center.x > screen_width:
            self.alive = False
            
        elif self.center.y > screen_height:
            self.alive = False


class Bullet (FlyingObject, ABC):
    
    #Inherits all the attributes of a FlyingObject()
    def __init__(self):
        super().__init__()
    
    def draw(self):
        arcade.draw_circle_filled(self.center.x, self.center.y,BULLET_RADIUS,BULLET_COLOR)
    
    #It projects a bullet at a certain angle and speed. 
    def fire(self, angle):
        self.velocity.dx = math.cos(math.radians(angle)) * BULLET_SPEED
        self.velocity.dy = math.sin(math.radians(angle)) * BULLET_SPEED
                      

class Target(FlyingObject, ABC):
    """
    Anything that can be hit.
    """
    def __init__(self):
        super().__init__()
        self.center.x = 0
        self.center.y = random.randint(SCREEN_HEIGHT/2, SCREEN_HEIGHT)
        self.velocity.dx = random.randint(1,5)
        self.velocity.dy = random.randint(-2,5)
    
    @abstractmethod
    def draw(self):
        pass
    
    @abstractmethod 
    def hit(self):
        pass
        
        
        
class StandardTarget(Target, ABC):
    """
    Dead after one hit and worth one point.
    """
    
    def __init__(self):
        super().__init__()
    
    def draw(self):
        arcade.draw_circle_filled(self.center.x, self.center.y,TARGET_RADIUS,TARGET_COLOR)
    
    def hit(self):
        self.alive = False
        return 1


class StrongTarget (Target, ABC):
    """
    Dead after three hits and worth five points.
    """
    
    def __init__(self):
        super().__init__()
        self.lives = 3
        self.velocity.dx = random.randint(1,3)
        self.velocity.dy = random.randint(-2,3)

        
    def draw(self): 
        arcade.draw_circle_outline(self.center.x, self.center.y, self.radius, TARGET_COLOR)
        text_x = self.center.x - (self.radius / 2)
        text_y = self.center.y - (self.radius / 2)
        #lives = 3
        arcade.draw_text(repr(self.lives), text_x, text_y, TARGET_COLOR, font_size=20)
    
    def hit(self):
        if self.lives > 1:
            self.lives -= 1
            return 1
            
        else:
            self.alive = False
            return 5
 
 
class SafeTarget(Target, ABC):
    """
    Dead after one hit and takes off 10 point from score.
    """
    def __init__(self):
        super().__init__()
        
    def draw(self):
        arcade.draw_xywh_rectangle_filled(self.center.x, self.center.y,TARGET_SAFE_RADIUS, TARGET_SAFE_RADIUS, TARGET_SAFE_COLOR)
    
    def hit(self):
        self.alive = False
        return -10

    
class Game(arcade.Window):
    """
    This class handles all the game callbacks and interaction
    """

    def __init__(self, width, height):
        """
        Sets up the initial conditions of the game
        :param width: Screen width
        :param height: Screen height
        """
       
        super().__init__(width, height)

        self.rifle = Rifle()
        self.score = 0

        self.bullets = []

        self.targets = [] 

        arcade.set_background_color(arcade.color.WHITE)

    def on_draw(self):
        """
        Called automatically by the arcade framework.
        Handles the responsibility of drawing all elements.
        """

        #Clear the screen to begin drawing
        arcade.start_render()
        
        #Draw each object
        self.rifle.draw()

        for bullet in self.bullets:
            bullet.draw()

        for target in self.targets:
            target.draw()

        self.draw_score()

    def draw_score(self):
        """
        Puts the current score on the screen
        """
        
        score_text = "Score: {}".format(self.score)
        start_x = 10
        start_y = SCREEN_HEIGHT - 20
        arcade.draw_text(score_text, start_x=start_x, start_y=start_y, font_size=12, color=arcade.color.NAVY_BLUE)

    def update(self, delta_time):
        """
        Update each object in the game.
        :param delta_time: tells us how much time has actually elapsed
        """
        
        self.check_collisions()
        self.check_off_screen()
        
        #Decide if we should start a target
        if random.randint(1, 50) == 1:
            self.create_target()

        for bullet in self.bullets:
            bullet.advance()
        
        for target in self.targets:
            target.advance()


    def create_target(self):
        """
        Creates a new target of a random type and adds it to the list.
        """
        target_type = random.randint(1, 3)
        
        standardtarget = StandardTarget()
        safetarget = SafeTarget()
        strongtarget = StrongTarget()
        
        if target_type == 1:
            self.targets.append(standardtarget)
            
        if target_type == 2:
            self.targets.append(safetarget)
            
        if target_type == 3:
            self.targets.append(strongtarget)

    def check_collisions(self):
        """
        Checks to see if bullets have hit targets.
        Updates scores and removes dead items.
        """
        
        for bullet in self.bullets:
            for target in self.targets:
                
                # Make sure they are both alive before checking for a collision
                if bullet.alive and target.alive:
                    too_close = bullet.radius + target.radius

                    if (abs(bullet.center.x - target.center.x) < too_close and
                                abs(bullet.center.y - target.center.y) < too_close):
                        #It's a hit!
                        bullet.alive = False
                        self.score += target.hit()
                        
                        # We will wait to remove the dead objects until after we
                        # finish going through the list

        # Now, check for anything that is dead, and remove it

        self.cleanup_zombies()

    def cleanup_zombies(self):
        """
        Removes any dead bullets or targets from the list.
        """

        for bullet in self.bullets:
            if not bullet.alive:
                self.bullets.remove(bullet)

        for target in self.targets:
            if not target.alive:
                self.targets.remove(target)

    def check_off_screen(self):
        """
        Checks to see if bullets or targets have left the screen
        and if so, removes them from their lists.
        """
        for bullet in self.bullets:
            if bullet.is_off_screen(SCREEN_WIDTH, SCREEN_HEIGHT):
                self.bullets.remove(bullet)

        for target in self.targets:
            if target.is_off_screen(SCREEN_WIDTH, SCREEN_HEIGHT):
                self.targets.remove(target)

    def on_mouse_motion(self, x: float, y: float, dx: float, dy: float):
        #Set the rifle angle in degrees
        self.rifle.angle = self._get_angle_degrees(x, y)

    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):
        #Fire!
        angle = self._get_angle_degrees(x, y)

        bullet = Bullet()
        bullet.fire(angle)

        self.bullets.append(bullet)

    def _get_angle_degrees(self, x, y):
        """
        Gets the value of an angle (in degrees) defined
        by the provided x and y.
        """

        # get the angle in radians
        angle_radians = math.atan2(y, x)
        
        # convert to degrees
        angle_degrees = math.degrees(angle_radians)

        return angle_degrees


# Creates the game and starts it going
window = Game(SCREEN_WIDTH, SCREEN_HEIGHT)
arcade.run()

