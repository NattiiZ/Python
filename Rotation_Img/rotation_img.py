import pgzrun


TITLE = 'Rotation Image'
WIDTH = 400
HEIGHT = 300
apple = Actor('apple')
apple.pos = (WIDTH/2, HEIGHT/2)


def draw():
    screen.fill('white')
    screen.draw.text('Rotation Image', center=(WIDTH/2,20), color='blue')
    screen.draw.text('Rotation Angle : ' + str(apple.angle), (50, 260), color='blue')
    apple.draw()


def update():
    apple.angle -= 3
    if (apple.angle <= -360):
        apple.angle = 0

        
pgzrun.go()