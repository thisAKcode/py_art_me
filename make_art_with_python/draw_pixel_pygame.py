import pygame

import pygame.gfxdraw

# make sure pygame gets set up
pygame.init()

screenWidth = 800
screenHeight = 800

screen = pygame.display.set_mode((screenWidth, screenHeight))

white = (255, 255, 255)

black = (0,0,0)

running = True

while running:
    
    screen.fill(black)
    
    pygame.gfxdraw.pixel(screen, screenWidth // 2, screenHeight //2 , white)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    pygame.display.flip()