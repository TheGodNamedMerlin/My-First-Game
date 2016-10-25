import pygame as pg

class Block(pg.sprite.Sprite):

    def __init__(self, x, y, width, height):
        super(Block, self).__init__()

        self.image = pg.Surface((width, height))
        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y

    def update(self):
        pass

    def draw(self, window):
        window.blit(self.image, self.rect)


