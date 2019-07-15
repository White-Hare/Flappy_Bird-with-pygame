import pygame as pg
import random



class Pipes(pg.sprite.Sprite):
    def __init__(self,pos, *groups):
        self.groups = groups[0], groups[1]
        self.bird = groups[2]

        pg.sprite.Sprite.__init__(self, self.groups)

        upper_colon = pg.image.load('pipe-green.png').convert_alpha()
        lower_colon = pg.transform.flip(upper_colon, 0, 1).convert_alpha()
        upper_colon_rect = upper_colon.get_rect()
        lower_colon_rect = upper_colon.get_rect()


        vertical_gap=300


        self.image = pg.Surface((upper_colon_rect.width, upper_colon_rect.height + upper_colon_rect.height + vertical_gap))
        self.image.blit(lower_colon, (0, 0))
        self.image.blit(upper_colon, (0, upper_colon_rect.height + vertical_gap))
        self.image.set_colorkey((0, 0, 0))
        self.image.convert_alpha()

        self.mask = pg.mask.from_surface(self.image)

        del upper_colon_rect
        del lower_colon_rect
        del upper_colon
        del lower_colon

        self.rect = self.image.get_rect()
        self.pos=pos.copy()
        self.rect.center = self.pos


    def update(self, time):


        self.pos[0] -= 100 * time
        
        collided = pg.sprite.spritecollide(self, self.bird, False, pg.sprite.collide_mask)
        for c in collided:
            import os
            os.system("pause")
            break

        if self.rect.right < 0:
            self.kill()

        self.rect.center=self.pos
