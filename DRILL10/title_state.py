import game_framework
from pico2d import *
import play_state
import logo_state

image = None

def enter():
    global image
    image = load_image('title.png')
    # fill here
    pass

def exit():
    global image
    del image
    # fill here
    pass

def handle_events():
    events = get_events()
    for event in events:
        if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
            game_framework.change_state(play_state)
    # fill here
    pass

def draw():
    clear_canvas()
    image.draw(400, 300)
    update_canvas()

def update():
    pass

def pause():
    pass

def resume():
    pass