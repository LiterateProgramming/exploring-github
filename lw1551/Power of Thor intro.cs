// *************
// Power of Thor
// *************
// This is my solution for the `Power of Thor coding game <https://www.codingame.com/training/easy/power-of-thor-episode-1/solution>`_
//
//
// =====================
// Thought Process
// =====================
// * Thor needs to be able to move based on the different locations of the power orb.
// * Thor currently just walks off the screen and goes out of bounds due to being stuck in a while loop that does not check to see thor's location in relation to either the light or the border of the screen.
// * There is going to need to be a way to increment Thor’s location in at least two variables depending on the cardinal direction he moves in.
// * Make a variable that is Thor’s updated location after he moves from his initial location, then change this variable based on checking where thor is in relation to the power orb.
// * Use *if statements* to check for thor’s updated location compared to the orb, then use *else statements* to compare them for each direction that thor can move in.
//
// .. image:: Power_Of_Thor.png
//
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
        int lightX = int.Parse(inputs[0]); 
        // The X position of the light of power
        int lightY = int.Parse(inputs[1]); 
        // The Y position of the light of power
        int initialTX = int.Parse(inputs[2]); 
        // Thor's starting X position
        int initialTY = int.Parse(inputs[3]); 
        // Thor's starting Y position
 //
        // The first two variables, lightX and lightY, are used to set where the coordinates of the light orb's location for each new level of the game. I then defined initialTX and initialTY to be Thor's initial location. When first designing this program, I had two addtional variables that would update to thor's new location, but I realized when working through this that the initialTX and initialTY variables can be used for both functions.
//
//
//
        string directionX = "";
        // Blank X direction string to fill with direction thor will move in.
        string directionY = "";
        // Blank Y direction string to fill with direction thor will move in.
        // These variables are used to read in the cardinal direction given by the player of the game.

// ****************
// Solution
// ****************
// This code operates by making multiple comparisons each time Thor moves. The loop begins by establishing that thor has a X and a Y direction, and creating a string variable that will store the Direction in it. For example, if Thor needs to move to the bottom right, then the if statements will check for whether Thor's X location is larger than the light's X value. The same will be done for the Y values of the game. Therefore after several runs through the code you will be moving in all cardinal directions. So the basic idea is that the strings will tell which cardinal direction we want to go in, while the code itself will run comparisons between thor's orginal/updated location and the light's location to decide if the move is valid for the game to be won. 
            while (true)
        {
            int remainingTurns = int.Parse(Console.ReadLine()); 
            // The remaining amount of turns Thor can move. Do not remove this line.

            string directionX = "";
            // Blank X direction string to fill with direction thor will move in.
            string directionY = "";
            // Blank Y direction string to fill with direction thor will move in.

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