import pgzrun

TITLE = "Pygame Zero | Rectangle"
WIDTH = 400
HEIGHT = 300


def draw():
    screen.clear()
    
    screen.draw.rect(Rect((0, 0), (200, 150)), (255, 255, 255))
    screen.draw.rect(Rect((200, 0), (200, 150)), (0, 255, 0))
    screen.draw.rect(Rect((0, 150), (200, 150)), (0, 255, 0))
    screen.draw.rect(Rect((200, 150), (200, 150)), (255, 255, 255))
    
    for n in range(5):
        screen.draw.rect(Rect((150+(n*10), 100+(n*10)), (100, 100)), 'yellow')


pgzrun.go()
