// *******************
// Power of Thor
// *******************
/*
Use this link to access the coding game

.. note::

    Provide a nicer link; for example: "Use `this link <https://www.codingame.com/ide/puzzle/power-of-thor-episode-1>`_ to access the coding game."

Instructions:
----------------------

**Write a program that will guide Thor to reach the light of power in the most efficient manner.**

.. note::

    Be specific. What is the light of power? How does Thor get to it? What does efficient meant?


*/
/*
*Note: You can utilize any coding language that you are most comfortable with to write this code by changing this option in the code tab. I chose to use C++*

.. note::

    Distinguish between text provided by the game and what your wrote. Perhaps:

            Note: You can utilize any coding language that you are most comfortable with to write this code by changing this option in the code tab.

        I chose to use C++.
*/

#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

/*
**This line of code will be given to you**
*/
int main()
{
    // .. note::
    //
    //  Put comment on the previous line, so they will be rendered nicely. Make this a heading such as "Inputs".
    int light_x; // the X position of the light of power
    int light_y; // the Y position of the light of power
    int initial_tx; // Thor's starting X position
    int initial_ty; // Thor's starting Y position
    cin >> light_x >> light_y >> initial_tx >> initial_ty; cin.ignore();

// **The game loop begins here**
    while (1) {
        // .. note::
        //
        //  Same here.
        int remaining_turns; // The remaining amount of turns Thor can move. Do not remove this line.
        cin >> remaining_turns; cin.ignore();
/*
This a diagram of Thor at his starting position

.. image:: ThorPwr.jpg

.. note::

    Explain what this images means. How does it help you explain the problem? How does it help you solve the problem?


**Discription/Directions: The red arrows are pointing at the XY plane and the compass below so that you can have a clear orientation of thor as he moves within the bondary conditions. Remember the objective is to get thor to move towards the light of power. The directions you will be using will be N(North), NE(North East), E(East), SE(South East), S(South), SW(South West), W (West), or NW(North West).**
*/
/*
.. note::

    Use a title/sub-title here::

        Test case 1 & 2
        ===============

**Test case 1 & 2:**

This line of code is where you will put in how Thor will move. In order to observe what direction he will go in based on what you are already given click on the "play testcase" button in the bottom right hand corner and watch the video as he moves. After this you will change the direction that thor moves "E" (East) towards the light of power and you passed the first test case. You will notice that as you play each testcase the orientation of thor changes, so you can repeat the same process in testcase 01 (straight line) in test case 02 (Up) but this time go N North in the direction of the light of power.
*/
/* **Test case 3:**

Easy angle is where things get a little tricky. In order to make Thor move toward the light of power, while also being mindful of his "Energy" located under the console output, you must how thor move SW (South West) and W (West) at the same time so you will need 2 else if statements. The reason you must increment is to prevent Thor from moving out of the boundary conditions before he reaches the light of power.

.. note::

    Explain this more -- one sentence has a phrase ("you must how thor move SW") I didn't understand. Why move SW and W? Why does this need 2 if statements?
*/
/* **Test case 4:**

The final test case (Optimal angle) utilizing everything implemented before while also assuring that the whole code is properly looped so that you can play all testcases. Here is where you apply the use of if and else if statements to get the last angle to be short but also keep you from running out of energy. In this case in order to achieve the angle you desire you must increment thor's inital X and Y position in the SE (South East) direction.

.. note::

    The term "optimal angle" suggests that you need to be computing an angle based on where Thor is and where the Light of Power is. Why is this not in the code?
*/
/*

Note: In order to loop each of the test cases to work all at the same time you have to use an if statement so that you can input more than one direction for each time that Thor moves. You will notice that as you play each testcase. Your conditions are created by making the light of power position X or Y (light_x/light_y) greater than or less than the positon of Thor(initial_tx/initial_ty) in the X or Y.

*/

        // **this is the fourth test case...**
        //
        // .. note::
        //
        //  Explain this. Why these comparsions? Why the selected direction? Why does this solve the problem? Add these comments to each case where you command Thor to move in a specific direction.
        if((light_y > initial_ty) && (light_x > initial_tx))

        {
            cout << "SE" << endl;
            initial_tx++;
            initial_ty++;
        }
        // **This is the first test case below...**
        else if(light_x > initial_tx) {
            cout << "E" << endl;
        }
        // **This is the second test case...**
        else if(light_y < initial_ty) {
            cout << "N" << endl;
        }
        // **This is the third test case...**
        else if(light_y > initial_ty) {
            cout << "SW" << endl;
            initial_ty++;
        }
        else if(light_x < initial_tx) {
            cout << "W" << endl;
            initial_tx--;
        }
        // **Don't forget to include the "else{}" statment at the end.**
        //
        // .. note::
        //
        //  Why?
        else{};
    }
}
// **Now you can press "PLAY ALL TESTCASES"**
