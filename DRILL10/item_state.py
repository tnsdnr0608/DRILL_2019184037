import pico2d

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
    image = load_image('add_delete_boy.png')
    pass

def exit():
    global image
    del image
    pass

def update():
    play_state.update()
    # fill here
    pass

def draw():
    global image
    clear_canvas()
    play_state.draw_world()
    image.draw(400, 300)
    update_canvas()
    # fill here
    pass

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            match event.key:
                case pico2d.SDLK_ESCAPE:
                    game_framework.pop_state() #이전 상태인 play_state로 복귀
                case pico2d.SDLK_0:
                    play_state.boy.item = None
                case pico2d.SDLK_k:
                    play_state.boy.item = 'p'
                    game_framework.pop_state()
                case pico2d.SDLK_j:
                    play_state.boy.item = 'm'
                    game_framework.pop_state()


def pause():
    pass

def resume():
    pass









