import pgzrun

TITLE = "Pygame Zero | Circle"
WIDTH = 400
HEIGHT = 300


def draw():
    screen.fill('white')
    screen.draw.circle((80, 80), 40, (255, 0, 0))
    screen.draw.circle((160, 80), 40, (255, 0, 0))
    screen.draw.circle((240, 80), 40, (255, 0, 0))
    screen.draw.circle((320, 80), 40, (255, 0, 0))
    for n in range(1, 6):
        screen.draw.circle((200, 150), 25*n, 'blue')


pgzrun.go()
