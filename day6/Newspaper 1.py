def turn_right():
    turn_left()
    turn_left()
    turn_left()

def step():
    turn_left()
    move()
    turn_right()
    repeat 2:
        move()

take()
for n in range(3):
    step()
def step_2():
    move()
    put()
    turn_left()
    turn_left()
    move()
def step_3():
    turn_left()
    turn_left()
    move()
    move()
    take()
    turn_left()
    turn_left()
    move()
    put()
    move()
step_2()
x = 0
while object_here():
    take()
    x += 1
move()

for n in range(x):
    put()
step_3()
for n in range(x):
    take()
move()
turn_left()
move()

def back_step():
    turn_right()
    repeat 2:
        move()
    turn_left()
    move()
repeat 2:
    back_step()
        
        
        
        
        
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
