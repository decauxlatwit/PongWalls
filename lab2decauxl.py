# import the pygame module, so you can use it
import pygame
 
# define a main function
def main():
     
    # initialize the pygame module
    pygame.init()
    # load and set the logo
    pygame.display.set_caption("DeCauxl pong")
    WIDTH = 800
    HEIGHT = 480
    BORDER = 20
    # create a surface on screen that has the size of 240 x 180
    screen = pygame.display.set_mode((WIDTH,HEIGHT))

    #Draw Top Wall
    pygame.draw.rect(screen, pygame.Color("white"), pygame.Rect((0,0), (WIDTH, BORDER)))
    #Draw Bottom Wall
    pygame.draw.rect(screen, pygame.Color("white"), pygame.Rect((0,0), (BORDER, HEIGHT)))
    #Draw Left Wall
    pygame.draw.rect(screen, pygame.Color("white"), pygame.Rect((0,HEIGHT-BORDER), (WIDTH, BORDER)))
    pygame.display.update() #only needed for macOS bug

    # define a variable to control the main loop
    running = True
     
    # main loop
    while running:
        # event handling, gets all event from the event queue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False
     
     
if __name__=="__main__":
    main()