# ***************************
# Shadows of the Knight Ep. 1
# ***************************
# This solves the `Shadows of the Knight Ep.1 puzzle <https://www.codingame.com/training/medium/shadows-of-the-knight-episode-1>`_.
#
# Problem
# ===========
# You (Batman) will look for the hostages on a given building by jumping from one window to
# another using your grapnel gun. Your goal is to jump to the window where the hostages are
# located in order to disarm the bombs. Unfortunately, you have a limited number of jumps before
# the bombs go off…
# Before each jump, the heat-signature device will provide you with the direction of the bombs
# based on your current position: 
#
# * U(Up)
# * UR (Up Right)
# * R (Right)
# * DR (Down Right)
# * DL (Down Left)
# * L (Left)
# * UL (Up Left)
#
# Your mission is to program the device so that **it indicates the location of the next window you
# should jump to** in order to reach the bombs' room **as soon as possible**.
#
# Solution Method
# ===============
# The following section demonstrate the solution used to solve the Shadows of the Kinght Ep.1 Problem
#
# Background
# ----------
# The Shadows of the Knight Ep.1 problem can be onsidered as a two dimensional `binary search problem <https://www.geeksforgeeks.org/binary-search/>`_,
# with the width array being one binary search and the height array being another binary search. I
# chose to return the next spot for batman as the midpoint of the width and height indices. Below is a diagram of the problem solution
#
# .. image:: diagram.png
#  :width: 100%
# 
# 
# Code
# -----
# Provided Code:
import sys
import math
w, h = [int(i) for i in input().split()]
n = int(input())  # maximum number of turns before game over.
x0, y0 = [int(i) for i in input().split()]
#
# ``x0``: x axis position
# 
# ``y0``: y axis position
#
# ``w``: width of the building.
#
# ``h``: height of the building.
# 
# Below are 4 list mappings with the directions in them: upwards,
# downwards, left, and right
upwards = ['U', 'UR', 'UL']
downwards = ['D', 'DR', 'DL']
left = ['L', 'UL', 'DL']
right = ['R', 'UR', 'DR']
# In order to keep track of the boundries of the binary search algorithm, the minimum width ``min_w`` and minimum height ``min_h`` are set to 0. The maximum width ``max_w`` and maximum height ``max_h`` are intialized to the given input length minus 1 (zero based)
min_w = 0
max_w = w - 1
min_h = 0
max_h = h - 1
# game loop
while True:
    bomb_dir = input()  # the direction of the bombs from batman's current location (U, UR, R, DR, D, DL, L or UL)

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)
    #
    # Variables
    #  
    # * ``min_w``
    # * ``min_h``
    # * ``max_w``
    # * ``max_h``
    # * ``x0`` - X axis position
    # * ``y0`` - Y axis position
    if min_w <= max_w:
        if bomb_dir in right:
            min_w  = x0 + 1
        elif bomb_dir in left:
            max_w = x0 - 1
    if min_h <= max_h:
        if bomb_dir in upwards:
            max_h = y0 - 1
        elif bomb_dir in downwards:
            min_h = y0 + 1
    # Update position of *Batman*
    x0 = (max_w + min_w) // 2
    y0 = (max_h + min_h) // 2
    # Print out the location of the next window *Batman* should jump to.
    print("{} {}".format(x0,y0))
