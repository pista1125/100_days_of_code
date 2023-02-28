def turn_right():
    turn_left()
    turn_left()
    turn_left()
def harvest():
    for n in range(5):
        while object_here():
            take()
        move()
    while object_here():
        take()
repeat 2:
    move()
turn_left()
repeat 2:
    move()

x = 0
for n in range(6):
    harvest()
    if x % 2 == 0:
        turn_right()
        move()
        turn_right()
    else:
        turn_left()
        move()
        turn_left()
    x += 1
    

################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
