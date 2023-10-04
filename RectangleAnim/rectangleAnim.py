import pgzrun


TITLE = 'Rectangle Animate'
WIDTH = 640
HEIGHT = 480
BGColor = (255, 255, 255)
x1 = int(WIDTH/2)
y1 = int(HEIGHT/2)
y2 = int(HEIGHT/2)


def draw():
    screen.fill(BGColor)
    
    screen.draw.text("Show Rectangle Animate", (250, 10), fontsize=28, color='blue')
    screen.draw.rect(Rect((100, y1),(50, 50)), color='red')
    screen.draw.filled_rect(Rect((400, y2),(50, 50)), color='green')
    screen.draw.circle((x1,240), 50, color='black')


def update():
    global x1, y1, y2
        
    y1 += 2
    if (y1 > HEIGHT+50):
        y1 = 0-50
    y2 -= 2
    if (y2 < 0):
        y2 = HEIGHT+100
        
    x1 += 3
    if (x1 > WIDTH+50):
        x1 = 0-50


pgzrun.go()