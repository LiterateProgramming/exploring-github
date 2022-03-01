/* 
*********************
Shadows of the Knight
*********************

This solves the `shadows of the knight <https://www.codingame.com/ide/puzzle shadows-of-the-knight-episode-1>`_ codeingame problem. 

See my `notes`...

Problem Solution
================
.. image:: Shadow_of_knight.png
    :width: 75%


This problem requires the user to code a process to get batman to a bomb in a building. The building is represented as a 2D array, with position (0,0) being in the top left, and position (w,h) being in the bottom right. In the example picture above batman is in the bottom left quadrant of the building and the bomb is the red circle in the top right of the bulding.

The output that we give the game is the next location that we would like to move. For
example, in the picture above the bomb is far up and to the right, so the next location 
we would want to choose would be to a location like (10,2). 
*/

/*
Code 
====
The following will be the source code for the solution, along with some explanation and reasoning behind the solution process.
*/

// Includes
// --------
#include <iostream>
#include <string>
#include <vector>`
#include <algorithm>

using namespace std;


// Provided Code
// -------------
// The provided code for the game, these functions and variables have been set up to hand the user the required information from the game to be able to create the solution.
int main()
{
    int w; // width of the building.
    int h; // height of the building.
    cin >> w >> h; cin.ignore();
    int n; // maximum number of turns before game over.
    cin >> n; cin.ignore();
    int x0;
    int y0;
    cin >> x0 >> y0; cin.ignore();

    
// My Code
// -------
    // The location of batman, also initx and intiy, which I used initially 
    int initx, inity, cur_batx, cur_baty, count;
    // Variable Definitions for the limits from the top, bottom, left, and right
    int upr_lim, lwr_lim, lft_lim, rgt_lim;
    // My final solution used what I called limits. The basic idea is that if the bomb is insome direction from batman, we should not go in the opposite direction. This only becomes an issue in later stages where overshooting is likely.
    // 
    // I also have a count variable, this lets me set a specific place to go to on my first turn,This helps with one of the levels that does not work well with my chosen method.
    count = 0;
    upr_lim = 0;
    lwr_lim = h;
    lft_lim = 0;
    rgt_lim = w;

    // These are the variables that I send to the output to pick batman's next location.
    int batx = x0;    // Selects the middle square to start from
    int baty = y0;
    // 
    // ---------
    // Game Loop
    // ---------
    // The input that the game gives the player is the general direction of the bomb. These directions are listed in the code, we'll use this to find the bomb.

    while (1) {
        // The direction of the bombs from batman's current location (U, UR, R, DR, D, DL, L or UL), and the input argument from the website
        string bomb_dir; 
        cin >> bomb_dir; cin.ignore();

        cur_batx = batx;
        cur_baty = baty;
        
        // This "if block" should only run if the game is in the **first** round. This is for the second to last level because without it the program will fail, however even with this the program will pass on all other levels
        if (count == 0){
            batx = 3;
            // One of the levels is a single wide tower, so a x location of 0 **must** be given to pass that stage.
            if(w < 3){
                batx = 0;
            }
            baty = 3;
            count++;
        }

        // For each of these if, else if statements the direction is checked and the limit for the opposite direction is set. This is so that Batman doesn't accidentally go backwards in future rounds.
        if (bomb_dir == "U"){
            lwr_lim = cur_baty;

            batx = batx;
            if(baty == 1){
                baty = 0;
            }
            else{
                baty -= (baty - upr_lim)/2;
            }
        }
        else if(bomb_dir == "UR"){
            lft_lim = cur_batx;
            lwr_lim = cur_baty;

            batx += (rgt_lim - batx)/2;

            if(baty == 1){
                baty = 0;
            }
            else{
                baty -= (baty - upr_lim)/2;
            }
        }
        else if (bomb_dir == "R"){
            lft_lim = cur_batx;

            batx += (rgt_lim - batx)/2;
            baty = baty;
        }
        else if (bomb_dir == "DR"){
            lft_lim = cur_batx;
            upr_lim = cur_baty;

            batx += (rgt_lim - batx)/2;
            baty += (lwr_lim - baty)/2;
        }
        else if (bomb_dir == "D"){
            upr_lim = cur_baty;

            batx = batx;
            baty += (lwr_lim - baty)/2;
        }
        else if (bomb_dir == "DL"){
            rgt_lim = cur_batx;
            upr_lim = cur_baty;

            if(batx == 1){
                batx = 0;
            }
            else{
                batx -= (batx - lft_lim)/2;
            }
            
            baty += (lwr_lim - baty)/2;
        }
        else if (bomb_dir == "L"){
            rgt_lim = cur_batx;

            if(batx == 1){
                batx = 0;
            }
            else{
                batx -= (batx - lft_lim)/2;
            }
        
            baty = baty;
        }
        else if (bomb_dir == "UL"){
            rgt_lim = cur_batx;
            lwr_lim = cur_baty;

            if(batx == 1){
                batx = 0;
            }
            else{
                batx -= (batx - lft_lim)/2;
            }

            if(baty == 1){
                baty = 0;
            }
            else{
                baty -= (baty - upr_lim)/2;
            }
        }

        //Write an action using cout. DON'T FORGET THE "<< endl"
        //
        To debug: cerr << "Debug messages..." << endl;


        //the location of the next window Batman should jump to.
        cout << batx << " " << baty << endl;
    }
}