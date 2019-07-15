import pygame as pg
from Bird import *
from Pipes import *

import random

WIDTH,HEIGHT=288,512

def main():
    pg.init()
    screen=pg.display.set_mode((WIDTH,HEIGHT),0,32)
    
    
    bg=pg.image.load("background-day.png")
    bg.convert_alpha()

    rect=bg.get_rect()

    background=pg.Surface((rect.width*2,rect.height*2))
    background.blit(bg,(0,0))
    background.blit(bg,(rect.width,0))

    del rect
    del bg

    backgroundx=0


    allgroups=pg.sprite.Group()
    birdgroup=pg.sprite.Group()
    colongroup=pg.sprite.Group()


    bird=Bird(screen,[50,100],allgroups,birdgroup)

    pipe_spawn_time=0
    pipe_interval=3

    clock=pg.time.Clock()
    running=True

    while running:
        time=clock.tick()/1000.0


        for event in pg.event.get():
            if event.type==pg.QUIT:
                running=False
            
            if event.type==pg.KEYDOWN:
                if event.key==pg.K_ESCAPE:
                    running=False


        backgroundx-=time*100
        screen.blit(background,(backgroundx,0))
        if backgroundx<-WIDTH:
            backgroundx=0;
        


        pipe_spawn_time += time

        if pipe_spawn_time > pipe_interval:
            pos=[288 + 52,  random.randint(80, 432)]
            Pipes(pos,allgroups, colongroup, birdgroup)
            pipe_spawn_time = 0
            del pos


        allgroups.update(time)
        allgroups.draw(screen)

        pg.display.flip()



    pg.quit()



if __name__=="__main__":
    main()
