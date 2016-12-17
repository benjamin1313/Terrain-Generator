import pygame, datetime, math, random
from pnoice import pnoise


white = (255,255,255)
black = (0,0,0)
red = (255,0,0)

pygame.init()
height = 600
width = 1000
gameDisplay = pygame.display.set_mode((width,height))#pygame.FULLSCREEN
pygame.display.set_caption('Perlin Noise')
fps = pygame.time.Clock()
pxarray = pygame.PixelArray(gameDisplay)

xoffset = 0.004
yoffset = 0.004
zoffset = 0.1
mul = 350

def close():
    pygame.quit()
    quit()

def drawMap(zoff):
    xoff = 0
    pxlist = []
    for x in range(width):
        yoff = 0
        for y in range(height):
            
            noise = pnoise(xoff,yoff,zoff)*mul
            if noise < 0:
                noise -= noise

            if noise < 30:
                r = 0
                g = 0
                b = 200
            elif noise < 60:
                r = 0
                g = 0
                b = 255
            elif noise < 70:
                r = 255
                g = 223
                b = 27
            elif noise < 200:
                r = 0
                g = 255
                b = 0
            elif noise < 240:
                r = 163
                g = 84
                b = 8
            else:
                r = 255
                g = 255
                b = 255
            gameDisplay.set_at((x, y), (r, g, b))
            yoff += yoffset
        xoff += xoffset

def main():
    zoff = 50
    drawMap(zoff)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                close()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    close()
                if event.key == pygame.K_UP:
                    zoff = zoff + zoffset
                    drawMap(zoff)
                if event.key == pygame.K_DOWN:
                    zoff = zoff - zoffset
                    drawMap(zoff)
                
        pygame.display.update()
        fps.tick(20)

main()
