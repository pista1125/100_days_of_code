def turn_right():
    turn_left()
    turn_left()
    turn_left()
def one_back():
    repeat 2:   
        turn_left()
    move()
    repeat 2:
        turn_left()
    turn_right()
    move()
    return object_here()
repeat 2:
    move()
turn_left()
repeat 2:
    move()
game_on = True
while game_on:
    if object_here():
        take()
        move()
    else:
        game_on = one_back()
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
