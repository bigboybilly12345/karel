from stanfordkarel import move, turn_left, put_beeper, run_karel_program

def main():
    pass
    sweep()
    turn_left()
    sweep()
    turn_left()
if __name__ == "__main__":
    run_karel_program("wow")
def sweep():
    while front_is_clear():
        move()