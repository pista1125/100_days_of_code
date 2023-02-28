def turn_right():
    turn_left()
    turn_left()
    turn_left()
i = 0
while front_is_clear():
    move()
    i +=1
repeat 2:
    turn_left()
a = int(i / 2)
for _ in range(a):
    move()
put()

################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
