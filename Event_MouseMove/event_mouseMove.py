import pgzrun


TITLE = 'Event Mouse Move'
WIDTH = 640
HEIGHT = 480
apple = Actor('apple', (WIDTH/2, HEIGHT/2))
strShow = ''


def draw():
    screen.fill('white')
    screen.draw.text('Show move mouse to move image', (200, 10), color='blue')
    screen.draw.text(strShow, (10,440), color='blue')
    apple.draw()
    
    
def on_mouse_move(pos, rel, buttons):
    global strShow
    
    strShow = f'Rel : {rel} , Pos : {pos}'
    if (mouse.LEFT in buttons):
        apple.pos = pos
    
    
pgzrun.go()