def loop_print(num):
    if num > 0:
        print(num)
        loop_print(num-1)


loop_print(5)