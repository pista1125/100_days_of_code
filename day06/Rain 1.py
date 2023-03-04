def turn_right():
    turn_left()
    turn_left()
    turn_left()
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
    move()
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
