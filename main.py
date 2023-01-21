import pygame 
import sys, pygame, os
from random import randrange
pygame.init()



size = WIGTH, HEIGHT = 1000, 500
FPS = 60 # Frame per seconds (how many times is the windue being opdated)

screen = pygame.display.set_mode(size)

# load background and scaling it to the windue size 
Background_img = pygame.image.load("bg1.PNG")
Background_img = pygame.transform.scale(Background_img, size)

# load pipes 
pipe_buttom_img = pygame.image.load("pipe.png")
pipe_top_img = pygame.transform.rotate(pipe_buttom_img, 180)

        
class PipeObject():

    GAP = 250 # the gap between each pipe 
    speed = 5
    
    def __init__(self, x, image="pipe.png"):
        self.pipe_img = pygame.image.load(image)
        self.pipe_buttom_img = pipe_buttom_img
        self.pipe_top_img = pipe_top_img
        self.pipe_buttom_hgt = 0
        self.x = x

        PipeObject.set_pipe_hight(self)

    
    def set_pipe_hight(self):
        """randomize the hight off the pipe"""

        # assign a random hight for buttomPipe 
        buttom_pipe_height = randrange(50, 280)
        #scale buttomPipe after assigned hight 
        self.pipe_buttom_hgt = buttom_pipe_height #scale (image, (x, y))
        #assign topPipe the diff  
        diff_top_buttom_pipe =  self.pipe_img.get_height() - buttom_pipe_height
        #scale topPipe after diff value
        self.pipe_top_img = pygame.transform.scale(self.pipe_img, (self.pipe_img.get_width(), diff_top_buttom_pipe)) 
        #roate topPipe 
        self.pipe_top_img = pygame.transform.rotate(self.pipe_top_img, 180)

    def move(self): 
        print(type(PipeObject.speed), type(self.x), PipeObject.speed, self.x)
        print("xx")
        self.x -= PipeObject.speed
        

    def draw_pipe(self): 
        screen.blit(self.pipe_top_img, (self.x, 0))
        screen.blit(self.pipe_buttom_img, (self.x, self.pipe_buttom_hgt+self.GAP))
        #pygame.display.update()
        #screen.blit(self.pipe_buttom_img, (self.pipe_buttom_img.get_wight()-self.speed, self.pipe_buttom_img.get_height()))

        


def draw_windue(): 
    """ drawing and updating the Background, pipes and bird"""
    screen.blit(Background_img, (0,0))
    #screen.blit(pipe_buttom_img, (0, 200))
    #print(pipe_buttom_img.get_rect())
    #screen.blit(pipe_top_img, (200, 0))
    pygame.display.update()

#ballrect = ball.get_rect()

def main(): 
    draw_windue()

    clock = pygame.time.Clock() 
    pipes = [PipeObject(1000)] # 1 object called pipe is being created. 1000 represent the size of the windue inwitch the pipe has to travel from
    

    while True:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()

        pygame.time.wait(199)

        add_pipe = False 

        for pipe in pipes: 
            pipe.move()

            # pipes moves from pipe.x windoeSize(1000) to 0. 
            # when pipe moves 120 on x-axsal in interval (def speed) a new pipe is created
            if pipe.x == 880: 
                add_pipe = True

        if add_pipe: 
            pipes.append(PipeObject(WIGTH))
        

        screen.blit(Background_img, (0,0))
        for pipe in pipes: 
            # pipe.x goes from 1000(windueSize) to 0. if 0 than remove pipe from list of pipes. 
            # means pipe has reach the end of the windue
            if pipe.x == 0: 
                pipes.remove(pipe)
            
            pipe.draw_pipe()
            pygame.display.update()
        
       
        clock.tick(FPS)

        
        #pygame.display.flip()

# runs everytime the script is called on 
if __name__ == "__main__": 
    main()