import game_framework
import title_state
from pico2d import *
import play_state

running = True
image = None
logo_time = 0.0
# fill here

def enter():
    global image
    image = load_image('tuk_credit.png')
    pass

def exit():
    global image
    del image
    pass

def update():
    global logo_time
    delay(0.01)
    logo_time += 0.01
    # global running
    if logo_time > 1.0:
        logo_time = 0
        # game_framework.quit()
        game_framework.change_state(title_state)
        # running = False

    # fill here
    pass

def draw():
    global image
    clear_canvas()
    image.draw(400, 300)
    update_canvas()
    # fill here
    pass

def handle_events():
    events = get_events()


def pause():
    pass

def resume():
    pass







