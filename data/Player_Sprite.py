import pygame as pg
from math import degrees, atan2, pi
from data import Weapons

def get_angle(origin, destination):
    """Returns angle in radians from origin to destination.
        This is the angle that you would get if the points were
        on a cartesian grid. Arguments of (0,0), (1, -1)
        return pi/4 (45 deg) rather than  7/4.
        """
    x_dist = destination[0] - origin[0]
    y_dist = destination[1] - origin[1]
    return atan2(-y_dist, x_dist) % (2 * pi)


class Player(pg.sprite.Sprite):
    def __init__(self, center_pos):
        super(Player, self).__init__()
        self.original_image = [
            [pg.image.load("data/resources/images/playerImageFist01.png").convert_alpha(),
             pg.image.load("data/resources/images/playerImageFist02.png").convert_alpha(),
             pg.image.load("data/resources/images/playerImageFist03.png").convert_alpha()],

            [pg.image.load("data/resources/images/playerImageSword01.png").convert_alpha(),
             pg.image.load("data/resources/images/playerImageSword02.png").convert_alpha(),
             pg.image.load("data/resources/images/playerImageSword03.png").convert_alpha()],

            [pg.image.load("data/resources/images/playerImageBow01.png").convert_alpha(),
             pg.image.load("data/resources/images/playerImageBow02.png").convert_alpha(),
             pg.image.load("data/resources/images/playerImageBow01.png").convert_alpha()]
            ]
        self.facing_angle = 90
        self.start_angle = 90
        self.pos = list(center_pos)
        self.rect = self.original_image[0][0].get_rect(center=self.pos)
        self.currentItem = 0


        self.attack = 0
        self.attackToogle = False
        self.attackCooldown = 0


        self.weaponManager = Weapons.weaponManager()
        self.items = [self.weaponManager.set_item(0),
                      self.weaponManager.set_item(0),
                      self.weaponManager.set_item(0),]

        self.set_image()
        self.vx = 0
        self.vy = 0


        self.keys_dict = {
                pg.K_w: (0, -1),
                pg.K_s: (0, 1),
                pg.K_a: (-1, 0),
                pg.K_d: (1, 0)}
        self.speed = .2

    def set_image(self):
        angle = self.facing_angle - self.start_angle
        self.image = pg.transform.rotozoom(self.original_image[self.items[self.currentItem].getValue()][self.attack], angle, 1)
        self.image_rect = self.image.get_rect()

    def update(self, mouse_pos, pressed, dt, obstacles, i, mousePressed, mobs):
        if mousePressed[0]:
            self.attackOnOff()
        self.attacktest()
        self.currentItem = i
        self.facing_angle = degrees(get_angle(self.pos, mouse_pos))
        self.set_image()
        self.items[self.currentItem].update(self.attackToogle, self.rect.center, self.facing_angle, mobs)

        move = [0, 0]
        for k in self.keys_dict:
            if pressed[k]:
                x, y = self.keys_dict[k]
                self.vx = x * self.speed * dt
                self.vy = y * self.speed * dt
                move = [move[0] + self.vx,
                        move[1] + self.vy]
        self.movement(move, obstacles, 0)
        self.movement(move, obstacles, 1)
        self.image_rect.center = self.pos


    def movement(self, move, obstacles, i):
        """
        Move player and then check for collisions; adjust as necessary.
        """
        self.pos[i] += move[i]
        self.rect.center = self.pos
        collision = pg.sprite.spritecollideany(self, obstacles)
        while collision:
            self.adjust_on_collision(collision, i)
            collision = pg.sprite.spritecollideany(self, obstacles)

    def adjust_on_collision(self, collide, i):
        """
        Adjust player's position if colliding with a solid block.
        """
        bounce = 10
        if self.rect[i] < collide.rect[i]:
            self.rect[i] -= bounce
        else:
            self.rect[i] += bounce
        self.pos[i] = self.rect.center[i]


    def draw(self, surface):
        surface.blit(self.image, self.image_rect)
        try:
             self.items[self.currentItem].drawArrow(surface)
        except:
            pass

    def drawItems(self, surface):
        for i in range(0,3):
            surface.blit(self.items[i].getImage(), (543+(i*67), 654))

    def attackOnOff(self):
        if self.attackToogle == False and self.attackCooldown == 0:
            self.attackToogle = True

    def attacktest(self):
        if self.attackToogle:
            if self.attack < 2:
                self.attack += 1
            else:
                self.attack = 0
                self.attackToogle = False

    def attacking(self):
        return self.attack

    def changeItem(self, i):
        self.items[self.currentItem] = self.weaponManager.set_item(i)








