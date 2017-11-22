import game_framework
import logo_Scene
from pico2d import *


name = "StartState"
image = None
logo_time = 0.0


def enter():            #handle_event 을 실행
    global image
    image = load_image('png/kpu.png')
    pass

def exit():
    global image
    del(image)
    pass


def update(frame_time):
    global logo_time

    if(logo_time > 1.0):
        logo_time = 0
        #game_framework.quit()
        game_framework.push_state(logo_Scene)      #start state의 pause를 먼저 수행. -> title_state의 enter 실행.
                                                    # 현재 상태에 머무른 뒤에  ,.... pop으로 돌아오기.
        #game_framework.change_state(title_state)      # 현재상태의 exit를 수행함. 에러발생.
    delay(0.01)
    logo_time += 0.01


def draw(frame_time):
    global image
    clear_canvas()
    image.draw(400, 300)
    update_canvas()




def handle_events(frame_time):        #update, draw 실행.
    events = get_events()
    pass


def pause(): pass


def resume(): pass      # exit 수행.



