from pico2d import *

TUK_WIDTH, TUK_HEIGHT = 1280, 1024

def handle_events():
    # fill here
    global running
    global dir
    global dir_y
    global move
    events = get_events()

    for event in events:
        if event.type == SDL_QUIT:
            running = False

        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                move = 1
                dir += 1
            elif event.key == SDLK_LEFT:
                move = 0
                dir -= 1
            elif event.key == SDLK_UP:
                if move == 0:
                    move = 2
                elif move == 1:
                    move = 3
                dir_y += 1
            elif event.key == SDLK_DOWN:
                if move == 0:
                    move = 2
                elif move == 1:
                    move = 3
                dir_y -= 1
            elif event.key == SDLK_ESCAPE:
                running == False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dir -= 1
            elif event.key == SDLK_LEFT:
                dir += 1
            elif event.key == SDLK_UP:
                dir_y -= 1
            elif event.key == SDLK_DOWN:
                dir_y += 1

open_canvas(TUK_WIDTH, TUK_HEIGHT)
character = load_image('animation_sheet.png')
TUK_GROUND = load_image("TUK_GROUND.png")

running = True
handle_events()
x = 1280 // 2
y = 1024 // 2
frame = 0
dir = 0
dir_y = 0
move = 0

while running:
    clear_canvas()
    TUK_GROUND.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    character.clip_draw(frame * 100, 100 * move, 100, 100, x, y)
    update_canvas()
    frame = (frame + 1) % 8
    handle_events()
    if x < 0:
        exit(1)
    elif x > TUK_WIDTH:
        exit(1)
    if y < 0:
        exit(1)
    elif y > TUK_HEIGHT:
        exit(1)

    x += dir * 5
    y += dir_y * 5

    delay(0.01)

close_canvas()
