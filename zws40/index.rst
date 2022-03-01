Solving *Marslander and The Descent* on codingame.com
============================================

.. toctree::
    :maxdepth: 2

    Intro_to_CodeChat.c
    TheDescentReview.py


Thinking Before Coding
----------------------
The number simply needs to be the closest to zero, meaning the absolute value function, abs(), will be of great use

By testing to see if the newly scanned integer is closer than the current closest to zero integer, we test if the new numbers absolute value is less than the current closest to zero number

For example, if 28 was the current closest to zero integer, and -14 was the most recent


Implementing Ideas
-----------------------
The first if statement is used as a "first time through" statement, letting us set a base value of the closest to zero integer

The second if statement is the main conditional statement of the code. This lets us see which integer is closer by comparing absolute values

After-Thoughts
---------------------

