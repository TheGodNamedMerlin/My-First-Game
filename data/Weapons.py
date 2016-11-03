import pygame as pg
from math import cos, sin, radians

class weaponManager(object):

    def set_item(self, value):

        if value == 0:
            return fist()

        elif value == 1:
            return sword()

        elif value == 2:
            return bow()

class fist(object):

    def __init__(self):

        self.damage = 10
        self.value = 0
        self.image = pg.image.load("data/resources/images/fist.png").convert_alpha()

    def getValue(self):
        return self.value

    def getImage(self):
        return self.image

    def update(self, attackToogle, location, angle, mobs):
        pass

class sword(object):

    def __init__(self):

        self.damage = 20
        self.value = 1
        self.image = pg.image.load("data/resources/images/sword.png").convert_alpha()

    def getValue(self):
        return self.value

    def getImage(self):
        return self.image

    def update(self, attackToogle, location, angle, mobs):
        pass


class bow(object):

    def __init__(self):

        self.damage = 10
        self.value = 2
        self.image = pg.image.load("data/resources/images/bow.png").convert_alpha()
        self.arrow = None
        self.cooldown = 0

    def getValue(self):
        return self.value

    def getImage(self):
        return self.image

    def update(self, attackToogle, location, angle, mobs):
        if attackToogle and self.cooldown <= 0:
            self.arrow = arrow(location, angle)
            self.cooldown = 80
        self.cooldown += -1

        try:
            if self.arrow.update():
                self.arrow = None
            if pg.sprite.spritecollide(self.arrow, mobs, True):
                self.arrow = None
        except:
            pass

    def drawArrow(self, window):
        self.arrow.draw(window)

class arrow(pg.sprite.Sprite):

    def __init__(self, location, angle):
        super(arrow, self).__init__()

        self.orginalImage = pg.image.load("data/resources/images/arrow.png")
        self.angle = -radians(angle)
        self.image = pg.transform.rotozoom(self.orginalImage, angle-90, 1)
        self.rect = self.image.get_rect(center=location)
        self.move = [self.rect.x, self.rect.y]
        self.speedMagnitude = 5
        self.speed = (self.speedMagnitude*cos(self.angle), self.speedMagnitude*sin(self.angle))

        self.life = 50


    def update(self):
        self.life += -1
        self.move[0] += self.speed[0]
        self.move[1] += self.speed[1]
        self.rect.center = self.move

        if self.life < 0:
            return True
        else:
            return False

    def draw(self, window):
        window.blit(self.image, self.rect)


