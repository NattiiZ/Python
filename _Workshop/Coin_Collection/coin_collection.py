import pgzrun
from random import randint


TITLE = 'Shoot the Fruits'
WIDTH = 800
HEIGHT = 600

score = 0
time = 0
maxtime = 30
timeout = False

fox = Actor('fox', (WIDTH/2, HEIGHT/2))
coin = Actor('coin')


# -----------------------------------------


def draw():
    if timeout:
        screen.fill('pink')
        screen.draw.text(f'Time out!, your score : {score}', center=(WIDTH/2, HEIGHT/2), fontsize=50)
    else:
        screen.fill((100, 200, 200))
        screen.draw.text(f'Score : {score}', (5, 10), fontsize=30, color='black')
        screen.draw.text(f'Time : {maxtime}', (690, 10), fontsize=30, color='black')
        fox.draw()
        coin.draw()
        

def place_coin():
    coin.x = randint(coin.width+10, WIDTH-coin.width+10)
    coin.y = randint(coin.height-10, HEIGHT-coin.height+10)
    
def update():
    global score
    
    if (keyboard.LEFT):
        fox.x -= 5
    elif (keyboard.RIGHT):
        fox.x += 5
    elif (keyboard.UP):
        fox.y -= 5
    elif (keyboard.DOWN):
        fox.y += 5
        
    if (fox.colliderect(coin)):
        sounds.ping.play()
        score += 1
        place_coin()
        
        
def count_time():
    global maxtime, timeout
    
    maxtime -= 1
    if (time==maxtime):
        timeout = True
        clock.unschedule(count_time)
    


# -----------------------------------------

place_coin()
clock.schedule_interval(count_time, 1.0)

pgzrun.go()