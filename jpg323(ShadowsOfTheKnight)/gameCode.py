# ********************************************
# Shadows of the Night - Ep1 | by JP Gathings
# ********************************************
#
# The purpose of this program is to solve the puzzle: `SHADOWS OF THE KNIGHT - EPISODE 1 <https://www.codingame.com/training/medium/shadows-of-the-knight-episode-1>`_,
# from the educational website `codingames.com <https://www.codingame.com/home>`_.
#
# In the game there is a grid of windows for an apartment building and one of those windows has a bomb in it. The game ends when the user arrives at the bomb. The user can jump to any window in the grid by changing their x and y coordinates, but are only given the direction in which the bomb is in relation to their current position.
#
# Goal
# ====
# The objective of the game is to get to the bomb in as few jumps as possible.
#
# You are given the size of the grid, the starting location and direction of the bomb. The number of jumps you are allowed to make is limited and the game will provide the direction in which the target is.
#
#
# Inputs
# ======
# Below are variables given by the game and are different for various test cases.
#
#   * **w**: width of the building. Provided only once. (int)
#   * **h**: height of the building. Provided only once. (int)
#   * **n**: maximum number of turns the user has to make it to the bomb. Provided only once. (int)
#   * **bomb_dir**: The direction of the bombs from batman's current location (U, UR, R, DR, D, DL, L or UL). Provided each round. The letters stand for Up, Down, Left, and Right. However, here it is just initialized as "AB" for organization. (string)
# 
import sys
import math
w, h = [int(i) for i in input().split()]
n = int(input())  # maximum number of turns before game over.
x0, y0 = [int(i) for i in input().split()]
bomb_dir = "AB"

# Approach
# ========
# The approach we are taking is based on a binary search tree. We will check what *directions* are in the **bomb_dir** string and write if-statements for each case.
#
# The steps are as follows:
#
# * Check the direction in which we are jumping.
# * Increase/decrease the lowest or highest possible value for each direction.
# * Use the lows and highs to calculate the new coordinates we are jumping to.
# * Jump
# * Repeat
#
# We start by getting the highest possible value at which the bomb can be vertically and horizontally. Since the grid starts at 0 we get this bottom right coordinate by subtracting 1 from the max width and height.
# 
high_x = w-1
low_x = 0

high_y = h-1
low_y=0
# We will repeat the following steps until the game forcibly exits for us. That happens when the player is in the same location as the bomb.
while True:
    bomb_dir = input()
    # the direction of the bombs from batman's current location (U, UR, R, DR, D, DL, L or UL)
    # |
    # 
    # Here we check if the bomb is located down or up from the player. If it is Up, the highest possible value for y will decrease since the y values increase downwards. Similarly, if the bomb is Down, the lowest y value increases.
    if "D" in bomb_dir:
        low_y = y0+1
    elif "U" in bomb_dir:
        high_y = y0-1
    # To calculate the new y value, we go to the middle of the remaining possible cells. We find the middle by dividing the difference by 2 and increasing that value by the minimum possible value to shift the value to the remaining possible cells.
	#
    y0 = low_y + (high_y-low_y) // 2
#
# .. image:: img1.png
#   :width: 30 %
#
    # For the scenario above, the max is 10. That means our highest y is 9 and our low y is 0. We know the bomb is Up and to the Right and our current position is (5, 2). Since it is Up, we change our highest possible y value to the current y value minus 1. That means the bomb's y value is somewhere between y=0 and y=4 as seen by the blue. Our next y position is calculated by 0+(4-0) / 2 = 2. Meaning our next jump will be to y=2.
    # **HORZONTAL**
    if "L" in bomb_dir:
        high_x = x0-1
    elif "R" in bomb_dir:
        low_x = x0+1
    x0 = low_x + (high_x-low_x) // 2
    # We follow the same process for the x values and eventually we will end up at the bomb.
    ## Handling 0s
    print("x0, y0:", file=sys.stderr, flush=True) # flushing the buffer prevents this output from counting as an attempt to "jump"
    print(x0, y0, file=sys.stderr, flush=True)
    # This is how the game tells us to make our jump to coordinates the x0 and y0 we just calculated.
    print(x0, y0)