# *************************************************
# Aaron Powell - Shadows of the Knight Ep. 1
# *************************************************
# This solves the `Shadows of the Knight Ep.1 puzzle <https://www.codingame.com/training/medium/shadows-of-the-knight-episode-1>`_.
#
# Problem
# ===========
# From the `Shadows of the Knight Ep.1 puzzle <https://www.codingame.com/training/medium/shadows-of-the-knight-episode-1>`_, the problem statement is below:
#
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
#  
# Solution Method
# ===============
# The following section demonstrate the solution used to solve the Shadows of the Knight Ep.1 Problem
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
# As depictied in the image above, using binary search can help window the target bomb for Batman. If one were to use the min and max boundaries in the width and height axis as a guide to either increment or decrement (on each axis respectfully) depending on the provided input direction of the relative bomb location, the bomb could be find in O(log(n)) time instead of iterating through each position in the respected axis. In order for Batman to find the bomb without going past the target area, it is necessary to have a small step size during the binary search algorithm. As a result, the algorithm should only update ``max_h/w`` and ``min_h/w`` by 1 depending on the relative direction of the bomb to batman.
#
#
# Code
# -----
# Provided Code:
import sys
import math
# To begin the game, the width, height, and number of turns before the game is over must be read in from the user (as shown below).
# 
# ``w``: width of the board game Batman can access
#
# ``h``: height of the board game Batman can access
w, h = [int(i) for i in input().split()]
# ``n``: maximum number of turns before game over.
n = int(input())  
x0, y0 = [int(i) for i in input().split()]
#
# * ``x0``: x axis position
# * ``y0``: y axis position
# * ``w``: width of the building
# * ``h``: height of the building
#
# Below are 4 list mappings with the directions in them: upwards,
# downwards, left, and right
upwards = ['U', 'UR', 'UL']
downwards = ['D', 'DR', 'DL']
left = ['L', 'UL', 'DL']
right = ['R', 'UR', 'DR']
# In order to keep track of the boundaries of the binary search algorithm, the minimum width ``min_w`` and minimum height ``min_h`` are set to 0. The maximum width ``max_w`` and maximum height ``max_h`` are intialized to the given input length minus 1 (zero based)
min_w = 0
max_w = w - 1
min_h = 0
max_h = h - 1
# =========
# Game loop
# =========
while True:
    # ``bomb_dir``: the direction of the bombs from batman's current location (U, UR, R, DR, D, DL, L or UL)
    bomb_dir = input()  
    #
    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)
    #
    # Variables
    #
    # * ``min_w`` - minimum width index 
    # * ``min_h`` - minimum height index
    # * ``max_w`` - maximum width index
    # * ``max_h`` - maximum height index
    # * ``x0`` - X axis position
    # * ``y0`` - Y axis position
    #
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
