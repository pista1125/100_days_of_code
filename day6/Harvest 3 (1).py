def turn_right():
    turn_left()
    turn_left()
    turn_left()

repeat 2:
    move()
turn_left()
repeat 2:
    move()
game_1 = 0
def harvest():
    for n in range(5):
        if object_here():
            while object_here():
                take()
            put()
            move()
        elif not object_here():
            put()
            move()
    for n in range(1):
        if object_here():
            while object_here():
                take()
            put()
        elif not object_here():
            put()

for n in range(5):
    harvest()
    if n % 2 == 0:
        turn_right()
        move()
        turn_right()
    elif n % 2 == 1:
        turn_left()
        move()
        turn_left()
harvest()
        
        
        
        
        
        
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
