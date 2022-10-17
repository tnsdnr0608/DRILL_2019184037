import game_framework
import item_state
import random
from pico2d import *

class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)

class Boy:
    def __init__(self):
        self.x, self.y = 0, 90
        self.frame = 0
        self.dir = 1
        self.item = None
        self.image = load_image('animation_sheet.png')

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += self.dir * 1
        if self.x > 800:
            self.x = 800
            self.dir = -1
        elif self.x < 0:
            self.x = 0
            self.dir = 1

    def draw(self):
        if self.dir == 1:
            self.image.clip_draw(self.frame*100, 100, 100, 100, self.x, self.y)
        elif self.dir == -1:
            self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)
        if self.item == 'p':
            self.image.clip_draw(self.frame * 100, 100, 100, 100, self.x, self.y)
            self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)
            self.x, self.y = random.randint(100, 700), 9
        elif self.item == 'm':
            self.boy -= boy


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                game_framework.quit()
            elif event.key == SDLK_b:
                game_framework.push_state(item_state)

boy = None
grass = None


# running  = None

def enter():
    global boy, grass, running
    boy = Boy()
    grass = Grass()
    running = True

def exit():
    global boy, grass
    del boy
    del grass

def update():
    boy.update()
    pass

def draw():
    clear_canvas()
    draw_world()
    update_canvas()


def draw_world():
    grass.draw()
    boy.draw()


def pause():
    pass

def resume():
    pass

# running = True