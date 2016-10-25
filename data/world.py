import pygame as pg
from data import Block_Sprites

def get_level_data(levelnumber):

    if levelnumber == "1" or levelnumber == 1:
        #x, y, width, height
        terrian = [
            [0, 700, 1280, 5],
            [0, 15, 1280, 5]
        ]


        terrian_group = pg.sprite.Group()
        for block in terrian:
            terrian_group.add(Block_Sprites.Block(block[0],block[1],block[2],block[3]))

        return 1, terrian_group

    elif levelnumber == "2" or levelnumber == 2:
        #x, y, width, height
        terrian = [
            [0, 650, 1280, 5],
            [0, 30, 1280, 5],
            [620, 340, 20, 20]
        ]

        terrian_group = pg.sprite.Group()
        for block in terrian:
            terrian_group.add(Block_Sprites.Block(block[0],block[1],block[2],block[3]))

        return 2, terrian_group

    elif levelnumber == "3" or levelnumber == 3:
        #x, y, width, height
        terrian = [
            [451, 261, 5, 262],
            [456, 261, 377, 5]

        ]
        terrian_group = pg.sprite.Group()
        for block in terrian:
            terrian_group.add(Block_Sprites.Block(block[0],block[1],block[2],block[3]))

        return 3, terrian_group

