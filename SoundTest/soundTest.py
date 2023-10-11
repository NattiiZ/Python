import pgzrun


TITLE = 'Test Sound'
WIDTH = 640
HEIGHT = 480


# --------------------------------------------------------------


def draw():
    screen.fill((100, 100, 100))
    screen.draw.text('Program Test Sound', (200, 10), fontsize=40)
    screen.draw.text('1. Bird', (250, 50), fontsize=36)
    screen.draw.text('2. Bug', (250, 90), fontsize=36)
    screen.draw.text('3. Dog', (250, 130), fontsize=36)
    screen.draw.text('4. Droid', (250, 170), fontsize=36)
    screen.draw.text('5. Duck', (250, 210), fontsize=36)
    screen.draw.text('Select Sound', (250, 250), fontsize=36)

 
def on_key_down(key, mod, unicode):
    if (key==keys.K_1):
        sounds.bird.play()    
    elif (key==keys.K_2):
        sounds.bug.play()    
    elif (key==keys.K_3):
        sounds.dog.play()    
    elif (key==keys.K_4):
        sounds.droid.play()    
    elif (key==keys.K_5):
        sounds.duck.play()
        
    
pgzrun.go()