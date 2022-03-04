# =========================================
# Power of Thor - Episode 1 - By Star
# =========================================
# Hello, my name is Star. Today I am going through my solution and thought process for `Power of Thor-Episode 1 <https://www.codingame.com/training/easy/power-of-thor-episode-1>`_. This game is about getting Thor to his energy source, a spot where lighting will hit. 
#
# .. image:: Power_of_thor_pic_1.png
#
#
# As you can see in the picture above, this game uses the xy plane, compass directions, and has boundries. For example, Thor's starting location is (1,1) and the light is located at (1,5). This means Thor needs to move South to get to the light. 
# 
#
                        # .. contents:: Table of Contents
                        #   :depth: 3
# 
# |
# |
# |
# |
# |
# |
# |
# |
# |
# |
# |
# |
# |
# |
# |
# |
#
# Provided Code
# ------------------
# This game has a built in code for the directions that you can't see. After trail and error, I figured out that all it is doing is either increasing/decreasing x and/or y. It is **not** updating Thor's position. Which can cause him to go outside of the boundry. 
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
# Solution: First Try with C++
# ------------------------------------
# My solution code is in C++. Please click `here <https://www.softwaretestinghelp.com/loops-in-cpp/#:~:text=Loops%20In%20C%2B%2B%201%20For%20Loop.%20The%20construct,...%205%20Infinite%20Loop.%20...%206%20Conclusion.%20>`_ if you are not familiar with it. 
#
# My Thoughts and Process
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
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
# 
# Looking Back
# ^^^^^^^^^^^^^^^^^
# Looking back, if I was going to do the game in C++, I really should have done the codechat in C++ also. I am learning Python now to make this a little easier on me so I don't have to switch back and forth. I would copy and paste the C++ code I used in the game; however, python doesn't care for C++ and keeps putting errors at the top. 
#
# Soultion: Second Try with Python
# ----------------------------------------
# With this second try, I am going to work in `Python <https://wiki.python.org/moin/BeginnersGuide>`_.
#
# My Thoughts and Process
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# The whole idea is to get Thor to a power source using the xy plane. So if Thor is at (0,3) and the light is at (1,3) then Thor needs to move to the right one. Since postive x is to the right (**East**) and postive y is down (**South**). Another given is that x is 0-40 and y is 0-18 and the coodinates start at the top left of the boundry. 
#
# However, as I found out this my first try, Thor's position isn't being tracked, just his intial position. This needs to taken into account. We already found out with try 1 that loops aren't the best way to complete this code. Maybe we can use math instead. 
#
#  Example: 
#
#   If Thor is at (0,0) and the light is at (40,0). We know just by looking at this that Thor is -40 from the light in the x direction. So to solve this we need to add 40 to Thor's intial position.
#
print(initial_tx, initial_ty, light_x, light_y)  
#
#| The above code gets the program to show us where Thor and the light start.
#
x_steps = [int]  # this is going to track our difference in Thor's x and Light's x.
y_steps = [int]  # this is going to track our difference in Thor's y and Light's y.

x_steps = initial_tx - light_x  # examples:  -40 = 0 - 40 (E); 40 = 40 - 0 (W)
y_steps = initial_ty - light_y  # examples:  -18 = 0 - 18 (S) ; 18 = 18 -0 (N)

if x_steps == 0:
    if y_steps > 0:
        print("N")
        y_steps -= 1
    if y_steps < 0:
        print ("S") 
        y_step += 1
elif y_steps == 0:
    if x_steps > 0:
        print("W")
        x_steps -= 1
    if x_steps < 0:
        print("E")
        x_steps += 1

# So I spent almost an hours tryin to get that version to work however it kept giving me a time out error. So instead of working with new varibles. Lets try working with the ones we already have.
#
# Let's try increment Thor's initial position with every move. 
#
# game loop
while True:
    remaining_turns = int(input())  # The remaining amount of turns Thor can move. Do not remove this line.

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)

    #
    #| The above code gets the program to show us where Thor and the light start.
    #

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