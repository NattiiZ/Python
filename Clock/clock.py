import pgzrun


TITLE = 'Test Clock'
WIDTH = 400
HEIGHT = 300

time1 = time2 = 0


# -----------------------------------------------------


def draw():
    screen.fill((255, 255, 255))
    screen.draw.text(f'Time 1 : {time1}', (10, 10), color='blue')
    screen.draw.text(f'Time 2 : {time2}', topright=(WIDTH-10, 10), color='magenta')


def on_mouse_down(pos, button):
    clock.schedule(count_time_1, 0.01)
    

def count_time_1():
    global time1
    
    time1 += 1


def count_time_2():
    global time2
    
    time2 += 1
    if (time2==20):
        clock.unschedule(count_time_2)
        print('stop clock')


clock.schedule(count_time_1, 5.0)
clock.schedule_interval(count_time_2, 1.0)
        
pgzrun.go()