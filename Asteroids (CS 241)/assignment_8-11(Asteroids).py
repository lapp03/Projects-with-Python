"""
File: assignment_8-11.py
Student: Alfredo Peña
Original Author: Br. Burton

This program implements the asteroids game.
"""

import arcade
import math
import random
from abc import ABC
from abc import abstractmethod 

###########################GLOBAL VARIABLES############################
"""
These are Global constants to use throughout the game
"""

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

SHIP_TURN_AMOUNT = 3
SHIP_THRUST_AMOUNT = 0.25
SHIP_RADIUS = 30

BULLET_RADIUS = 30
BULLET_SPEED = 10
BULLET_LIFE = 60
BULLET_COLOR = arcade.color.CARROT_ORANGE

INITIAL_ROCK_COUNT = 5

BIG_ROCK_SPIN = 1
BIG_ROCK_SPEED = 1.5
BIG_ROCK_RADIUS = 15

MEDIUM_ROCK_SPIN = -2
MEDIUM_ROCK_RADIUS = 5
MEDIUM_ROCK_SPEED = 3

SMALL_ROCK_SPIN = 5
SMALL_ROCK_RADIUS = 2
SMALL_ROCK_SPEED = 4.5

##################################GLOBAL CLASSES###############################

class Point:
    def __init__(self):       #Initilizes the point at 0.0 (float)
        self.x = 0.0
        self.y = 0.0
             
class Velocity:               #Initializes velocity at 0.0 (float)
    def __init__(self): 
        self.dx = 0.0
        self.dy = 0.0

class FlyingObject(ABC):      #Anything that moves across the screenplay.
    def __init__(self):
        self.center = Point()
        self.velocity = Velocity()
        self.radius = 0
        self.alive = True
        self.angle = 0
        self.speed = 0
        self.hits = 0
    
    def advance(self):        #It moves the flying object according to its velocity. 
        self.center.x += self.velocity.dx
        self.center.y += self.velocity.dy
    
    @abstractmethod
    def draw(self):
        pass
        
    def wrap(self):          #Checks if the flying object is off screen limits and makes it appear on the other side of the screen.  
        if self.center.x > (SCREEN_WIDTH + 50):
            self.center.x = -50
        
        elif self.center.x < -50:
            self.center.x = (SCREEN_WIDTH + 50)
            
        elif self.center.y > (SCREEN_HEIGHT + 50):
            self.center.y = -50
        
        elif self.center.y < -50:
            self.center.y = (SCREEN_HEIGHT + 50)

class Bullet (FlyingObject):
    def __init__(self, x, y, angle):    
        super().__init__()    #Inherits all the attributes of a FlyingObject()
        self.center.x = x
        self.center.y = y
        self.radius = BULLET_RADIUS
        self.angle = angle
        self.lives = 0
    
    def draw(self):
        img = "laser.png"
        texture = arcade.load_texture(img)

        width = texture.width
        height = texture.height
        alpha = 1 

        x = self.center.x
        y = self.center.y

        arcade.draw_texture_rectangle(x, y, width, height, texture, self.angle, alpha)
        
        self.lives += 1
        
        if self.lives == 60:
            self.alive = False
    
    def fire(self):    #It projects a bullet at a certain angle and speed.
        self.velocity.dx = math.cos(math.radians(self.angle)) * BULLET_SPEED
        self.velocity.dy = math.sin(math.radians(self.angle)) * BULLET_SPEED
    
class Ship(FlyingObject):
    def __init__(self):
        super().__init__()
        self.center.x = SCREEN_WIDTH - (SCREEN_WIDTH/2)
        self.center.y = SCREEN_HEIGHT - (SCREEN_HEIGHT/2)
        self.radius = SHIP_RADIUS

    def draw(self):
        img = "ship.png"
        texture = arcade.load_texture(img)

        width = texture.width
        height = texture.height
        alpha = 1 

        x = self.center.x
        y = self.center.y

        arcade.draw_texture_rectangle(x, y, width, height, texture, self.angle, alpha)
    
    def hit(self):
        self.alive = False
        return 10

    def thrust(self):
        self.speed += SHIP_THRUST_AMOUNT
        self.velocity.dx = math.cos(math.radians(self.angle)) * self.speed 
        self.velocity.dy = math.sin(math.radians(self.angle)) * self.speed 
    
    def slow_down(self):
        self.speed -= SHIP_THRUST_AMOUNT
        self.velocity.dx = math.cos(math.radians(self.angle)) * self.speed
        self.velocity.dy = math.sin(math.radians(self.angle)) * self.speed

