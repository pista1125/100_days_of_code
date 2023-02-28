def turn_right():
    turn_left()
    turn_left()
    turn_left()
x = 1
y = 1
view = 0
game_on = True
move_on_x = True
while game_on:
    print(f" x = {x}, y = {y}, view = {view} ")
    if front_is_clear():
        move()
        if move_on_x:
            if view == 0 or view == 1:
                x += 1
            else:
                x -=1
        else:
            if view == 0 or view == 1:
                y += 1
            else:
                y -= 1
    else:
        turn_left()
        if view == 3:
            view = 0
        else:
            view += 1
        move_on_x = not move_on_x
    if x == 1 and y ==1:
        done()

################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
