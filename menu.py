import game_framework
import collision

from pico2d import*

name = "Menu"
image_menu = None
state = None

def enter():
    global image_menu, state
    image_menu = load_image('resource/png/main_ready.png')
    state = 1

def exit():
    global image_menu
    del(image_menu)


def draw(frame_time):
    global image_menu
    clear_canvas()
    image_menu.draw(400, 300)
    update_canvas()

def handle_events(frame_time):
    global image_menu, state
    events = get_events()
    for event in events:
        #if(event.type == SDL_BUTTON_LEFT)
        if (event.type, event.key) == (SDL_KEYDOWN, SDLK_UP):
            image_menu = load_image('resource/png/main_ready.png')
            state = 1
        elif  (event.type, event.key) == (SDL_KEYDOWN, SDLK_DOWN):
            image_menu = load_image('resource/png/main_exit.png')
            state = 0
        elif  (event.type, event.key) == (SDL_KEYDOWN, SDLK_RETURN):
            if state == 0:
                game_framework.quit()
            elif state == 1:
                game_framework.change_state(collision)

def update(frame_time):
    pass



def pause():
    pass


def resume():
    pass