class Asteroid(FlyingObject, ABC):
    def __init__(self):           #Anything that can be hit.
        super().__init__()
        self.center.x = random.randint(1,SCREEN_WIDTH)
        self.center.y = random.randint(1,SCREEN_HEIGHT)
        self.spin = 0
        angle = random.randint(1,100)
        self.velocity.dx = math.cos(math.radians(angle)) * BIG_ROCK_SPEED
        self.velocity.dy = math.sin(math.radians(angle)) * BIG_ROCK_SPEED
    
    @abstractmethod
    def rotate(self):            #It makes the asteroid spin a certain speeds. 
        pass
    
    @abstractmethod
    def draw(self):              #Call the right image to display on the screen
        pass
    
    @abstractmethod
    def hit(self,parent):        #Makes the asteroid separate into smaller parts or disappear after colliding. 
        pass

class BigAsteroid(Asteroid):
    def __init__(self):
        super().__init__()
        self.radius = BIG_ROCK_RADIUS
    
    def draw(self):
        img = "big.png"
        texture = arcade.load_texture(img)

        width = texture.width
        height = texture.height
        alpha = 1 

        x = self.center.x
        y = self.center.y

        arcade.draw_texture_rectangle(x, y, width, height, texture, self.angle, alpha)
    
    def hit(self,parent):               #After it gets hit, creates two medium rocks and small one. 
        a = MediumAsteroid()
        angle1 = random.randint(1,100)
        a.spin = 0
        a.velocity.dx = math.cos(math.radians(angle1)) * MEDIUM_ROCK_SPEED
        a.velocity.dy = math.sin(math.radians(angle1)) * MEDIUM_ROCK_SPEED
        
        b = MediumAsteroid()
        angle2 = random.randint(1,100)
        b.spin = 5
        b.velocity.dx = math.cos(math.radians(angle2)) * MEDIUM_ROCK_SPEED
        b.velocity.dy = math.sin(math.radians(angle2)) * MEDIUM_ROCK_SPEED
        
        c = SmallAsteroid()
        angle3 = random.randint(1,100)
        c.spin = 4
        c.velocity.dx = math.cos(math.radians(angle3)) * SMALL_ROCK_SPEED
        c.velocity.dy = math.sin(math.radians(angle3)) * SMALL_ROCK_SPEED
        
        self.babies = [a,b,c]
        for baby in self.babies:
            baby.center.x = parent.center.x
            baby.center.y = parent.center.y
            
        return self.babies
    
    def rotate(self):
        self.angle += BIG_ROCK_SPIN
        return self.angle
          

class MediumAsteroid(Asteroid):        #After it gets hit, creates two  small rocks.
    def __init__(self):
        super().__init__()
    
    def draw(self):
        img = "medium.png"
        texture = arcade.load_texture(img)

        width = texture.width
        height = texture.height
        alpha = 1 

        x = self.center.x
        y = self.center.y

        arcade.draw_texture_rectangle(x, y, width, height, texture, self.angle, alpha)
    
    def hit(self,parent):
        a = SmallAsteroid()
        angle2 = random.randint(1,100)
        a.spin = 5
        a.velocity.dx = math.cos(math.radians(angle2)) * SMALL_ROCK_SPEED
        a.velocity.dy = math.sin(math.radians(angle2)) * SMALL_ROCK_SPEED
        
        b = SmallAsteroid()
        angle3 = random.randint(1,100)
        b.spin = 4
        b.velocity.dx = math.cos(math.radians(angle3)) * SMALL_ROCK_SPEED
        b.velocity.dy = math.sin(math.radians(angle3)) * SMALL_ROCK_SPEED
        
        self.babies = [a,b]
        for baby in self.babies:
            baby.center.x = parent.center.x
            baby.center.y = parent.center.y
        
        return self.babies
    
    def rotate(self):
        self.angle += MEDIUM_ROCK_SPIN
        return self.angle
        
class SmallAsteroid(Asteroid):
    def __init__(self):
        super().__init__()
    
    def draw(self):
        img = "small.png"
        texture = arcade.load_texture(img)

        width = texture.width
        height = texture.height
        alpha = 1 

        x = self.center.x
        y = self.center.y

        arcade.draw_texture_rectangle(x, y, width, height, texture, self.angle, alpha)
    
    def rotate(self):
        self.angle += SMALL_ROCK_SPIN
        return self.angle
    
    def hit(self,parent):      
        return []
    
#########################################GAME CLASS######################################
"""
This class handles all the game callbacks and interaction. This class will then call the
appropriate functions of each of the above classes.
"""

