import pgzrun


TITLE = 'UFO Animate'
WIDTH = 800
HEIGHT = 600

ufo = Actor('ufo')


# -----------------------------------------------------


def draw():
    screen.fill((100, 100, 100))
    screen.draw.text('1. linear ', (200, 50), fontsize=28)
    screen.draw.text('2. accelerate ', (200, 100), fontsize=28)
    screen.draw.text('3. decelerate ', (200, 150), fontsize=28)
    screen.draw.text('4. accel_decel ', (200, 200), fontsize=28)
    screen.draw.text('5. bounce_end ', (200, 250), fontsize=28)
    screen.draw.text('6. bounce_start ', (200, 300), fontsize=28)
    screen.draw.text('7. bounce_start_end ', (200, 350), fontsize=28)
    ufo.draw()
        

def on_key_down(key, mod, unicode):
    if (key==keys.K_1):
        animate(ufo, pos=(WIDTH, HEIGHT), tween='linear', on_finished=reset_ufo)
    elif (key==keys.K_2):
        animate(ufo, pos=(WIDTH, HEIGHT), tween='accelerate', on_finished=reset_ufo)
    elif (key==keys.K_3):
        animate(ufo, pos=(WIDTH, HEIGHT), tween='decelerate', on_finished=reset_ufo)
    elif (key==keys.K_4):
        animate(ufo, pos=(WIDTH, HEIGHT), tween='accel_decel', on_finished=reset_ufo)
    elif (key==keys.K_5):
        animate(ufo, pos=(WIDTH, HEIGHT), tween='bounce_end', on_finished=reset_ufo)
    elif (key==keys.K_6):
        animate(ufo,pos=(WIDTH, HEIGHT), tween='bounce_start', on_finished=reset_ufo)
    elif (key==keys.K_7):
        animate(ufo, pos=(WIDTH, HEIGHT), tween='bounce_start_end', on_finished=reset_ufo)
    ufo.draw()
    
        
def reset_ufo():
    ufo.pos = (ufo.width/2, ufo.height/2)

        
pgzrun.go()