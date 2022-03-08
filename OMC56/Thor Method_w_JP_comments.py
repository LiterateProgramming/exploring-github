# ************************
# Gaming Solutions
# ************************
#
# Power of Thor - Episode 1
# ============================
# Hello, my name is Star. Today I am going through my solution and thought process for `Power of Thor-Episode 1 <https://www.codingame.com/training/easy/power-of-thor-episode-1>`_. This game is about getting Thor to his energy source, a spot where lighting will hit. 
#
# .. image:: Power_of_thor_pic_1.png
#
#
# As you can see in the picture above, this game uses the xy plane, compass directions, and has boundries. For example, Thor's starting location is (1,1) and the light is located at (1,5). This means Thor needs to move South to get to the light. 
# 
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
# This game has a built in code for the directions that you can't see. After **trail** and error, I figured out that all it is doing is either increasing/decreasing x and/or y. It is **not** updating Thor's position. Which can cause him to go outside of the boundry. 
# 
# .. note::
# 
#   **trial**-mispelled
#
# .. image:: Power_of_thor_pic_3.png
#   
# Solution
# --------------------
# My solution code is in C++. Please click `here <https://www.softwaretestinghelp.com/loops-in-cpp/#:~:text=Loops%20In%20C%2B%2B%201%20For%20Loop.%20The%20construct,...%205%20Infinite%20Loop.%20...%206%20Conclusion.%20>`_ if you are not familiar with it. 
#
# .. note::
# 
#   This section either needs more text or could be turned into a simple note like this one.
#
# First Try
# ==========
# First off, taking a *step back* and drawing out the xy plane and the directions the are required was helpful. 
# 
# .. _imgNote1:
#
#  .. image:: Power_of_thor_pic_2.png
#  
#
# However, without the original code telling me exactly what the directions did, I had no idea of knowing that the initial Thor position never changed. Keeping notes helped me track how past codes I wrote worked and didn’t work. Taking notes was helpful then just trying to type in code without much guidance. It will take me a while to look and gather before trying code. 
# I started with trying to figure out Thor's position in comparison to light's position but did it have in common with directions.
#
# .. image:: Power_of_thor_pic_4.png
#
# I started with a while loop but noticed it only worked for a straight line movement. Next i tried if loops. That just got messy. Last i tried a for loop, and incorprated Thor's position getting updated. 
#
# 
# .. image:: Power_of_thor_pic_5.png
# .. image:: Power_of_thor_pic_6.png
#
# Errors in My Code
# =================
# Due to all the if statements I had and built in while loops with only work 75% of the time. When I have time I may go back and clean up this code to a similar form and able to work 100% of the time. 
#
# Code Review Summary
# -------------------
# The descriptions you provide make the game seem very simple and doable and outline the goal very well. However, once I got to :ref:`this image <imgNote1>`, I got very lost. 
#   It is a very busy photo and doesn't seem to have much explanation for what it is a picture of other than it helped you to draw out the axes. 
# 
# It took a lot of looking ahead to your C++ code to realize what any of the drawn out images were saying because they had more info than needed at that time. The description and pictures have all of the information about the game, but when you read it from the top, there are a lot of assumptions made about the user knowing keywords involved with the code.
