import pygame as pg
from math import degrees, atan2, pi

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
        self.original_image = pg.image.load("data/resources/images/playerImage.png").convert_alpha()
        self.facing_angle = 90
        self.start_angle = 90
        self.pos = center_pos
        self.velocity = [0, 0]
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
        self.image = pg.transform.rotate(self.original_image, angle)
        self.rect = self.image.get_rect()

    def update(self, mouse_pos, pressed, dt, obstacles):

        self.facing_angle = degrees(get_angle(self.pos, mouse_pos))
        self.set_image()
        for k in self.keys_dict:
            if pressed[k]:
                x, y = self.keys_dict[k]
                self.vx = x * self.speed * dt
                self.vy = y * self.speed * dt
                self.pos = (self.pos[0] + (self.vx),
                                self.pos[1] + (self.vy))

        self.rect.center = self.pos
        collision = pg.sprite.spritecollideany(self, obstacles)
        while collision:
            self.adjustCollision(collision)
            self.rect.center = self.pos
            collision = pg.sprite.spritecollideany(self, obstacles)

    def adjustCollision(self, wall):
        wall = wall.rect
        if self.rect.x < wall.x:
            self.pos = (self.pos[0]-5,self.pos[1])
        else:
            self.pos = (self.pos[0]+5, self.pos[1])
        if self.rect.y < wall.y:
            self.pos = (self.pos[0],self.pos[1]-5)
        else:
            self.pos = (self.pos[0], self.pos[1]+5)





    def draw(self, surface):
        surface.blit(self.image, self.rect)
