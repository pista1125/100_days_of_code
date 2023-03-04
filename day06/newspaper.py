def turn_right():
    turn_left()
    turn_left()
    turn_left()
def up_two_step():
    move()
    move()
def step():
    turn_left()
    move()
    turn_right()
    up_two_step()

take()
for n in range(3):
    step()
put()
turn_left()
turn_left()
def back_step():
    up_two_step()
    turn_left()
    move()
    turn_right()
for x in range(3):
    back_step()