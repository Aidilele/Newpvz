import pygame as pg



    
class plant(pg.sprite.Sprite):

    def __init__(self,pos,screen):
        pg.sprite.Sprite.__init__(self)
        self.image=pg.image.load('wall_nut.png')
        self.rect=self.image.get_rect()
        self.rect.x=pos[0]
        self.rect.y=pos[1]
        self.hp=10000
        self.screen=screen                    ##用于指示植物是否处于攻击状态
        self.cost=50
        self.id='wn'
        self.recover=0.5
        self.recover_wait=0
        self.hp_next=self.hp
    def update(self):
        if self.hp_next==self.hp and self.hp<=6666:
            self.recover_wait+=1
            if self.recover_wait>=180:
                self.hp+=self.recover
                
        else:
            self.recover_wait=0
            
        self.hp_next=self.hp
    
    
        
