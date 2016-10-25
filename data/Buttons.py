import pygame as pg

class MenuButton(pg.sprite.Sprite):

    def __init__(self, x, y, text, id):

        super(MenuButton, self).__init__()

        self.image = pg.image.load("data/resources/images/ButtonBox.png").convert_alpha()

        self.rect = self.image.get_rect()

        self.rect.x = x

        self.rect.y = y

        self.ID = id

        self.toggle = False

        self.text = text
        self.font = pg.font.Font("data/resources/FreeSansBold.ttf",32)
        self.displaytext = self.font.render(self.text, True, (0, 0, 0))

    def whatButton(self):
        return self.ID

    def istoggled(self):
        return self.toggle

    def toggle(self):
        if self.toggle:
            self.toggle = False
        else:
            self.toggle = True

    def getPosition(self):
        self.Pos = [
            [self.rect.topleft[0]],
            [self.rect.topleft[1]],
            [self.rect.bottomright[0]],
            [self.rect.bottomright[1]]
        ]

        return self.Pos

    def draw(self, window):
        window.blit(self.image, self.rect)
        window.blit(self.displaytext, (self.rect.centerx-len(str(self.text))*8 ,self.rect.y+15))

    def updatetext(self, text):
        self.text = text
        self.displaytext = self.font.render(str(self.text), True, (0, 0, 0))