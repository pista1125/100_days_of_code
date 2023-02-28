def turn_right():
    turn_left()
    turn_left()
    turn_left()
move()
x = 0
while not at_goal():
    if front_is_clear():
        while object_here():
            take()
        move()
    elif not front_is_clear():
        while object_here():
            take()
        if x % 2 == 0:
            turn_left()
            move()
            turn_left()
            x += 1
        elif x % 2 == 1:
            turn_right()
            if not front_is_clear():
                turn_left()
                turn_left()
                repeat 3:
                    move()
                while object_here():
                    take()
                while carries_object():
                    toss()
                turn_left()
                move()
                turn_right()
                repeat 2:
                    move()
                turn_right()
                move()
            else:    
                move()
                turn_right()
                x += 1
def step_back():
    turn_left()
    move()
    turn_left()
    repeat 4:
        move()
    while carries_object():
        toss()

################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
