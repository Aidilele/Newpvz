
from GAMEMAP import *
import pygame as pg
from pygame.locals import *
from sys import *
import random as rm
def check_event(event,body):
    if event.type == QUIT:
        exit()
    if event.type == KEYDOWN:
        if event.key==K_b:
            body.zlag=1
    if event.type==MOUSEBUTTONDOWN:

        if 1500<=event.pos[0]<=1600 and 300<=event.pos[1]<=400:
            body.plag=1
        if 1500<=event.pos[0]<=1600 and 400<=event.pos[1]<=500:
          
            body.plag=2
        if 1500<=event.pos[0]<=1600 and 500<=event.pos[1]<=600:
      
            body.plag=3
            
        for each in body.sun_group:
            if each.rect.left<=event.pos[0]<=each.rect.right and each.rect.top<=event.pos[1]<=each.rect.bottom:
                body.sun+=each.attack_point
                each.exist=0
                
    if event.type==MOUSEBUTTONDOWN and body.plag!=0:
        x,y=event.pos
        if x<100 or x>1400 or y<100 or y>800:
            pass
        else:
          
            body.creat_plant(x,y)
            body.plag=0
                      
    if event.type==MOUSEBUTTONDOWN and body.zlag==1:
        x,y=event.pos
        if y<100 or y>800:
            pass
        else:
            body.creat_zombie(x,y)
            body.zlag=0

def main():
    pg.init()
    body=gamemap()
    running=1
    clock=pg.time.Clock()
    timeline=0
    pause=0
    while running:
        timeline=(timeline+1)%180
        pause+=1
        clock.tick(60)
        for event in pg.event.get():
            check_event(event,body)
        if timeline==-1:
            x=0
            y=rm.randint(100,801)
            body.creat_zombie(x,y)
        body.bg_load()
        body.get_sun()
        body.check_plant()
        body.check_zombie()
        body.check_sun()
        running=body.failed()
        pg.display.update()

main()
