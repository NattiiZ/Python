import pgzrun


TITLE = 'Load and Display Image'
WIDTH = 400
HEIGHT = 300
logo = Actor('it_logo')
apple = Actor('apple', (350, 250))


def draw():
    screen.fill('white')
    
    logo.draw()
    screen.draw.text('Logo Width : %d' %logo.width, (200, 50), color='blue')
    screen.draw.text('Logo height : %d' %logo.height, (200, 80), color='blue')
    
    apple.draw()
    screen.draw.text('Apple Width : %d' %apple.width, (50, 200), color='blue')
    screen.draw.text('Apple Height : %d' %apple.height, (50, 250), color='blue')

        
pgzrun.go()