class Game(arcade.Window):
    def __init__(self, width, height):
        """
        Sets up the initial conditions of the game
        :param width: Screen width
        :param height: Screen height
        """
        super().__init__(width, height)
        
        self.held_keys = set()
        
        self.ship = Ship()
        
        self.score = 0

        self.bullets = []

        self.asteroids = []
        
        self.create_target()

    def on_draw(self):
        """
        Called automatically by the arcade framework.
        Handles the responsibility of drawing all elements.
        """
        
        arcade.start_render()  #Clears the screen to begin drawing
        
        background = arcade.load_texture("universe.jpg")
        
        arcade.draw_texture_rectangle(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2,
                                      SCREEN_WIDTH, SCREEN_HEIGHT, background)
        self.ship.draw()
        
        for bullet in self.bullets: 
            bullet.draw()

        for asteroid in self.asteroids:
            asteroid.draw()

        self.draw_score()
    
    def draw_score(self):     #Draws the score un the upper left side of the screen. 
        score_text = "Score: {}".format(self.score)
        start_x = 10
        start_y = SCREEN_HEIGHT - 20
        arcade.draw_text(score_text, start_x=start_x, start_y=start_y, font_size=12, color=arcade.color.WHITE)

    def update(self, delta_time):
        """
        Update each object in the game.
        :param delta_time: tells us how much time has actually elapsed
        """
        self.check_keys()
        self.check_collisions()

        for bullet in self.bullets:
            bullet.advance()
            bullet.wrap()
            
        for asteroid in self.asteroids:
            asteroid.advance()
            asteroid.wrap()
            asteroid.rotate()
        
        self.ship.wrap()
        self.ship.advance()
        
    def create_target(self):    #It creates the first five bigger asteroids. 
        for asteroids in range(INITIAL_ROCK_COUNT):
            big = BigAsteroid()
            self.asteroids.append(big)
        
    def check_collisions(self):
        for bullet in self.bullets:    #If a bullet and asteroid collide, it adds five points to the score and kills the bullet and the asteroid. 
            for asteroid in self.asteroids:
                if bullet.alive and asteroid.alive:
                    too_close = bullet.radius + asteroid.radius
                    if (abs(bullet.center.x - asteroid.center.x) < too_close and
                        abs(bullet.center.y - asteroid.center.y) < too_close):
                        bullet.alive = False
                        asteroid.alive = False
                        babies = asteroid.hit(asteroid)
                        self.asteroids.extend(babies)
                        self.score += 5
            
        for asteroid in self.asteroids:        #If the ship gets hit, it returns it to the beginning of the game and restart the score. 
            if self.ship.alive and asteroid.alive:
                too_close = self.ship.radius + asteroid.radius
                if (abs(self.ship.center.x - asteroid.center.x) < too_close and
                    abs(self.ship.center.y - asteroid.center.y) < too_close):
                    self.score = 0
                    self.ship.center.x = SCREEN_WIDTH - (SCREEN_WIDTH/2)
                    self.ship.center.y = SCREEN_HEIGHT - (SCREEN_HEIGHT/2)
                    
        self.cleanup_zombies()
    
    def cleanup_zombies(self):
        """
        Removes any dead bullets or targets from the list.
        """
        for bullet in self.bullets:
            if not bullet.alive:
                self.bullets.remove(bullet)

        for asteroid in self.asteroids:    
            if asteroid.alive == False:
                self.asteroids.remove(asteroid)
                
        if self.ship.alive == False:
            self.ship.center.x = SCREEN_WIDTH - (SCREEN_WIDTH/2)
            self.ship.center.y = SCREEN_HEIGHT - (SCREEN_HEIGHT/2)
           
    def check_keys(self):
        """
        This function checks for keys that are being held down.
        """
        if arcade.key.LEFT in self.held_keys:
            self.ship.angle += SHIP_TURN_AMOUNT    

        if arcade.key.RIGHT in self.held_keys:
            self.ship.angle -= SHIP_TURN_AMOUNT

        if arcade.key.UP in self.held_keys:
            self.ship.thrust()
            self.ship.advance()
        
        if arcade.key.UP not in self.held_keys:
            self.ship.speed =- SHIP_THRUST_AMOUNT
            
        if arcade.key.DOWN in self.held_keys:
            self.ship.center.y += -3
            self.ship.slow_down()
            
            
    def on_key_press(self, key: int, modifiers: int):
        """
        Puts the current key in the set of keys that are being held.
        """
        if self.ship.alive:
            self.held_keys.add(key)

            if key == arcade.key.SPACE:
                bullet = Bullet(self.ship.center.x, self.ship.center.y, self.ship.angle)
                bullet.fire()
                self.bullets.append(bullet)

    def on_key_release(self, key: int, modifiers: int):
        """
        Removes the current key from the set of held keys.
        """
        if key in self.held_keys:
            self.held_keys.remove(key)
    
    def _get_angle_degrees(self, x, y):
        angle_radians = math.atan2(y, x)                 ###Get the angle in radians
        angle_degrees = math.degrees(angle_radians)      ###Convert to degrees
        return angle_degrees

window = Game(SCREEN_WIDTH, SCREEN_HEIGHT)
arcade.run()