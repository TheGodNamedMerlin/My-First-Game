import pygame as pg, sys
from data import Load, States


def get_events(current_state):
    for event in pg.event.get():
        if event.type == pg.QUIT:
            return False

        current_state.update_event(event)




    current_state.get_events(current_state)
    return True


def update(current_state, Clock):
    current_state.update(Clock)
    pg.display.set_caption("FPS: " + str(Clock)[14:16])


def render(window, current_state):
    window.fill((255, 255, 255))
    current_state.render(window)


def run():

    pg.init()

    game_options = Load.load_options()

    save_data = Load.load_save_data()

    background_images = Load.load_background_images()

    if game_options[4][1] == "FULLSCREEN":
        window = pg.display.set_mode((1280,720), pg.FULLSCREEN)
    else:
        window = pg.display.set_mode((1280,720))

    #levels are saved as strings due to how loading files work

    Clock = pg.time.Clock()

    current_state = States.Current_state(States.MainMenu(), save_data, background_images, Clock)

    running = True

    while running:

        Clock.tick(60)


        running = get_events(current_state)

        update(current_state, Clock)

        render(window, current_state)

        pg.display.update()

    pg.quit()
    sys.exit()

