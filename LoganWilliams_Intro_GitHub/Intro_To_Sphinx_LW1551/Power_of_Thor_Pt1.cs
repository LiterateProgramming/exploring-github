// **********************
// Power of Thor, part 1
// **********************
// This is my solution for the Power of Thor coding game: https://www.codingame.com/training/easy/power-of-thor-episode-1/solution.
// The process behind this solution is explained in the rest of this document.
//
// .. note:: This should be a hyperlink instead of a pasted link. 
//
// See `notes` ...
//
// =====================
// Thought Process
// =====================
// * Thor needs to be able to move based on the different locations of the power orb.
// * Thor currently just walks off the screen and goes out of bounds due to being stuck in a while loop that does not check to see thor's location in relation to either the light or the border of the screen.
// * There is going to need to be a way to increment Thor’s location in at least two variables depending on the cardinal direction he \moves in.
// * Make a variable that is Thor’s updated location after he moves from his initial location, then change this variable based on checking where thor is in relation to the power orb.
// * Use *if statements* to check for thor’s updated location compared to the orb, then use *else statements* to compare them for each direction that thor can move in.
// 
// .. image:: Power_Of_Thor.png
// .. note:: 
//          This Image should have more of a description around it. Perhaps directly below the image would be suitable.
// -------------------
// Desgin Constraints
// -------------------
// 1. Thor cannot move beyond the coordinate plane defined by the game, which is **40 width by 18 height**.
//
// 2. Thor cannot run out of energy; the game allows for a **maximum of 100 energy**.
//
// ---------------------
// Defined Variables
// ---------------------
// 
        string[] inputs = Console.ReadLine().Split(' ');
        int lightX = int.Parse(inputs[0]); // the X position of the light of power
        int lightY = int.Parse(inputs[1]); // the Y position of the light of power
        int initialTX = int.Parse(inputs[2]); // Thor's starting X position
        int initialTY = int.Parse(inputs[3]); // Thor's starting Y position
 //
 // The first two variables, lightX and lightY, are used to set where the coordinates of the light orb's location for each new level of the game. I then defined initialTX and initialTY to be Thor's initial location. When first designing this program, I had two addtional variables that would update to thor's new location, but I realized when working through this that the initialTX and initialTY variables can be used for both functions.
//
//
        string directionX = "";// Blank X direction string to fill with direction thor will move in.
        string directionY = "";// Blank Y direction string to fill with direction thor will move in.
// These variables are used to read in the cardinal direction given by the player of the game.

// ****************
// Solution
// ****************
// This code is what I came up with to move Thor by going into a while loop and then using if else statements to compare thor's location with the location of the orb, and then increment either the X or the Y variable based on where Thor moved in relation to the Orb. 
            while (true)
        {
            int remainingTurns = int.Parse(Console.ReadLine()); // The remaining amount of turns Thor can move. Do not remove this line.
           
            string directionX = "";// Blank X direction string to fill with direction thor will move in.
            string directionY = "";// Blank Y direction string to fill with direction thor will move in.
            
            if (initialTX > lightX) 
            {
                directionX = "W";
                initialTX--;
            }
            else if(initialTX < lightX)
            {
                directionX = "E";
                initialTX++;
            }
            
            if(initialTY > lightY)
            {
                directionY = "N";
                initialTY--;
            }
            else if(initialTY < lightY)
            {
                directionY = "S";
                initialTY++;
            }