# Liv S.: Power of Thor - Episode 1
# =================================
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
# For my first try though this game I used C++. By the end I only got a 75% accuracy for the code once it was submitted. C++ is the langauge my degree has given me; however, since my teacher writes mostly in python, I decided to use python. `Python <https://wiki.python.org/moin/BeginnersGuide>`_.
#
    # Thinking It Through
    # ^^^^^^^^^^^^^^^^^^^^^^^^^^
        # First off, taking a *step back* and drawing out the xy plane and the directions the are required was helpful. If during the first round I used the correct directions for the xy plane. But with it mapped out similar to this I was eventually able to figure it out.
        #
        #  .. image:: Power_of_thor_pic_2.png
        #
        # However, without the original code telling me exactly what the directions did, I had no idea of knowing that the initial Thor position never changed. Keeping notes helped me track how past codes I wrote worked and didn’t work. Taking notes was helpful then just trying to type in code without much guidance. It will take me a while to look and gather before trying code.
        # I started with trying to figure out Thor's position in comparison to light's position but did it have in common with directions.
        #

# game loop- From here
while True:
    remaining_turns = int(input())  # The remaining amount of turns Thor can move. Do not remove this line.

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)

    #
    #| The above code gets the program to show us where Thor and the light start.
    #
# to here was all from the game. The next part was written by myself.

    if initial_tx == light_x:  # if we are already on the correct x position
        while initial_ty > light_y:
        # then check to see if thor is further down the y axis, if so then keep north
        # until Light y and Thor's y are equal
            print("N")
            initial_ty -= 1
        while initial_ty < light_y:
            # then check to see if thor is further up the y axis, if so then keep south
            # until Light y and Thor's y are equal
            print ("S")
            initial_ty += 1

    elif initial_ty == light_y:
        while initial_tx > light_x:
        # then check to see if thor is further down the x axis, if so then keep north
        # until Light y and Thor's y are equal
            print("W")
            initial_tx -= 1
        while initial_tx < light_x:
            # then check to see if thor is further up the x axis, if so then keep south
            # until Light y and Thor's y are equal
            print ("E")
            initial_tx += 1

# This code worked for the following test cases:
#   * Straight line
#   * Up
#
# However the game play had,
#
#       WARNING: your code did not read all available input before printing an instruction, your outputs will not be synchronized with the game's turnns and unexpected behavior may occur.
#
# This is probably because I played the testcases seprately instead of all together.
#
# That code was only when Thor's x or y was equal to Light's x or y respectfully. Now what if Neither of Thor's x or y is equal to Light's x or y respectfully? In this case we will have to look into either using NW, NE, SW, SE, or having thor move along the x axis then the y axis.

    if initial_tx > light_x:
        # remember when Thor x > light x then Thor needs to go W.
        while initial_ty > light_y:
            # This mean Thor needs to go N.
            # so together thor needs to go NW
            print ("NW")
            initial_tx -= 1
            initial_ty -= 1
        while initial_ty < light_y:
            # this means Thor needs to go S.
            # so the if statement plus this while loop means Thor needs to go SW
            print ("SW")
            initial_tx -= 1 # this will minus one from Thor's initial_tx so it updates as he walks/floats
            initial_ty += 1 # this will add one to Thor's initial_ty so it updates as he walks/floats

    elif initial_tx < light_x:
        # remember when Thor x > light x then Thor needs to go E.
        while initial_ty > light_y:
            # This mean Thor needs to go N.
            # so together thor needs to go NE
            print ("NE")
            initial_tx += 1
            initial_ty -= 1
        while initial_ty < light_y:
            # this means Thor needs to go S.
            # so the if statement plus this while loop means Thor needs to go SE
            print ("SE")
            initial_tx += 1 # this will add one to Thor's initial_tx so it updates as he walks/floats
            initial_ty += 1 # this will add one to Thor's initial_ty so it updates as he walks/floats

# After this part was added to the code, I pressed play all testcases and passed the following:
#   * Straight line
#   * Up
#   * Easy Angle
#   * Optimal Angle
#
# However the game play still had,
#
#       WARNING: your code did not read all available input before printing an instruction, your outputs will not be synchronized with the game's turnns and unexpected behavior may occur.
#
# End Result
# ^^^^^^^^^^^^^^^
# Durning the second try using Python, I was able to get a 100% on the code.
