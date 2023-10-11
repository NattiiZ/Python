import pgzrun


TITLE = 'Change position and move image'
WIDTH = 400
HEIGHT = 300
logo = Actor('it_logo', (0, 0))


def draw():
    screen.fill('white')
    screen.draw.text('Change Postion and Diaplay', topright=(380, 30), color='blue')
    
    logo.draw()


def update():
    if (logo.x < WIDTH):
        logo.x += 1
    else:
        logo.x = 0
    
    if (logo.y < HEIGHT):
        logo.y += 1
    else:
        logo.y = 0 

        
pgzrun.go()