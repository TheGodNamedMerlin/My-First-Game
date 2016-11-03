import pygame as pg
from math import sqrt, atan2, pi, degrees

def get_angle(origin, destination):
    """Returns angle in radians from origin to destination.
        This is the angle that you would get if the points were
        on a cartesian grid. Arguments of (0,0), (1, -1)
        return pi/4 (45 deg) rather than  7/4.
        """
    x_dist = destination[0] - origin[0]
    y_dist = destination[1] - origin[1]
    return atan2(-y_dist, x_dist) % (2 * pi)

class mob(pg.sprite.Sprite):

    def __init__(self, x, y, chase, startingDirection):
        super(mob, self).__init__()

        self.orginalImage = pg.image.load("data/resources/images/Enemy.png").convert_alpha()
        self.rect = self.orginalImage.get_rect()

        self.rect.centerx = x
        self.rect.centery = y

        self.attempt = chase

        self.chasex = False
        self.chasey = False
        self.facing_angle = 90
        self.start_angle = 90

        self.speed = 4

        self.image = pg.transform.rotate(self.orginalImage, 90*startingDirection)

    def update(self, player):


        if self.attempt:

            try:
                self.movex = (player.rect.centerx - self.rect.centerx)/sqrt((player.rect.centerx - self.rect.centerx)**2+(self.rect.centery-self.rect.centery) ** 2)*self.speed
            except:
                self.movex = 0


            try:
                self.movey = (player.rect.centery - self.rect.centery)/sqrt((player.rect.centery - self.rect.centery)**2+(self.rect.centerx-self.rect.centerx) ** 2)*self.speed
            except:
                self.movey = 0

            x = player.rect.centerx-5
            for i in range(x, player.rect.centerx+5):
                if self.rect.centerx == i:
                    self.chasey = True
            y = player.rect.centery-5
            for i in range(y, player.rect.centery+5):

                if self.rect.centery == i:
                    self.chasex = True
            if self.chasex:
                self.rect.centerx += self.movex


            if self.chasey:
                self.rect.centery += self.movey

        if self.chasex or self.chasey:
            self.facing_angle = degrees(get_angle(self.rect.center, player.rect.center))
            self.set_image()


    def draw(self, window):
        window.blit(self.image, self.rect)

    def set_image(self):
        angle = self.facing_angle - self.start_angle
        self.image = pg.transform.rotozoom(self.orginalImage, angle, 1)

