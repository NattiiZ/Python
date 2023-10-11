import pgzrun


TITLE = 'Test Music'
WIDTH = 640
HEIGHT = 480


# --------------------------------------------------------------


def draw():
    screen.clear()
    screen.draw.text('Program Test Music', center=(320, 30), fontsize=40)
    screen.draw.text('1. Alone Heart', (250, 100), fontsize=36)
    screen.draw.text('2. Always', (250, 150), fontsize=36)
    screen.draw.text('3. Carrie', (250, 200), fontsize=36)
    screen.draw.text('4. I Think I', (250, 250), fontsize=36)
    screen.draw.text('S. Stop Music', (250, 300), fontsize=36)
    screen.draw.text('Select Music', (220, 350), fontsize=36)

 
def on_key_down(key, mod, unicode):
    if (key==keys.K_1):
        music.play_once('alone_heart')  
    elif (key==keys.K_2):
        music.play_once('always')
    elif (key==keys.K_3):
        music.play_once('carrie')
    elif (key==keys.K_4):
        music.play_once('i_think_i')
    elif (key==keys.S):
        music.stop()
    
pgzrun.go()