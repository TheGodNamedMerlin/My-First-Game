import pygame as pg
from data import Block_Sprites, Mobs_Sprites

def get_level_data(levelnumber):

    if levelnumber == "1" or levelnumber == 1:
        #x, y, width, height
        terrian = [
            [0, 0, 319, 543],
            [319, 0, 448, 287],
            [-1, 0, 5, 720],
            [0,0,1280,5],
            [1281,0,5,720],
            [0,721,1280,5]
        ]

        #x, y
        mobs = [
            [488, 324, True, 2],
            [919, 17, True, 2]
        ]

        #x, y, item
        #0 = fist, 1 = sword, 2 = bow
        items = [
            [337, 301, 1]
        ]


        terrian_group = pg.sprite.Group()
        for block in terrian:
            terrian_group.add(Block_Sprites.Block(block[0],block[1],block[2],block[3]))

        mobs_group = pg.sprite.Group()
        for mob in mobs:
            mobs_group.add(Mobs_Sprites.mob(mob[0],mob[1], mob[2], mob[3]))

        items_group = pg.sprite.Group()
        for item in items:
            items_group.add(Block_Sprites.Item(item[0],item[1], item[2]))

        finishPoint = Block_Sprites.Block(1152, 32, 32,32)

        return 1, terrian_group, mobs_group, [59, 637], finishPoint, items_group

    elif levelnumber == "2" or levelnumber == 2:
        #x, y, width, height
        terrian = [
            [-1, 0, 5, 720],
            [0,0,1280,5],
            [1281,0,5,720],
            [0,721,1280,5],
            [0, 288, 415, 448],
            [864, 192, 416, 544]
        ]

        #x, y
        mobs = [
            [465, 426, True, 0],
            [900, 34, True, 2]
        ]

        #x, y, item
        #0 = fist, 1 = sword, 2 = bow
        items = [
            [751, 658, 1]
        ]


        terrian_group = pg.sprite.Group()
        for block in terrian:
            terrian_group.add(Block_Sprites.Block(block[0],block[1],block[2],block[3]))

        mobs_group = pg.sprite.Group()
        for mob in mobs:
            mobs_group.add(Mobs_Sprites.mob(mob[0],mob[1], mob[2], mob[3]))

        items_group = pg.sprite.Group()
        for item in items:
            items_group.add(Block_Sprites.Item(item[0],item[1], item[2]))

        finishPoint = Block_Sprites.Block(1152, 64, 32,32)

        return 2, terrian_group, mobs_group, [91, 110], finishPoint, items_group

    elif levelnumber == "3" or levelnumber == 3:
        #x, y, width, height
        terrian = [
            [-1, 0, 5, 720],
            [0,0,1280,5],
            [1281,0,5,720],
            [0,721,1280,5],
            [1, 417, 478, 319],
            [481, 254, 799, 482]
        ]

        #x, y
        mobs = [
            [733, 210, True, 1],
            [976, 54, True, 1]
        ]

        #x, y, item
        #0 = fist, 1 = sword, 2 = bow
        items = [
            [420, 365, 2]
        ]


        terrian_group = pg.sprite.Group()
        for block in terrian:
            terrian_group.add(Block_Sprites.Block(block[0],block[1],block[2],block[3]))

        mobs_group = pg.sprite.Group()
        for mob in mobs:
            mobs_group.add(Mobs_Sprites.mob(mob[0],mob[1], mob[2], mob[3]))

        items_group = pg.sprite.Group()
        for item in items:
            items_group.add(Block_Sprites.Item(item[0],item[1], item[2]))

        finishPoint = Block_Sprites.Block(1184, 96, 32,32)

        return 3, terrian_group, mobs_group, [60, 354], finishPoint, items_group

    elif levelnumber == "4" or levelnumber == 4:
        #x, y, width, height
        terrian = [
            [-1, 0, 5, 720],
            [0,0,1280,5],
            [1281,0,5,720],
            [0,721,1280,5],
            [0, 0, 96, 512],
            [96, 0, 779, 63],
            [865, 64, 362, 193],
            [1218, 254, 62, 173],
            [736, 418, 544, 92],
            [256, 160, 478, 351]
        ]

        #x, y
        mobs = [
            [118, 337, False, 0],
            [202, 295, False, 0],
            [284, 106, False, 3],
            [651, 106, False, 3],
            [1024, 329, False, 3]
        ]

        #x, y, item
        #0 = fist, 1 = sword, 2 = bow
        items = [
            [391, 570, 2],
            [838, 543, 1]
        ]


        terrian_group = pg.sprite.Group()
        for block in terrian:
            terrian_group.add(Block_Sprites.Block(block[0],block[1],block[2],block[3]))

        mobs_group = pg.sprite.Group()
        for mob in mobs:
            mobs_group.add(Mobs_Sprites.mob(mob[0],mob[1], mob[2], mob[3]))

        items_group = pg.sprite.Group()
        for item in items:
            items_group.add(Block_Sprites.Item(item[0],item[1], item[2]))

        finishPoint = Block_Sprites.Block(1152, 320, 32,32)

        return 4, terrian_group, mobs_group, [1158, 646], finishPoint, items_group

    elif levelnumber == "5" or levelnumber == 5:
        #x, y, width, height
        terrian = [
            [-1, 0, 5, 720],
            [0,0,1280,5],
            [1281,0,5,720],
            [0,721,1280,5],
            [320, 417, 960, 95],
            [192, 128, 127, 608],
            [309, 128, 75, 63],
            [0, 0, 384, 31],
            [0, 21, 32, 566],
            [0, 557, 205, 159]
        ]

        #x, y
        mobs = [
            [1208, 82, True, 1],
            [1056, 553, False, 0],
            [753, 553, False, 1],
            [102, 472, True, 0],
            [99, 82, True, 3]
        ]

        #x, y, item
        #0 = fist, 1 = sword, 2 = bow
        items = [
            [358, 303, 1],
            [1126, 86, 2]
        ]


        terrian_group = pg.sprite.Group()
        for block in terrian:
            terrian_group.add(Block_Sprites.Block(block[0],block[1],block[2],block[3]))

        mobs_group = pg.sprite.Group()
        for mob in mobs:
            mobs_group.add(Mobs_Sprites.mob(mob[0],mob[1], mob[2], mob[3]))

        items_group = pg.sprite.Group()
        for item in items:
            items_group.add(Block_Sprites.Item(item[0],item[1], item[2]))

        finishPoint = Block_Sprites.Block(89, 525, 32,32)

        return 5, terrian_group, mobs_group, [797, 306], finishPoint, items_group