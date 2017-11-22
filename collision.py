from pico2d import *

import game_framework


from objects import Player #, item # import Boy class from boy.py
from Enemy import Enemy
from map import map


name = "collision"

pacman = None
ghost = [None]*4
item_set = [None] *8
world_map = None

#enemy__collision_check = None

def create_world():
    global pacman, ghost, item_set, world_map
    pacman = Player()
    ghost = [Enemy(35, 565, 1),Enemy(565, 35, 2),Enemy(565, 565, 3),Enemy(350, 390, 4)]
 #   item_set = [item(1), item(1), item(1), item(1)
  #              ,item(5), item(6), item(7), item(8)]
    world_map = map()


def destroy_world():
    global pacman, ghost, item_set, world_map

    del(pacman)
    del(ghost)
    del(item_set)
    del(world_map)



def enter():
    game_framework.reset_time()
    create_world()


def exit():
    destroy_world()


def pause():
    pass


def resume():
    pass


def handle_events(frame_time):
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            else:
                pacman.handle_event(event)



def collide(a, b):
    # fill here
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()
    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False
    return True


def update(frame_time):
    pacman.update(frame_time)
    for g in ghost:
        g.update(frame_time)

    # fill here
#    for ball in balls:
#        if collide(boy, ball):
 #           balls.remove(ball)

#    for ball in big_balls_for_collision_check:
 #       if collide(grass, ball):
 #           ball.stop()
  #          big_balls_for_collision_check.remove(ball)

    delay(0.5)

def draw(frame_time):
    clear_canvas()
#    world_map.draw()
    pacman.draw()

    for g in ghost:
        g.draw()

    for i in range(25):
        for j in range(23):
            if world_map.mapdata[i][22-j]==1:
                draw_rectangle(j*26, 600-i*24,  (j+1)*26, 600-((i+1)*24))

    update_canvas()
