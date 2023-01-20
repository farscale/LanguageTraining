import pygame 
import sys, pygame, os
from random import randrange
pygame.init()



size = WIGTH, HEIGHT = 1000, 500
FPS = 60 # Frame per seconds (how many times is the windue being opdated)
speed = [2, 2]
black = 0, 0, 0

screen = pygame.display.set_mode(size)

# load background and scaling it to the windue size 
Background_img = pygame.image.load("bg1.PNG")
Background_img = pygame.transform.scale(Background_img, size)

# load pipes 
pipe_buttom_img = pygame.image.load("pipe.png")
pipe_top_img = pygame.transform.rotate(pipe_buttom_img, 180)

class GameObject:
    def __init__(self, image, height=0, speed=1, windue_WIGTH=WIGTH):
        self.speed = speed
        self.image = image
        self.windue_WIGTH = windue_WIGTH
        self.pos = image.get_rect()#.move(0, height)

    def move(self):
        
        self.pos = self.pos.move(self.speed, 0) # func move here is from pygame and you can determine the speed and position of an object 
        
        if self.pos.right > self.windue_WIGTH:
            self.pos.left = 0


def random_pipe_img(img):
    """randomize the hight af the pipe"""
    return pygame.transform.scale(img, (img.get_width(), randrange(img.get_height()+25)))       
        

class PipeObject():
    GAP = 300 # the gap between each pipe 
    speed = 2

    def __init__(self, x):
        pass 

    def set_pipe(self): 
        image = random_pipe_img(pipe_top_img)
        o = GameObject(image)
        return o



def pipemove(): 
    
    
    screen.blit(Background_img, o.pos, o.pos)  #makes sure that the background isnt ersead when objects moves 

    #moves/updates objects position
    o.move()     
    screen.blit(o.image, o.pos)
    pygame.display.update()


def draw_windue(): 
    """ drawing and updating the Background, pipes and bird"""
    screen.blit(Background_img, (0,0))
    screen.blit(pipe_buttom_img, (0, 200))
    print(pipe_buttom_img.get_rect())
    #screen.blit(pipe_top_img, (200, 0))
    pygame.display.update()

#ballrect = ball.get_rect()

def main(): 
    draw_windue()

    clock = pygame.time.Clock() 

    while True:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()

        pipemove()
       
        clock.tick(FPS)

        
        #pygame.display.flip()

# runs everytime the script is called on 
if __name__ == "__main__": 
    main()