def turn_right():
    turn_left()
    turn_left()
    turn_left()
a = 500
put()
turn_left()
move()
while a == 500:
    if object_here():
        done()
    elif not wall_on_right():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()
    
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
