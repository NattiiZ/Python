import pgzrun


TITLE = 'Event Keyboard Control Image'
WIDTH = 640
HEIGHT = 480
apple1 =Actor('apple', (WIDTH/2, HEIGHT/2))
apple2 =Actor('apple', (WIDTH/2, HEIGHT/2))
# apple2 = apple1
Play1= False


def draw():
    screen.fill('white')
    screen.draw.text('Show animate image', center=(WIDTH/2, 10), color='blue')
    screen.draw.text('Apple1 start(P) and stop(S)', center=(20, 40), color='blue')
    screen.draw.text('Apple2 use key U and D', center=(20, 80), color='blue')
    apple1.draw()
    apple2.draw()
    
    
def update():
    if (Play1):
        apple1.x += 1
        if (apple1.x > WIDTH):
            apple1.x = 0
    
    
def on_key_down(key, mod, unicode):
    global Play1
    
    if (key==keys.P):
        Play1 = True
    elif (key==keys.S):
        Play1 = False
    elif (key==keys.U):
        apple2.y -= 5
    elif (key==keys.D):
        apple2.y += 5
        
    
    
pgzrun.go()