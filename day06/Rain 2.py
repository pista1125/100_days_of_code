def turn_right():
    turn_left()
    turn_left()
    turn_left()
repeat 3:
    move()
turn_right()
move()

x = 0
while not at_goal():
    if not wall_on_right():
        move()
        if wall_on_right():
            repeat 2:
                turn_left()
            move()
            turn_left()
            build_wall()
            turn_left()
        else:
            turn_right()
            move()
            turn_left()
    elif wall_on_right():
        if front_is_clear():
            move()
        elif x == 3:
            turn_left()
            move()
            turn_right()
            move()
            x += 1
        elif not front_is_clear():
            turn_left()
            x += 1
        
     
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################

def turn_right():
    turn_left()
    turn_left()
    turn_left()
repeat 3:
    move()
turn_right()
move()
x = 0
y = 1
switch = 0
while x < 4:
    if wall_on_right() and front_is_clear():
        if switch == 0:
            move()
            y += 1
        else:
            move()
    elif not wall_on_right():
        turn_right()
        build_wall()
        turn_left()
        move()
    elif not front_is_clear():
        turn_left()
        x += 1
        switch += 1
    elif front_is_clear():
        move()
        
for n in range(y):