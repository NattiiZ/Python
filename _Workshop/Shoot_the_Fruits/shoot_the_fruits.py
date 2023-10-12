import pgzrun
from random import randint


TITLE = 'Shoot the Fruits'
WIDTH = 800
HEIGHT = 600

score = 0

apple = Actor('apple')
orange = Actor('orange')


# -----------------------------------------


def draw():
    screen.fill((100, 200, 200))
    screen.draw.text(f'Score : {score}', (10, 10), fontsize=30, color='black')
    apple.draw()
    orange.draw()
    
    
def place_apple():
    apple.x = randint(apple.width, WIDTH-apple.width)
    apple.y = -50
    apple.speed = randint(3, 5)
    
    
def place_orange():
    orange.x = randint(orange.width, WIDTH-orange.width)
    orange.y = -70
    orange.speed = randint(3, 5)
    

def on_mouse_down(pos, button):
    global score
    
    if (button==mouse.LEFT and apple.collidepoint(pos)):
        sounds.ping.play()
        print('+1')
        score += 1
        place_apple()
    if (button==mouse.LEFT and orange.collidepoint(pos)):
        sounds.ping.play()
        print('+1')
        score += 1
        place_orange()
        
    
def update():
    apple.y += apple.speed
    if (apple.y > HEIGHT):
        print('Apple miss')
        place_apple()
        
    orange.y += orange.speed
    if (orange.y > HEIGHT):
        print('Orange miss')
        place_orange()


# -----------------------------------------


place_apple()
place_orange()

pgzrun.go()