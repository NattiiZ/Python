import pgzrun


TITLE = 'Character Animate'
WIDTH = 640
HEIGHT = 800

index = 0

imgName = ['boy_1', 'boy_2', 'boy_3', 'boy_4']
boy = Actor('boy_1', (WIDTH/2, HEIGHT/2))
boy1 = Actor('boy_1')
boy2 = Actor('boy_2')
boy3 = Actor('boy_3')
boy4 = Actor('boy_4')


# -----------------------------------------------------


def draw():
    screen.fill('white')
    if (index==0):
        boy1.draw()
    elif (index==1):
        boy2.draw()
    elif (index==2):
        boy3.draw()
    elif (index==3):
        boy4.draw()
    boy.draw()
        

def count_index():
    global index
    
    index = (index+1)%4
    boy.image = imgName[index]


clock.schedule_interval(count_index, 0.1)
        
pgzrun.go()