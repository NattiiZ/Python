import pgzrun

TITLE = "Pygame Zero | Fill Circle"
WIDTH = 400
HEIGHT = 300


def draw():
    screen.clear()
    
    screen.draw.filled_circle((80, 60), 40, (255, 255, 0))
    screen.draw.filled_circle((160, 60), 40, (255, 255, 0))
    screen.draw.filled_circle((240, 60), 40, (255, 255, 0))
    screen.draw.filled_circle((320, 60), 40, (255, 255, 0))
    
    Colors = ('red', 'green', 'blue', 'white')
    
    for n in range(4):
        screen.draw.filled_circle((200, 200), 25*(4-n), Colors[n])


pgzrun.go()
