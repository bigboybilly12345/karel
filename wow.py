from stanfordkarel import move, turn_left, put_beeper, run_karel_program

def main():
    pass
    pick_beeper()
    row_2()


if __name__ == "__main__":
    run_karel_program("challenge-v-wall3")







def sweep():
    while front_is_clear():
        move()
        if beepers_present():
            pick_beeper()

def change_left():
    turn_left()
    move()
    turn_left()
    if beepers_present():
        pick_beeper()

def change_right():
    turn_right()
    move()
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
        move()
        turn_right()
        sweep()
        turn_left()
        move()
        turn_left()
        sweep()
        turn_left()
        turn_left()
        sweep()
        turn_left()
        move()
        turn_left()
        sweep()
        turn_right()
        move()
        turn_right()
        sweep()
        turn_left()
        move()
        turn_left()
        sweep()
        turn_right()
        move()
        turn_right()
        sweep()
        turn_left()
        move()
        turn_left()
        sweep()
        turn_left()
        turn_left()
        sweep()
        turn_left()
        move()
        turn_left()
        sweep()
        turn_right()
        move()
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
