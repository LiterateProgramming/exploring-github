// *******************
// **Power of Thor**
// *******************
/*
Use `this link <https://www.codingame.com/ide/puzzle/power-of-thor-episode-1>`_ to access the coding game.


General Instructions
--------------------

**Objective**

Write a program that will guide Thor to reach the light of power in the most efficient manner.

**Game Rules**

Thor will move on this map that has the coordinates of 40 wide by 18 high. As the light of power changes locations your goal is change the direction of Thor's movements based on the coordinate placement of the light of power.


*Note: You can utilize any coding language that you are most comfortable with to write this code by changing this option in the code tab. I chose to use C++*

*/

#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;
/*
Provided Code
--------------
*/
/* These are the functions and variables that are also provided to the developer when you begin the coding game.
*/
int main() 
// beginning bracket
{
    // the X coordinate position of the light of power
    int light_x;
    // the Y coordinate position of the light of power
    int light_y; 
    // Thor's starting position at X
    int initial_tx; 
    // Thor's starting position at Y
    int initial_ty;
    // The cin.ignore() function is used to ignore characters that may not belong in your input buffer
    cin >> light_x >> light_y >> initial_tx >> initial_ty; cin.ignore();

/* This while statement is the beginning of the beginning of the game loop and it allows causes all of your test cases to run
*/
    while (1) {
        
        int remaining_turns; 
        // This is the remaining amount of turns Thor can move. Do not remove this line.
        cin >> remaining_turns; cin.ignore();

/*
Diagram
---------

.. image:: ThorPwr.jpg


*/
/* **This a diagram of Thor at his starting postion. The red arrows are pointing at the XY plane and the compass below so that you can have a clear orientation of Thor as he moves within the boundary conditions.** 

Variables
----------
The directions below are the variables used to output the direction in which you want Thor to go at the end of each game turn.Each movement makes Thor move by 1 cell the direction chosen

*       N (North) 
*       NE (North East) 
*       E (East)
*       SE (South East) 
*       S (South)
*       SW (South West) 
*       W (West)
*       NW (North West)
*/
/* 
Thor's Movement
----------------
*/

        /* In this case the light of power at the X and Y coordinates are greater than Thor's initial condition so 2 if condition statements have to be implemented. Thor's initial X and Y conditions must be incremented so he can move in a diagonal direction without going out of bounds or repositioning from the light of power.
        */
        if ((light_y > initial_ty) && (light_x > initial_tx))
        {
            cout << "SE" << endl;
            initial_tx++;
            initial_ty++;
            }
        /* Based on the compass it can be determined that Thor will travel E (East).The light_x is the position of the light of power  and initial_tx is Thor's starting position in the X-coordinate plane. The postion of the light of power is is going in the positive direction and it greater than Thor's starting postion so a condition statement is created that if this is the case travel East.
        */
        else if (light_x > initial_tx) {
            cout << "E" << endl;
            }
        /* Thor will travel N (North) since the light of power is above his location and it is in the positive direction .The light_y is the position of the light of power and initial_ty is Thor's starting position in the Y-coordinate plane.
        */
        else if (light_y < initial_ty) {
            cout << "N" << endl;
            }
        /* In this instance the light of power is in the negative Y direction of Thor's position. It is also at an angle which means Thor must move in an diagonal direction so that he does not run out of energy. He will travel diagional because of the increment then straight.
        */
        else if (light_y > initial_ty) {
            cout << "SW" << endl;
            initial_ty++;
            // *Positive increment here so that Thor does not run out of bounds.*
            }
        // This else if statement is so that Thor will travel West after incrementing to the point where the light of power is equal to Thor's initial position.
        else if (light_x < initial_tx) {
            cout << "W" << endl;

            } 
    }


