import pgzrun

TITLE = "Pygame Zero | Display Text"
WIDTH = 800
HEIGHT = 600


def draw():
    screen.fill((24, 24, 24))
    
    screen.draw.text("Hello World", topleft=(10, 10), fontsize=30, color='red')
    screen.draw.text("Hello World", topright=(780, 10), fontsize=30, color='green')
    screen.draw.text("Hello World", bottomleft=(10, 580), fontsize=30, color='blue')
    screen.draw.text("Hello World", bottomright=(780, 580), fontsize=30, color='magenta')
    screen.draw.text("Hello World", center=(400, 300), fontsize=50, color='white')


pgzrun.go()
