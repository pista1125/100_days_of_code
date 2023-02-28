def turn_right():
    turn_left()
    turn_left()
    turn_left()
a = 500
put()
move()
while a > 400:
    if object_here():
        done()
    elif front_is_clear():
        move()
    else:
        turn_left()
    
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
