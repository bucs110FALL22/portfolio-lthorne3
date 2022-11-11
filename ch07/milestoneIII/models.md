# Final Project Milestone #3

[Final Project Description](https://docs.google.com/document/d/1j3zgypVjPjzXl4pL1_Wpjvp3GLCW9zcFydkwUjNfNUA/edit?usp=sharing)

Complete this document in **your** portfolio (CH 9). 

You should now begin to code your models. 

Define your models in the `FinalProject/src/` folder in your portfolio.

Although you will probably need to alter them further, you should try to write as much of the models as you can. You can always change things later.

## Models Design

You need to make sure you have the following for each Model:

1. for classes that should be sprites:
    * inherit sprite functionality
    * have instance variables image and rect
2. Models should not have any event logic
    * In other words, you should not be inspecting or responding to events in your models
    * Although some is required, such as the Sprite class, try to minimize how much of the pygame library you use in your models

Remember, this is to get you thinking and help me guide you. Nothing is set in stone.

***

Using the example below, list each model class and its interface

1. < Class Enemy > 
    * __init__
        * < description >
    * < additional methods >

1. class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(self)
        self.health = 2
        self.x= x
        self.y= y
        self.image = pygame.image.load("assets/enemy.png")
        self.rect = self.image.get_rect()
        self.speed = Random.randrange(1,5)

    def generate(self, x, y):
        '''puts the enemy in a randomly generated position'''
        self.x= Random.randrange(#width of the maze)
        self.y= Random.randrange(#height of the maze)

    def move(self, x, y):
        '''enemy moes back and forth within the maze (like pacman)'''
        while #pos of enemy is not touching a wall of the maze:
           self.x= self.x-10 #or to wherever a wall is
           self.x= self.x+10 #back to starting
   
    def die(self, x, y):
       '''if enemy and player come into contact, enemy dies, might belong better in the player class so could be changed later'''
        if enemy.x=player.x and enemy.y=player.y:
          self.image= None


3. class Wall():
    def __init__(self):
        self.x= x
        self.y= y
        self.width= w
        self.height= h
        self.rect= pygame.Rect(self.x, self.y, self.height, self.width)

    def makeWall(self, display, color):
        pygame.draw.rect(display, color, self.rect)
        pygame.display.flip()
   
