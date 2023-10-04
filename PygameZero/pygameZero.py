import pgzrun

TITLE = "Pygame Zero | Demo"
WIDTH = 800
HEIGHT = 600


def draw():
    screen.clear()
    screen.draw.text("Hello World", topleft=(10, 10), fontsize=30)
   

pgzrun.go()
