import pgzrun


TITLE = 'Event Keyboard'
WIDTH = 640
HEIGHT = 480
strDown = strUp = ''


def draw():
    screen.fill('white')
    screen.draw.text(strDown, (10, 400), color='blue')
    screen.draw.text(strUp, (10,440), color='blue')
    
    
def on_key_down(key, mod, unicode):
    global strDown
    
    print('Key DOWN : ', key, unicode, mod)
    strDown = f'Key DOWN : {key}, {mod}'
    

def on_key_up(key, mod):
    global strUp
    
    print('Key Up   : ', key, mod)
    strUp = f'Key UP         : {key}, {mod}'
    
    
pgzrun.go()