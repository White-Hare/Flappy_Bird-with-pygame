import pygame as pg




class Bird(pg.sprite.Sprite):

    def __init__(self,screen,pos,*groups):
        self.groups=groups
        pg.sprite.Sprite.__init__(self,self.groups)
        
        self.image_array=[]
        for i in range(1,4):
            self.image_array.append(pg.image.load("b{}.png".format(str(i))).convert_alpha())

        self.current_pic=0
        self.image=self.image_array[self.current_pic]
        self.rect=self.image.get_rect()
        self.screenrect=screen.get_rect()

        self.pos=pos.copy()
        self.rect.center=self.pos

        self.animationinterval=0.2
        self.animationtime=0

        self.flyinginterval=0.5
        self.flyingtime=0

        self.buttoninterval=self.flyinginterval/2
        self.buttontime=0


        self.flying=False


    def animation(self,time):
       self.animationtime+=time
       if self.animationtime>self.animationinterval:
          self.current_pic+=1
          self.current_pic%=3
          self.image=self.image_array[self.current_pic]
          self.animationtime=0



    def update(self,time):
        keys=pg.key.get_pressed()

        
        if self.flying==True:
            self.pos[1]-=500*time
            self.flyingtime-=time
            self.animation(time)
            self.buttontime=self.buttoninterval

        if self.flyingtime<=0:
            self.flying=False
            
        if self.buttontime>=0:
            self.buttontime-=time


        if keys[pg.K_SPACE] and self.buttontime<=0:
            self.flyingtime=self.flyinginterval
            self.flying=True

        else:
            self.pos[1]+=time*200
        
            

        self.rect.center=self.pos

        if self.rect.top>self.screenrect.bottom:
            self.kill()
        
