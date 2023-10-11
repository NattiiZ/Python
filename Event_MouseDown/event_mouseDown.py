import pgzrun


TITLE = 'Event Mouse Down'
WIDTH = 640
HEIGHT = 480
apple = Actor('apple')
apple.pos = (WIDTH/2, HEIGHT/2)


def draw():
    screen.fill('white')
    screen.draw.text('Press click mouse', (200, 10), color='blue')
    apple.draw()
    
    
def on_mouse_down(pos, button):
    apple.pos = pos
    print(button) 
    
    
pgzrun.go()