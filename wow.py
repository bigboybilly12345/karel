from stanfordkarel import move, turn_left, put_beeper, front_is_blocked, run_karel_program

def move_if_blocked_turn_left():
    if front_is_blocked():
        turn_left()
        move()
        turn_right()
        move()
        turn_right()
        move()
    else:
        move()

def test_2():
    turn_left()
    sweep()
    change_right_top()
    sweep()
    change_right_bottom()
    sweep()
    change_right_top()
    sweep()
    change_right_bottom()
    sweep()
    move_if_blocked_turn_left()
    turn_left()
    sweep()
    reverse_change_right_top()

def reverse_change_right_top():
    turn_left()
    move()
    turn_left()
    sweep()
def test():
    test_2()


def change_right_bottom():
    turn_left()
    move_if_blocked_turn_left()
    turn_left()
def sweep():
    while front_is_clear():
        move_if_blocked_turn_left()
        if beepers_present():
            pick_beeper()

def change_left():
    turn_left()
    move_if_blocked_turn_left()
    turn_left()
    if beepers_present():
        pick_beeper()

def change_right_top():
    turn_right()
    move_if_blocked_turn_left()
    turn_right()
    if beepers_present():
        pick_beeper()
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def row_2():
    while front_is_clear():
        turn_left()
        sweep()
        turn_right()
        move_if_blocked_turn_left()
        turn_right()
        sweep()
        turn_left()
        move_if_blocked_turn_left()
        turn_left()
        sweep()
        turn_left()
        turn_left()
        sweep()
        turn_left()
        move_if_blocked_turn_left()
        turn_left()
        sweep()
        turn_right()
        move_if_blocked_turn_left()
        turn_right()
        sweep()
        turn_left()
        move_if_blocked_turn_left()
        turn_left()
        sweep()
        turn_right()
        move_if_blocked_turn_left()
        turn_right()
        sweep()
        turn_left()
        move_if_blocked_turn_left()
        turn_left()
        sweep()
        turn_left()
        turn_left()
        sweep()
        turn_left()
        move_if_blocked_turn_left()
        turn_left()
        sweep()
        turn_right()
        move_if_blocked_turn_left()
        turn_right()
        sweep()


def row():
    while front_is_clear():
        sweep()
        change_left()
        sweep()
        change_right()
        sweep()
        change_left()
        sweep()
        change_right()
        sweep()
        change_left()
        sweep()
        change_right()
        sweep()
        change_left()
        sweep()
        change_right()
        sweep()
        change_left()
        sweep()

def main():
    pick_beeper()
    test()

if __name__ == "__main__":
    run_karel_program("challenge-v-wall3")