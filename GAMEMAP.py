import BEAN_SHOTER as p
import ZOMBIE as z
import pygame as pg
import SUNFLOWER as s
import WALL_NUT as wn
plant_path='plant.png'
zombie_path='zombie.png'
bg_path='bg.png'
sunflower_path='sunflower.png'

class gamemap:
    def __init__(self):
        win_size=(1700,900)
        self.screen=pg.display.set_mode(win_size)
        self.plant_group=pg.sprite.Group()
        self.zombie_group=pg.sprite.Group()
        self.sun_group=pg.sprite.Group()
        self.bg=pg.image.load(bg_path)
        self.zlag=0
        self.plag=0
        self.sun=500
        self.font=pg.font.SysFont('arial',50)
        self.sun_surface=self.font.render(str(self.sun),True,(0,0,0))
    
    def creat_plant(self,x,y):
        plant_map={1:'p',2:'s',3:'wn'}
        x=int(x/100)*100
        y=int(y/100)*100
        pos=(x,y)

        tar=eval(plant_map[self.plag]).plant(pos,self.screen)
        if self.sun>=tar.cost:
            self.plant_group.add(tar)
            self.sun-=tar.cost
            return tar
        else:
            print("you are using out of your sun")
            del tar
            
    def creat_zombie(self,x,y):
        x=int(x/100)*100
        y=int(y/100)*100
        pos=(x,y)
        tar=z.zombie(pos)
        self.zombie_group.add(tar)
        return tar

    def check_plant(self):
        for each in self.plant_group:
            if each.hp<=0:
                each.kill()
                del each
                continue
            if each.id== 'bs':
                if each.spy(self.zombie_group)==1:
                    each.attack(self.zombie_group)
                    
            elif each.id== 'sf':
                new_sun=each.attack()
                if new_sun!=0:
                    self.sun_group.add(new_sun)
                
        self.plant_group.draw(self.screen)
        self.plant_group.update()

    def check_zombie(self):
        for each in self.zombie_group:
            if each.hp<=0:
                each.kill()
                del each
           
                continue
            tar=each.spy(self.plant_group)
       
            if tar!=0:
        
                each.attack(tar)

        self.zombie_group.draw(self.screen)
        self.zombie_group.update()
        
    def check_sun(self):
        for each in self.sun_group:
            if each.exist==0 or each.exist==each.disapper:
                each.kill()
                del each
        self.sun_group.draw(self.screen)
        self.sun_group.update()
        
    def get_sun(self,sun_mount=0):
        self.sun+=sun_mount
        self.sun_surface=self.font.render(str(self.sun),True,(0,0,0))
        self.screen.blit(self.sun_surface,(1520,180))
        
    def bg_load(self):
        self.screen.blit(self.bg,(0,0))
    

    def failed(self):
        for each in self.zombie_group:
            if each.rect.left<=100:
                print('You are failed!')
                return 0
        return 1
    


        
        
