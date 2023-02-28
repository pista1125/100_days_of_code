def turn_right():
    turn_left()
    turn_left()
    turn_left()
move()
x = 0
while not at_goal():
    if not wall_in_front():
        while object_here():
            take()
        if not front_is_clear():
            if x % 2 == 0:
                turn_right()
                move()
                turn_left()
                repeat 2:
                    move()
                turn_left()
                move()
                turn_right()
            elif x % 2 == 1:
                turn_left()
                move()
                turn_right()
                repeat 2:
                    move()
                turn_right()
                move()
                turn_left()
        if front_is_clear():
            move()
    elif wall_in_front():
        while object_here():
            take()
        if x % 2 == 0:
            turn_left()
            if not wall_in_front():
                move()
                turn_left()
                x += 1
            elif wall_in_front():
                turn_left()
                turn_left()
                while not wall_in_front():
                    move()
                turn_left()
                while not wall_in_front():
                    while object_here():
                        take()
                    move()
                while carries_object():
                    toss()
                turn_left()
                move()
                turn_right()
                repeat 2:
                    move()
                turn_right()
                move()
        elif x % 2 == 1:
            turn_right()
            if wall_in_front():
                turn_left()
                turn_left()
                while not wall_in_front():
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
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
