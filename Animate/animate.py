import pgzrun


TITLE = 'Test Animate'
WIDTH = 640
HEIGHT = 480
ufo = Actor('ufo')


# -----------------------------------------------------


def draw():
    screen.fill('white')
    ufo.draw()


def on_mouse_down(pos, button):
    if (button==mouse.LEFT):
        posM = pos
        animate(ufo, pos=posM, duration=5, on_finished=finish)
    

def finish():
    ufo.pos = (0, 0)
    animate(ufo, pos=(WIDTH, HEIGHT), on_finished=finish)


# animate(ufo, pos=(WIDTH, HEIGHT), duration=5, on_finished=finish)
        
pgzrun.go()