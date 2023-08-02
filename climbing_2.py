from stanfordkarel import move, turn_left, put_beeper, run_karel_program

i = 0
while i < 4:
    move()
    i = i + 1


def straight():
    while front_is_clear():
        move()


def turn_right():
    turn_left()
    turn_left()
    turn_left()


def sweep_straight():
    while front_is_clear():
        move()
        if beepers_present():
            pick_beeper()


def loop():
    for i in range(4):
        turn_right()
        turn_left()
        sweep_straight()
        straight()
        straight_down_up()


#         turn_right()
#         move()
#         turn_right()
#         sweep_straight()
#         turn_left()
#         move()
#         pick_beeper()
#         turn_left()
#         sweep_straight()

def straight_down_up():
    turn_right()
    move()
    turn_right()
    sweep_straight()
    turn_left()
    move()
    pick_beeper()
    turn_left()
    sweep_straight()


def ok_loop():
    for i in range(3):
        straight_down_up()


def ok_2():
    turn_right()
    move()
    turn_right()
    sweep_straight()


def loop_3():
    pick_beeper()
    turn_left()
    sweep_straight()
    # straight()
    straight_down_up()


def row_sweep():
    while front_is_clear() and beepers_present():
        pick_beeper()
        move()


def row_down():
    turn_left()
    turn_left()
    sweep_straight()


#		turn_right()
# #     move()
# #     turn_right()
# #     sweep_straight()

# #     turn_left()
# #     move()
# #     pick_beeper()
# #     turn_left()
# #     sweep_straight()
def loop_pick():
    while front_is_clear():
        loop_row()
        turn_left()
        if front_is_clear():
            move()
            turn_left()



def angle():
    turn_left()



def loop_row():
    row_sweep()
    row_down()


def main():
    turn_left()
    loop_pick()
    print("after loop_pick")

    # loop_3()
    # ok_loop()
    # ok_2()


if __name__ == "__main__":
    run_karel_program("karel_conditional_climbing_wider")

