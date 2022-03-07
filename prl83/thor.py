# **************************************
# Peter Loux - Power of Thor - Episode 1
# **************************************
# -------------
# Introduction
# -------------
# This documentation will walk you through developing a Python 3 solution to the `Power of Thor - Episode 1 puzzle <https://www.codingame.com/ide/puzzle/power-of-thor-episode-1>`_.
#
# ------------------
# Procedure and Tips
# ------------------
# So what do I have to do?
# ====================================
# .. image:: thor_1.png
#   :width: 100%
#
# The little man is Thor. The red lightning is the "light of power". You have to make Thor walk to the light of power.
#
# Sounds easy enough, but what about all that gibberish in the solution window?
# =======================================================================================
# .. image:: starter_code.png
#   :width: 100%
#
# The first two lines import libraries that you need:
import sys
import math
# These are the given variables:
#
#   :light_x: the X position of the light of power
#   :light_y: the Y position of the light of power
#   :initial_tx: Thor's starting X position
#   :initial_ty: Thor's starting Y position
#
# These variables never change. **You will need to make two new variables for Thor's current position.** Give them *meaningful* names, like ``thor_x`` and ``thor_y``.
#
# The next line of code uses the ``split()`` method to parse input from the game. You can read more about ``split`` `here <https://www.tutorialspoint.com/python3/string_split.htm>`_. Basically, the game starts you with a string like "3 8 3 6" and this line takes that string and sets the light position variables to (3,8) and Thor's initial position to (3,6):
light_x, light_y, initial_tx, initial_ty = [int(i) for i in input().split()]
# Then there's an infinite while loop. Whatever you want Thor to do each turn, you put it in the loop. But remember, you need to keep track of Thor's *current* position:
thor_x = initial_tx
thor_y = initial_ty
# Main loop
# ---------
while True:
#     This line keeps track of how many turns you have left:
    remaining_turns = int(input())
#     The starter code also tells you how to add debug messages:
#     ``print("Debug messages...", file=sys.stderr, flush=True)``
#
# How do I make Thor walk?
# ========================
# With ``print()`` statements. There are eight valid directions: "N", "NE", "E", "SE", "S", "SW", "W", and "NW". So ``print("N")``, will make Thor take one step "up".
#
# .. image:: directions.png
#   :width: 80%
#
# How do I make him go towards the light?
# =======================================
#
# Thor moves on a map which is 40 wide by 18 high. Note that the coordinates (X and Y) start at the top left! This means the most top left cell has the coordinates "X=0,Y=0" and the most bottom right one has the coordinates "X=39,Y=17".
#
# .. image:: moving.png
#   :width: 100%
#
# See, if Thor is at (3,6), and the light is at (3,8), you want to go south. So you ``print("S")`` and he takes one step south, and is now at (3,7). You don't have to do anything when you get to the light; you automatically win.
#
# Then what?
# ==========
#
# Each turn, compare Thor's *current* position to the light's position. Figure out which direction he needs to go and ``print`` it. Then don't forget to update ``thor_x`` and ``thor_y`` to reflect where you moved him.
#
# Let's goooo!!
# =============
#
# You should take a minute or two to plan it out. I drew this little sketch to help me:
#
# .. image:: sketch.png
#   :width: 100%
#
# #. I drew a map of the game grid and labeled the corners
# #. I put Thor at (20, 10), near the center of the map.
# #. Then for each of the eight possible directions, I wrote out some hypothetical coordinates. E.g. if the light was directly to the east, then its x-coordinate would be higher than Thor's, but the y-coordinate would be the same, for example (25, 10)
# #. I then wrote out the checks needed for each direction. E.g. if ``thor_x`` ("tx" in the sketch) is ``< light_x``, then he needs to go east
# #. Finally, I figured out how Thor's position would need to update after he'd moved in that direction. For east, it would be ``thor_x += 1``
#
# Can you do the first one for me?
# ================================
#
# Sure, if the light is to the north east then we move Thor and update his position like this:
    if thor_x < light_x and thor_y > light_y:
        print ("NE")
        thor_x += 1
        thor_y -= 1
#
# What if I want him to move a different direction besides NE?
# ==================================================================
#
# You could use an ``elif`` which is Python for "else if". Here, I did another one for you:
    elif  thor_x < light_x and thor_y < light_y:
        print ("SE")
        thor_x += 1
        thor_y += 1
#
# Why don't I just move him one of the four cardinal directions each turn?
# ============================================================================================
#
# That *would* be less typing, but when I did it, I ran out of moves. You can try it if you want.
#
# How do I screw it up?
# =====================
#
# If you move in the wrong direction, you'll go off the map and lose. You'll also lose if Thor sits there too long.
#
# Is there another way to solve it?
# =================================
#
# Yes, in Python, you can append to strings with the ``+`` operator. So make a variable called ``thor_move``, and set it to an empty string each turn. If he needs to go north, append "N" to it. If he also needs to move east, append "E" to it. Then at the end of the turn, just ``print(thor_move)``
#
# -------------
# Solution
# -------------
#
# I give up, just tell me the answer!
# ===================================
# Fine, if you want to cheat and not learn anything, just copy and paste this *entire* document into the solution window and it will pass all the tests.
#
    elif thor_x > light_x and thor_y < light_y:
        print ("SW")
        thor_x -= 1
        thor_y += 1

    elif thor_x > light_x and thor_y > light_y:
        print ("NW")
        thor_x -= 1
        thor_y -= 1

    elif thor_y > light_y:
        print ("N")
        thor_y -= 1

    elif thor_x < light_x:
        print ("E")
        thor_x += 1

    elif thor_y < light_y:
        print ("S")
        thor_y += 1

    elif thor_x > light_x:
        print("W")
        thor_x -= 1