import pygame as pg


class bullet(pg.sprite.Sprite):
    def __init__(self,plant):
        pg.sprite.Sprite.__init__(self)
        self.image=pg.image.load('sun.png')
        self.rect=self.image.get_rect()
        self.rect.x=plant.rect.x
        self.rect.y=plant.rect.y
        self.attack_point=plant.attack_point
        self.exist=1
        self.disapper=120
    def update(self):
        self.exist+=1

    
class plant(pg.sprite.Sprite):

    def __init__(self,pos,screen):
        pg.sprite.Sprite.__init__(self)
        self.image=pg.image.load('sunflower.png')
        self.rect=self.image.get_rect()
        self.rect.x=pos[0]
        self.rect.y=pos[1]
        self.hp=100
        self.attack_count=0
        self.attack_freq=180
        self.attack_point=25
        self.bullet_move_speed=0
        self.bullet_group=pg.sprite.Group()
        self.screen=screen
        self.state_flag=0    ##用于指示植物是否处于攻击状态
        self.cost=50
        self.id='sf'
    def spy(self,zombie_group):
        return 1
        

    def attack(self):
        if self.attack_count>=self.attack_freq:    
            bu=bullet(self)
            self.bullet_group.add(bu)
            self.attack_count=0             
            return bu
        return 0
    def update(self):
        self.attack_count+=1

    
    
        
