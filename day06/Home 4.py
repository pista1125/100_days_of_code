def turn_right():
    turn_left()
    turn_left()
    turn_left()

def step():
    repeat 3:
        move()
    turn_left()
    repeat 3:
        move()
    turn_right()
    move()
    turn_right()

repeat 3:
    step()
repeat 3:
    move()
turn_left()
repeat 3:
    move()
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
