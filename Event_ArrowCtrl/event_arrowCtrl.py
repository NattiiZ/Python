import pgzrun


TITLE = 'Event Keyboard Control Image'
WIDTH = 640
HEIGHT = 480
apple =Actor('apple', (WIDTH/2, HEIGHT/2))


def draw():
    screen.fill('white')
    screen.draw.text('Move image with Arrow key', (200, 10), color='blue')
    apple.draw()


def on_key_down(key, mod, unicode):
    if (key==keys.LEFT):
        apple.x -= 10
    elif (key==keys.RIGHT):
        apple.x += 10
    elif (key==keys.UP):
        apple.y -= 10
    elif (key==keys.DOWN):
        apple.y += 10
    elif (key==keys.F1):
        apple.x = WIDTH/2
        apple.y = HEIGHT/2


pgzrun.go()