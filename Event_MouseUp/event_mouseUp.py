import pgzrun


TITLE = 'Event Mouse UP'
WIDTH = 640
HEIGHT = 480
apple = Actor('apple')
apple.pos = (WIDTH/2, HEIGHT/2)
showStr = ''


def draw():
    screen.fill('white')
    screen.draw.text('Press click and release mouse', (200, 10), color='blue')
    screen.draw.text(showStr, (20,400), color='blue')
    apple.draw()
    
    
def on_mouse_up(pos, button):
    global showStr
    
    apple.pos = pos
    showStr = f'Pos : {pos} , Button : {button}'
    
    
pgzrun.go()