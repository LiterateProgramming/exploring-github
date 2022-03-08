# The Descent - Austin W
# =======================
#
#
#
# This documentation helps solve "The Descent" on `codingame.com <https://www.codingame.com/ide/puzzle/the-descent>`_.
#
# By Austin Wesley
#
# The Problem
# ----------------
# .. image:: descent.jpg
#   :width: 100%
#
# Destroy the mountains before your starship collides with one of them. For that, shoot the highest mountain on your path.
# At the start of each game turn, you are given the height of the 8 mountains from left to right.
# By the end of the game turn, you must fire on the highest mountain by outputting its index (from 0 to 7).
#
# Firing on a mountain will only destroy part of it, reducing its height. Your ship descends after each pass.
#
# -----------------------------------------------------------------
#
# * The while loop represents the game.
# * Each iteration represents a turn of the game where you are given inputs
#   (the heights of the mountains)and where you have to print an output (the index of the mountain to fire on)
# * The inputs you are given are automatically updated according to your last actions.
#
#
#
#
# The  Game Loop
# __________________
# The solution method for this problem is for loop practice. The game loop takes whatever
# mountain index is printed and chooses it as the mountain to fire on.
#
# *This section of code sets up the game loop*
#
# **Game Loop**
import sys
import math
while True:
    max = 0
    maxIndex = -1
    for i in range(8):
        # We will use "mountain_h" as our variable for the height of a mountain
        mountain_h = int(input())
#
# Now we must write an action using print:
#
# The index of the mountain to fire on in the first test case is 4. To fire on this mountain we would use:
#
# .. code-block:: Python
#   :linenos:
#
#   print(4)
#
#
# This example solution takes the mountain height (mountain_h) as an input, and then prints the output mountain 4. This tells the program to fire on the mountain in index 4, regardless of the input height.
#
# ------------------------
# The "Brute Force" Method
# ------------------------
# Now that we know the basic rules for how the game works, we can start to solve it.
#
# The "brute force" method is to simply look at the mountain heights and output the one the ship needs to fire on. In the descending mountains test case seen in the photo, we can simply output the mountains in descending order as we need to fire on them:
#
# .. code-block:: Python
#   :linenos:
#
#   print("0")
#   print("1")
#   print("2")
#   print("3")
#   print("4")
#   print("5")
#   print("6")
#   print("7")
#
# This works for this particular test case. However, it fails all the other ones. We could write a seperate solution for each testcase, but that would take too long and defeat the purpose of the game.
#
# Instead, we need to use a for loop.
#
# The Loop Solution
# -----------------
# The actual solution to this problem is to have the computer fire on the highest mountain like in our previous solution, but also allow the computer to take over our job of deciding which mountain is the highest.
#
# --------------------------------------
#
# The code will take the mountain height given by the game as an input, and compare it to the current highest mountain height stored in our variable "mountain_h". It will then output (or "fire on") the highest mountain so that the ship is safe for that turn of the game. This is repeated for 8 turns until the ship is safe to land.
#
# **Game Loop**
        if mountain_h > max:
            max = mountain_h
            maxIndex = i
            
# This compares the height of the mountain to the current max and stores it as the new max. The index of the new highest mountain is recorded as "maxIndex"
#
# Finally, we output the index of the highest mountain as our target to fire on
    print(maxIndex)
#
#
# -------------------------------------
#
# Here is the code in its entirety so you can test it out yourself!
#
# .. code-block:: Python
#   :linenos:
#
#   import sys
#   import math
#   while True:
#        max = 0
#        maxIndex = -1
#        for i in range(8):
#            mountain_h = int(input())
#            if mountain_h > max:
#                max = mountain_h
#                maxIndex = i
#        print(maxIndex)
#
# *Python is sensitive to indent. It is important that the print statement does not fall inside the if statement but does fall inside the for loop*