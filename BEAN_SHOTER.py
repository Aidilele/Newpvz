import pygame as pg
bullet_path='bullet.png'

class bullet(pg.sprite.Sprite):
    def __init__(self,plant,bullet_path):
        pg.sprite.Sprite.__init__(self)
        self.image=pg.image.load(bullet_path)
        self.rect=self.image.get_rect()
        self.rect.x=plant.rect.x+plant.rect.width
        self.rect.y=plant.rect.y+int(0.2*plant.rect.height)
        self.move_speed=plant.bullet_move_speed
        self.attack_point=plant.attack_point
    def hitted(self,zombie_group):
       
        for each in zombie_group:
            
            if self.rect.top>=each.rect.top and self.rect.bottom<=each.rect.bottom and self.rect.right>=each.rect.left:
               
                each.hp-=self.attack_point
                return 1
        return 0
            
    def update(self):
        self.rect.x+=self.move_speed

    
class plant(pg.sprite.Sprite):

    def __init__(self,pos,screen):
        pg.sprite.Sprite.__init__(self)
        self.image=pg.image.load('plant.png')
        self.rect=self.image.get_rect()
        self.rect.x=pos[0]
        self.rect.y=pos[1]
        self.hp=100
        self.attack_count=0
        self.attack_freq=60
        self.attack_point=20
        self.bullet_move_speed=7
        self.bullet_group=pg.sprite.Group()
        self.screen=screen
        self.state_flag=0    ##用于指示植物是否处于攻击状态
        self.cost=100
        self.id='bs'
    def spy(self,zombie_group):
        for each in zombie_group:
            if each.rect.y==self.rect.y:
                self.state_flag=1
                return 1
        self.state_flag=0
        return 0

    def attack(self,zombie_group):
        if self.attack_count>=self.attack_freq:    
            bu=bullet(self,bullet_path)
            self.bullet_group.add(bu)
            self.attack_count=0
        for each in self.bullet_group:
            a=each.hitted(zombie_group)
            if a==1:
                each.kill()
                del each
                
        self.bullet_group.update()
        self.bullet_group.draw(self.screen)

    def update(self):
        if self.state_flag==1:
            self.attack_count+=1

    
    
        
