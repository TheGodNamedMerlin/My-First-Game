import pygame as pg
import sys, subprocess, os
from data import Player_Sprite, world, Buttons, Load


class Current_state(object):

    def __init__(self, state, save_data, background_images, clock):

        #save date control
        self.save_data = save_data

        #state control
        self.state = state

        self.old_state = None

        #event control
        self.event = None

        #player control

        self.player = Player_Sprite.Player((500,500))

        #level control
        self.current_level, self.level_terrain = world.get_level_data(save_data[0][1])

        #image control
        self.background_images = background_images
        self.current_background_image = self.background_images[self.current_level]

    def change_state(self, state):
        self.old_state = self.state
        self.state = state
        try:
            self.state.give_gameplay_data(self.level_terrain, self.player, self.current_background_image)

        except:
            pass


    def revert_state(self):
        self.state = self.old_state

    def update_event(self, event):
        self.event = event

    def get_events(self):
        self.state.get_events(self.event)

    def update(self, clock):
        self.state.update(clock)

    def render(self, window):
        self.state.render(window)

    def reload(self, level):
        print("reloading state and changing level to " + str(level))
        self.current_level, self.level_terrain = world.get_level_data(level)
        self.current_background_image = self.background_images[level]
        try:
            self.state.give_gameplay_data(self.level_terrain, self.player, self.current_background_image)

        except:
            pass

class game_play(object):

    def __init__(self):
        print("Game_play State Loaded")
        self.hotBar = pg.image.load("data/resources/images/hotBar.png").convert_alpha()

    def give_gameplay_data(self, level_terrain, player, current_background_image):
        self.level_terrain, self.player, self.background_image = level_terrain, player, current_background_image


    def get_events(self, event):
        pass

    def update(self, clock):
        self.dT = clock.get_time()
        pressed = pg.key.get_pressed()
        mousePos = pg.mouse.get_pos()
        self.player.update(mousePos, pressed, self.dT, self.level_terrain)

    def render(self, window):

        window.blit(self.background_image, (0,0))
        self.level_terrain.draw(window)
        self.player.draw(window)
        window.blit(self.hotBar,(557,680 ))


class MainMenu(object):

    def __init__(self):
        print("MainMenu State Loaded")

        self.background01 = pg.image.load("data/resources/images/menuBackground.png").convert_alpha()
        self.background02 = pg.transform.flip(self.background01, True, False)
        self.background01Rect = self.background01.get_rect()
        self.background02Rect = self.background02.get_rect()
        self.background02Rect[0] += self.background01Rect[2]

        self.timer = 0
        self.scrollTime = 10

        self.reloadOptions()

        self.backgroundPos = (0, 0)


        self.buttonList = pg.sprite.Group()

        self.currentMode = "main"
        # "main", "options", "controls"
        self.change_mode()


    def reloadOptions(self):
        self.options = Load.load_options()
        self.left = str(self.options[0][1][5:])
        self.right = str(self.options[1][1][5:])
        self.up = str(self.options[2][1][5:])
        self.down = str(self.options[3][1][5:])


    def change_mode(self):
        if self.currentMode == "main":
            self.buttonList.empty()

            self.buttons = [
                [50, 50, "Play", 0],
                [50, 150, "Options", 1],
                [50, 250, "Controls", 2],
                [50, 350, "Quit", 3]

            ]
            #Xposition Yposition Text Id

            for button in self.buttons:
                button = Buttons.MenuButton(button[0], button[1], button[2], button[3])
                self.buttonList.add(button)

        elif self.currentMode == "options":
            self.buttonList.empty()

            self.buttons = [
                [50, 640, "Save", 4],
                [496, 640, "Use Defaults", 5],
                [942, 640, "Back", 6]

            ]
            #Xposition Yposition Text Id

            for button in self.buttons:
                button = Buttons.MenuButton(button[0], button[1], button[2], button[3])
                self.buttonList.add(button)

        elif self.currentMode == "controls":
            self.buttonList.empty()

            self.buttons = [
                [942, 640, "Back", 6],
                [50, 50, "Move Left =", 7],
                [350, 50, self.left, 8],
                [50, 130, "Move right =", 9],
                [350, 130, self.right, 10],
                [50, 210, "Move up =", 11],
                [350, 210, self.up, 12],
                [50, 290, "Move down =", 13],
                [350, 290, self.down, 14],
                [942, 560, "Open location", 15]
            ]

            for button in self.buttons:
                button = Buttons.MenuButton(button[0], button[1], button[2], button[3])
                self.buttonList.add(button)

    def buttonClick(self, button, mouse):
        self.pos = button.getPosition()
        if mouse[0] > self.pos[0][0]:
            if mouse[1] > self.pos[1][0]:
                if mouse[0] < self.pos[2][0]:
                    if mouse[1] < self.pos[3][0]:
                        return True

    def get_events(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            mouse = pg.mouse.get_pos()

            for button in self.buttonList:

                if button.whatButton() == 0:
                    if self.buttonClick(button, mouse):
                        print("Play was Clicked")

                elif button.whatButton() == 1:
                    if self.buttonClick(button, mouse):
                        print("Options was Clicked")
                        self.currentMode = "options"
                        self.change_mode()

                elif button.whatButton() == 2:
                    if self.buttonClick(button, mouse):
                        print("Controls was Clicked")
                        self.reloadOptions()
                        self.currentMode = "controls"
                        self.change_mode()

                elif button.whatButton() == 3:
                    if self.buttonClick(button, mouse):
                        print("Quit has been pressed")
                        pg.quit()
                        sys.exit()

                elif button.whatButton() == 6:
                    if self.buttonClick(button, mouse):
                        print("Back was Clicked")
                        self.currentMode = "main"
                        self.change_mode()

                elif button.whatButton() == 15:
                    if self.buttonClick(button, mouse):
                        print("Back was Clicked")
                        f = open("data/resources/options.txt")
                        dirname = os.path.realpath(f.name)
                        print(dirname)
                        subprocess.call("explorer "+dirname, shell=True)
                        f.close()
                        self.currentMode = "main"
                        self.change_mode()


    def update(self, clock):
        self.timer += clock.get_time()
        while self.timer >= self.scrollTime:
            self.timer -= self.scrollTime
            self.background01Rect[0] += -1
            self.background02Rect[0] += -1
        if self.background01Rect[0] <= -self.background01Rect[2]:
            self.background01Rect[0] = self.background01Rect[2]

        elif self.background02Rect[0] <= -self.background02Rect[2]:
            self.background02Rect[0] = self.background02Rect[2]



    def render(self, window):
        window.blit(self.background01, self.background01Rect)
        window.blit(self.background02, self.background02Rect)
        for button in self.buttonList:
            button.draw(window)
