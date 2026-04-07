"""
File: PotholeFilling.py
Name: Cherry:
--------------------------
This program demonstrates how Karel fills multiple potholes
by using decomposition.

In this program, we will guide Karel to fix three potholes
on the road. Instead of writing all the commands in one place,
we will practice breaking a big task into smaller, reusable
functions to make the program clearer and easier to manage.
"""

from karel.stanfordkarel import *


def turn_right():
    for i in range(3):
        turn_left()

def turn_leftt():
    for i in range(2):
        turn_left()


def put_beeperrrrrrrrr():
    for i in range(99):
        put_beeper()

def go_go_karel():
    for i in range(2):
        turn_right()
        move()
        put_beeperrrrrrrrr()
        turn_leftt()
        move()
        turn_right()
        move()
        move()

def main():
    move()
    go_go_karel()
    turn_right()
    move()
    put_beeperrrrrrrrr()
    turn_leftt()
    move()
    turn_right()
    move()
    turn_left()

    """
    cherry:
    """
    pass


# ----- DO NOT EDIT CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
