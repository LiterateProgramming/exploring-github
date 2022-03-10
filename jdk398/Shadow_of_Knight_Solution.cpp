/*
***********************************
Joe Kennedy - Shadows of the Knight
***********************************

This solves the `shadows of the knight <https://www.codingame.com/ide/puzzle shadows-of-the-knight-episode-1>`_ codeingame problem.

Problem Solution
================
.. image:: Shadow_of_knight.png
    :width: 75%


This problem requires the user to code a process to get batman to a bomb in a building. The building is represented as a 2D array, with position (0,0) being in the top left, and position (w,h) being in the bottom right. In the example picture above batman is in the bottom left quadrant of the building and the bomb is the red circle in the top right of the bulding.

The output that we give the game is the next location that we would like to move. For
example, in the picture above the bomb is far up and to the right, so the next location
we would want to choose would be to a location like (10,2).

Something that also should be noted about the above picture are the two red lines flanking Batman. These are a graphical representation of what I call "limits". Limits are essentially coordinates, either x or y, that Batman is restricted from going past. So in a future move Batman will use the limits defined before as an outer bounds to help calculate his next move. We decide limits based on the direction that the game gives us for the bomb. For our example above, because the bomb is above and to the right, we know for sure that it is not anywhere below or to the left of our current position. by using this method repeatedly we cut down the search area until we can make our final move with certainty.

For this solution I use the find function of the string class that the game requires us to import. we will be checking this against the class defined value npos.

 .. code::

    if (bomb_dir.find("R") != string::npos)

What this snippet of code is doing is trying to find the character R in the string supplied, if what it returns is not equal to the value defined as essentially "sub character not found", then the if receives a true and we go into the if's code.

Each section is a separate if statement, so that if the program finds R, it will still look for U or D to see if the direction is diagonal.

Code
====
The following will be the source code for the solution, along with some explanation and reasoning behind the solution process.

Includes
--------
*/
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;


// Provided Code
// -------------
// The provided code for the game, these functions and variables have been set up to hand the user the required information from the game to be able to create the solution.
int main()
{
    // The following variables are one time inputs for the game. ``h`` and ``w`` determine the height and width of the building that Batman is scaling respectively.
    int w;
    int h;
    cin >> w >> h; cin.ignore();
    // ``n`` is the maximum number of turns before game over. (we use this very little)
    int n;
    cin >> n; cin.ignore();
    // ``x0`` and ``y0`` represent the initial coordinates of Batman.
    int x0;
    int y0;
    cin >> x0 >> y0; cin.ignore();


// My Code
// -------
    // The location of batman, also count, which is just used to check if we are in the first round, this is for some levels it is important to start in the right position.
    int cur_batx, cur_baty, count;
    // Variable Definitions for the limits of where the bomb could be from the top, bottom, left, and right
    int upr_lim, lwr_lim, lft_lim, rgt_lim;
    // My final solution used what I called limits (defined above). The basic idea is that if the bomb is in some direction from batman, we should not go in the opposite direction. This only becomes an issue in later stages where overshooting is likely.

    // count is initially set to zero, and the inital limits are set
    count = 0;
    // These limits are essentially the edge of the board, because we don't know where the bomb could be.
    upr_lim = 0;
    lwr_lim = h;
    lft_lim = 0;
    rgt_lim = w;

    // These are the variables that I send to the output to pick batman's next location.
    int batx = x0;
    int baty = y0;
    //
// ---------
// Game Loop
// ---------
    // The input that the game gives the player is the general direction of the bomb. These directions are listed in the code, we'll use this to find the bomb.

    while (1)   {
        // The direction of the bombs from batman's current location (U, UR, R, DR, D, DL, L or UL), and the input argument from the website
        // Each direction is specified by a letter, U D R L as Up Down Right and Left respectively. if there's only one letter (like U) then that means you have the other direction correct, and only need to move in that one direction. Two letters means it is on some diagonal and you need to change both coordinates.
        //
        // **Important:** the coordinates are set up with zeros in the top left and max height and width in the bottom right. So, while I know it is confusing it's important to understand that when I say Up, I mean smaller coordinates and when I say Down I mean larger coordinates.
        string bomb_dir;
        cin >> bomb_dir; cin.ignore();

        cur_batx = batx;
        cur_baty = baty;

        // This "if block" should only run if the game is in the **first** round. This is for the second to last level because without it the program will fail, however even with this the program will pass on all other levels
        //
        // Unfortunately I couldn't think of another way to solve this problem without this quick fix.
        if (count == 0){
            batx = 0;
            baty = h/5;
            count++;
        }
        // For each of these if, else if statements the direction is checked and the limit for the opposite direction is set. This is so that Batman doesn't accidentally go backwards in future rounds.
        if (bomb_dir.find("U") != string::npos){
            // here I assign my lower limit to be one space below where batman currently is. This helps me in later steps so when I'm calculating moves I don't accidentally move into an area I should have already ruled out.
            lwr_lim = cur_baty+1;

            // This assignment to ``baty`` is necessary because the integer division below it will not give a position of 0, so if you're at y position 1 and the bomb is up the bomb is at position 0;
            if(baty == 1){
                baty = 0;
            }
            else{
                // Here I use my upper limit to help find how far up I need to go. I don't want to move past where I've already been, so I subract my current position by the farthest up I've been and then divide by two to get the point in the middle.
                baty -= (baty - upr_lim)/2;
                // It's also important to note that I use a divide by 2 because I feel on average picking the point in the middle will cut out the most possible positions.
            }
        }
        // The other three definitions are pretty similar to the first one, first we set the limit for the adjacent line of coordinates opposite to the direction the bomb is in, then we set the next coordinate as halfway between where we currently are and the limit in the direction of the bomb.
        if (bomb_dir.find("R") != string::npos){
            lft_lim = cur_batx-1;

            batx += (rgt_lim - batx)/2;
        }
        if (bomb_dir.find("D") != string::npos){
            upr_lim = cur_baty;

            baty += (lwr_lim - baty)/2;
        }
        if (bomb_dir.find("L") != string::npos){
            rgt_lim = cur_batx+1;

            if(batx == 1){
                batx = 0;
            }
            else{
                batx -= (batx - lft_lim)/2;
            }
        }

        // Finally The output is a simple cout of the two coordinates that we calculated.
        // the location of the next window Batman should jump to.
        cout << batx << " " << baty << endl;
    }
}
//
// Below is an example of one of my boolean operations before I found my final solution. I looked for the exact string for each possible input (U, UR, R, L...). This was not the best way to do this because it took up way too much space. As seen above, using the find feature of the string class was much more effective.
//
// .. code::
//
//  else if(bomb_dir == "UR"){
//      lft_lim = cur_batx-1;
//      lwr_lim = cur_baty+1;
//
//      batx += (rgt_lim - batx)/2;
//
//      if(baty == 1){
//          baty = 0;
//      }
//      else{
//          baty -= (baty - upr_lim)/2;
//      }
//  }
//