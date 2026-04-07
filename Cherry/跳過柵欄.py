"""
File: Steeplechase.py
Name: CHERRY:
---------------------------------
"""

from karel.stanfordkarel import *


def main():
    """
    Karel crosses hurdles in a 12x12 world
    with a for loop 
    """
    for i in range(11):
        if front_is_clear():
            move()
        else:
            jump()

def jump():
    up()
    down()

def turn_right():
    for i in range(3):
        turn_left()

def up():
    while not front_is_clear():
        # east
        turn_left()
        move()
        # north
        turn_right()
        # east

def down():
    move()
    # east
    turn_right()
    # south
    while front_is_clear():
        move()
    turn_left()
    # east


# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
