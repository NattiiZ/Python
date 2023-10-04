import pgzrun

TITLE = "Pygame Zero | Line"
WIDTH = 400
HEIGHT = 300


def draw():
    screen.fill('white')
    
    for n in range(1, 11):
        screen.draw.line((10,1),(250,30*n), (255, 0, 0))
    for n in range(1, 6):
        screen.draw.line((400,299),(100,50*n), (0, 0, 255))


pgzrun.go()
