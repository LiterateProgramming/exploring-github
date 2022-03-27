# *******************************
# Gaming Solutions- By Star
# *******************************
#
# Power of Thor - Episode 1
# ===============================
# Welcome everyone to my page. My name is Star and I will be walking through the game called Power of Thor. If you would like to see this game for yourself, `Power of Thor-Episode 1 <https://www.codingame.com/training/easy/power-of-thor-episode-1>`_. The goal of this game is getting Thor to his energy source, a spot where lighting will hit. 
#
# .. image:: Power_of_thor_pic_1.png
#
#
# As you can see in the picture above, this game uses the xy plane, compass directions, and has boundries. It is key to notice how the xy plane is set up. the right is positive x and down is positive y. The red dotted square in the picutre above are the boundaries. The top left corner is our orgin. 
# Now to get Thor to his lighting source we have to know Thor's starting location and the location of the lighting. For example, Thor's starting location is (1,1) and the light is located at (1,5). This means Thor needs to move South to get to the light. 
# 
#
# .. contents:: Table of Contents
#   :depth: 2
# 
# |
# |
#
# Provided Code
# ------------------
# This game has a built in code for the directions that you can't see. After trail and error, I figured out that all it is doing is either increasing/decreasing x and/or y. It is **not** updating Thor's position. Which can cause him to go outside of the boundry. When you go outside the boundry it is game over. 
#
# 
from re import X
import sys
import math

# *Auto- generated code below aims to helping you parse the standard input according to the problem statement. Hint: you can use the debug stream to print initialTX and initialTY, if Thor seems not to follow your instructions.*
 # **Light_x**: the X position of the light of power
 #
 # **Light_y**: the Y position of the light of power 
 #
 # **Initial_tx**: Thor's starting X position
 #
 # **Initial_ty**: Thor's starting Y position
 #
light_x, light_y, initial_tx, initial_ty = [int(i) for i in input().split()]

# game loop
while True:
    remaining_turns = int(input())  # The remaining amount of turns Thor can move. Do not remove this line.

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)


    # A single line providing the move to be made: N NE E SE S SW W or NW
    print("SE")

#   
# Solution
# --------------------
# My solution code is in C++. Please click `here <https://www.softwaretestinghelp.com/loops-in-cpp/#:~:text=Loops%20In%20C%2B%2B%201%20For%20Loop.%20The%20construct,...%205%20Infinite%20Loop.%20...%206%20Conclusion.%20>`_ if you are not familiar with it. 
#
# First Try
# ^^^^^^^^^^^^^^^^^
# First off, taking a *step back* and drawing out the xy plane and the directions the are required was helpful. 
# 
#  .. image:: Power_of_thor_pic_2.png
#  
# However, without the original code telling me exactly what the directions did, I had no idea of knowing that the initial Thor position never changed. Keeping notes helped me track how past codes I wrote worked and didn’t work. Taking notes was helpful then just trying to type in code without much guidance. It will take me a while to look and gather before trying code. 
# I started with trying to figure out Thor's position in comparison to light's position but did it have in common with directions.
#
# .. image:: Power_of_thor_pic_4.png
#
# I started with a while loop but noticed it only worked for a straight line movement. Next i tried if loops. That just got messy. Last i tried a for loop, and incorprated Thor's position getting updated. 
#
# .. image:: Power_of_thor_pic_5.png
# .. image:: Power_of_thor_pic_6.png
#
# Errors in My Code
# ^^^^^^^^^^^^^^^^^
# Due to all the if statements I had and built in while loops with only work 75% of the time. When I have time I may go back and clean up this code to a similar form and able to work 100% of the time. 

