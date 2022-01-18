from pgzrun import go
import random
WIDTH = 480
HEIGHT = 360
TITLE = "Ninja Cube"

cube = Actor("ninja cube", (30, 180))
rain = Actor("rain", (1000, 1000))
pause = Actor("pause", (440, 40))
pause_window = Actor("pause window")
run = Actor("run", (240, 220))
game_over_window = Actor("game over window")
restart = Actor("restart", (240, 180))
barriers = []
map = []
mode = "game"
sound_play = 1

meters = 0
repeat_playback = 0
music.play('the sound of footsteps')

for i in range(12):
    map.append(Actor("scroll", (80 * i, 180)))

def draw():
    global mode
    for i in range(len(map)):
        map[i].draw()
    for i in range(len(barriers)):
        barriers[i].draw()
    cube.draw()
    rain.draw()
    screen.draw.text(f"{meters}", pos=(10, 0), color='white', fontsize=30, fontname="monsterrat")
    pause.draw()

    if mode == "pause":
        music.pause()
        screen.clear()
        pause_window.draw()
        run.draw()
    else:
        music.unpause()

    if mode == "game over":
        game_over_window.draw()
        restart.draw()
        screen.draw.text(f"{meters}", pos=(10, 0), color='white', fontsize=30, fontname="monsterrat")


def update(dt):
    global meters, repeat_playback, rain, mode
    if mode == "game":
        for i in range(len(map)):
            map[i].x -= 5
        for i in range(len(barriers)):
            barriers[i].x -= 5
        for i in range(len(barriers)):
            if cube.colliderect(barriers[i]):
                music.stop()
                music.play_once("game over")
                mode = "game over"
        for i in range(len(map)):
            if map[i].x < -40:
                map.pop(i)
                map.append(Actor("scroll", (520, 180)))
                if random.randint(1,6) == 1:
                    barriers.append(Actor("block", (520, random.randint(110, 240))))
                meters += 1
                repeat_playback += 1
        if meters > 100 and meters < 201:
            rain = Actor("rain", (random.randint(0, 480), random.randint(0, 360)))
        else:
            rain = Actor("rain", (1000, 1000))
        if meters == 100:
            music.play('rain')
        if repeat_playback == 40:
            if meters < 100 or meters > 200:
                music.play('the sound of footsteps')
            else:
                if meters < 200:
                    music.play('rain')
                else:
                    music.stop()
            repeat_playback = 0
        if cube.y > 85 and keyboard.up:
            cube.y -= 5
        if cube.y < 225 and keyboard.down:
            cube.y += 5

def on_mouse_down(pos):
    global mode, barriers, meters, repeat_playback
    if pause.collidepoint(pos):
        mode = "pause"
    if run.collidepoint(pos):
        mode = "game"
    if restart.collidepoint(pos):
        mode = "game"
        generate_map()
        barriers = []
        music.play('the sound of footsteps')
        meters = 0
        repeat_playback = 0

def generate_map():
    map = []
    for i in range(12):
        map.append(Actor("scroll", (80 * i, 180)))


go()