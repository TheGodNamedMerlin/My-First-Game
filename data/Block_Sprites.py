import pygame as pg

class Block(pg.sprite.Sprite):

    def __init__(self, x, y, width, height):
        super(Block, self).__init__()

        self.image = pg.Surface((width, height))
        self.rect = self.image.get_rect()
        self.image = pg.image.load("data/resources/images/Background_images/0.png").convert_alpha()

        self.rect.x = x
        self.rect.y = y

    def update(self):
        pass

    def draw(self, window):
        window.blit(self.image, self.rect)

class Item(pg.sprite.Sprite):

    def __init__(self, x, y, item):
        super(Item, self).__init__()

        self.image = pg.Surface((32, 32))
        self.rect = self.image.get_rect()
        self.item = item
        self.items = [pg.image.load("data/resources/images/fist.png").convert_alpha(), pg.image.load("data/resources/images/sword.png").convert_alpha(), pg.image.load("data/resources/images/bow.png").convert_alpha()]
        self.image = self.items[item]

        self.rect.x = x
        self.rect.y = y

    def update(self):
        pass

    def returnItem(self):
        return self.item

    def draw(self, window):
        window.blit(self.image, self.rect)



