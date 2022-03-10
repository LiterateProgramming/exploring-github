// ******************************
// Logan Williams - Power of Thor
// ******************************
// This is my solution for the `Power of Thor <https://www.codingame.com/training/easy/power-of-thor-episode-1/solution>`_
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
// The idea is that Thor has an x and y position that is separate from the x and y position of the power, and this image shows that the plane is 40 wide by 18 high, but due to arrays this runs from 0 to 39 and 0 to 17.
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
        int lightY = int.Parse(inputs[1]);
        int initialTX = int.Parse(inputs[2]);
        int initialTY = int.Parse(inputs[3]);
        // The first two variables, ``lightX`` and ``lightY``, are used to set where the coordinates of the light orb's location is for each new level of the game. The next two variables are defined as ``initialTX`` and ``initialTY`` to be Thor's initial location. When first designing this program, I had two addtional variables that would update to thor's new location, but I realized when working through this that that would be unneeded. Instead of having variables that are only used one time to set an initial location, they can be reused for Thor's updated location as well. In hindsight for this solution, I should have changed the names of these variables to better illustrate their funcionality.

//
// ========
// Solution
// ========
        // This code operates by making multiple comparisons each time Thor moves. The loop begins by establishing that thor has a X and a Y direction, and creating a string variable that will store the Direction in it. For example, if Thor needs to move to the bottom right, then the if statements will check for whether Thor's X location is larger than the light's X value. The same will be done for the Y values of the game. Therefore after several runs through the code you will be moving in all cardinal directions. So the basic idea is that the strings will tell which cardinal direction we want to go in, while the code itself will run comparisons between thor's orginal/updated location and the light's location to decide if the move is valid for the game to be won.
        //
        // .. image:: PowerOfThorXY.png
        while (true)
            {
                // The remaining amount of turns Thor can move. Do not remove this line.
                int remainingTurns = int.Parse(Console.ReadLine());
                // directionX is a string used to fill with the cardinal direction thor will move in horizontally.
                string directionX = "";
                // directionY is a string used to fill with the cardinal direction thor will move in vertically.
                string directionY = "";
                // I used if/else statements to work through each cardinal direction and insert a value for each of the strings above. These values are then used in the function below to move Thor in the user's desired direction.
                //
                // In order to represent East and West, we use the Horizontal of the game, which in terms of an XY coordinate system is left and right. The picture above shows the XY planes.
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
                // In order to represent North and South, we use the Vertical of the game, which in terms of an XY coordinate system is up or down. The picture above shows the XY planes.
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
                //Console.WriteLine("SE"); // A single line providing the move to be made: N NE E SE S SW W or NW
                Console.WriteLine("{0}{1}",directionY,directionX);
