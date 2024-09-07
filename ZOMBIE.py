import pygame as pg

class zombie(pg.sprite.Sprite):

    def __init__(self,pos,hp=100):
        pg.sprite.Sprite.__init__(self)
        self.image=pg.image.load('zombie.png')
        self.rect=self.image.get_rect()
        self.hp=hp
        self.rect.x=1400-self.rect.width
        self.rect.y=pos[1]
        self.attack_freq=12
        self.attack_count=0
        self.move_speed=1
        self.update_flag=0
        self.attack_point=20
        
    def attack(self,target):
     
        if self.attack_count>=self.attack_freq:
            target.hp-=self.attack_point
            self.attack_count==0
 
    def spy(self,plant_group):
        for each in plant_group:
            if each.rect.top==self.rect.top and each.rect.right>=self.rect.left and self.rect.left>=each.rect.left:
                self.update_flag=1
                return each
        self.update_flag=0
        return 0
      


    def update(self):
        
        if self.update_flag==1:
            self.attack_count+=1
    
        else:
            self.rect.x-=self.move_speed

    
