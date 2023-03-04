def turn_right():
    turn_left()
    turn_left()
    turn_left()
a = 500
while a > 464:
    if front_is_clear():
        move()
        put()
        a -= 1
    else:
        turn_left()
    
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
