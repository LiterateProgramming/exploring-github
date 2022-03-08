// *******************
// Power of Thor
// *******************
/*
Use this link to access the coding game https://www.codingame.com/ide/puzzle/power-of-thor-episode-1

*Note: You can utilize any coding language that you are most comfortable with to write this code by changing this option in the code tab. I chose to use the C++ coding language.* 

**Instructions:
Write a program that will guide Thor to reach the light of power in the most efficient manner.**

*/
/*
Begin Game Code!
----------------
**Below is the code written for the solution, and some discriptions and reasoning behind the solution method, behind my code is also provided.**
*/
/*
Includes
--------

All of the includes you may need will already be be provided for you when you begin your coding game
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
//beginning bracket
{
    int light_x; // the X position of the light of power
    int light_y; // the Y position of the light of power
    int initial_tx; // Thor's starting X position
    int initial_ty; // Thor's starting Y position
    cin >> light_x >> light_y >> initial_tx >> initial_ty; cin.ignore();


    while (1) {
        int remaining_turns; // The remaining amount of turns Thor can move. Do not remove this line.
        cin >> remaining_turns; cin.ignore();
        
/*
Diagram
--------

.. image:: InkedThorDiagram.jpg


**Discription/Directions:** 

This a diagram of Thor at his starting postion. The red arrows are pointing at the XY plane and the compass below so that you can have a clear orientation of Thor as he moves within the boundary conditions. Remember the objective of the game is to get Thor to move towards the light of power. The directions you will use are: 

*N (North), NE (North East), E (East), SE (South East), S (South), SW(South West), W (West), and NW (North West).*

*/
/* 
Thor's Movement
----------------
**Based on the position light of power I first determined which direction he would travel and then developed this code on the basis of each test code.**

**Test case 1 & 2:**

This line of code is where you will put in how Thor will move. In order to observe what direction he will go in based on what you are already given click on the "play testcase" button in the bottom right hand corner and watch the video as he moves. After this you will change the direction that thor moves "E" (East) towards the light of power and you passed the first test case. You will notice that as you play each testcase the orientation of thor changes, so you can repeat the same process in testcase 01 (straight line) in test case 02 (Up) but this time go N North in the direction of the light of power. 
*/
/* **Test case 3:**

Easy angle is where things get a little tricky. In order to make Thor move toward the light of power, while also being mindful of his "Energy" located under the console output, you must how thor move SW (South West) and E (East) at the same time so you will need 2 else if statements. The reason you must increment is to prevent Thor from moving out of the boundary conditions before he reaches the light of power. 
*/
/* **Test case 4:**

The final test case (Optimal angle) utilizing everything implemented before while also assuring that the whole code is properly looped so that you can play all testcases. Here is where you apply the use of if and else if statements to get the last angle to be short but also keep you from running out of enery. You essentially have to loop Thor's inital direction twice so that he can reach the light of power.
*/
/* *Note: In order to loop each of the test cases to work all at the same time you have to use an if statement so that you can input more than one direction for each time that Thor moves. You will notice that as you play each testcase. Your conditions are created by making the light of power position X or Y (light_x/light_y) greater than or less than the positon of Thor(initial_tx/initial_ty) in the X or Y.*

Code for Movement
------------------

*/
// **this is the fourth test case...**
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
else{};
}
}// closing bracket

/* **Now you can press "PLAY ALL TESTCASES"**

*Note for room of improvement: A way that was brought to my improve this code be to create a solution separate from the test cases that will move Thor to the light from any position on the map.I am open to edits to aid in the further development of this code to make it reusable for any instance!*
*/