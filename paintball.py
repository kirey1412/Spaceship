# do not put x,y coordinate on image load func
# put x,y coordinate on blit function instead to set the pic's pos

import pygame, random
pygame.font.init()
pygame.mixer.init() #allowing to load sounds
pygame.init()
WIDTH, HEIGHT=1024, 500
RW, RH = 200,200

screen=pygame.display.set_mode((WIDTH, HEIGHT))
title=pygame.display.set_caption("Paintball")

background=pygame.image.load("checkerbg.png")
gun=pygame.image.load("revolver.png")
wall=pygame.image.load("wall.png")

background=pygame.transform.scale(background, (WIDTH, HEIGHT))
gun=pygame.transform.scale(gun, (RW, RH))

speed=5

border=pygame.Rect(WIDTH/2-5, 0, 10, HEIGHT)
def handlegun(key_pressed, rev):
    if key_pressed [pygame.K_LEFT] and rev.x>0:
        print(rev.x)
        rev.x-=speed
    if key_pressed [pygame.K_UP] and rev.y>0:
        rev.y-=speed
    if key_pressed [pygame.K_RIGHT] and rev.x<WIDTH-rev.width:
        rev.x+=speed
    if key_pressed [pygame.K_DOWN] and rev.y>HEIGHT-rev.height:
        rev.y+=speed

def draw(rev):
    screen.blit(background, (0,0))
    # pygame.draw.rect(screen, "pink", rev)
    screen.blit(gun, (rev.x-40, rev.y-60))
    pygame.draw.rect(screen, "black", border)
    screen.blit(wall, (WIDTH-400, HEIGHT/14))
    pygame.display.update()

def play():
    rev=pygame.Rect(WIDTH/9, HEIGHT/2-60, 130, 90)
    run = True
    while run:
        for events in pygame.event.get():
            if events.type==pygame.QUIT:        #Close the window
                pygame.quit()
                break
        key_pressed=pygame.key.get_pressed()

        handlegun(key_pressed, rev)
        draw(rev)
play()