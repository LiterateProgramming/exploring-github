# *****************************************************
# Coding with Reflection - Death-First Search (sam1123)
# *****************************************************
# Solving the the `death-first-search puzzle <https://www.codingame.com/ide/puzzle/death-first-search-episode-1>`_ from codingame
#
# .. note::
#   Overall, there could be more of an explanation of what the problem statement is for this game. 
#   Without having knowledge of the problem, the reader could easily get lost on the solution since they don't know why the solution is needed.
#
#   The images provided a clear and explanitory and the code contains comments dispearsed throughout.
#
#   The variable names could be more descriptive or have comments explaining the variables usage for the reader. 
#
#   Solution passes all test cases sucessfully
#

# ^^^^^^^^^^^^^^^
# Solution Method
# ^^^^^^^^^^^^^^^
# .. image:: dfs_solution.png
#   :width: 95%

# My *intended* solution was going to include a graph search to find the shortest path. The virus moves as the code cuts the path, so the the shortest path is constantly changing. The solution would use depth first search to find the path to the exit then close the path farthest down the tree to the exit.
#
# My actual solution just ended up being to randomly cut a path in the graph. If the virus was next to an exit the program then cuts that exit path, and the process repeats. **This solution passed all the test cases of the codingame.** 

# =====================
# Imports and Variables
# =====================
# 
# This section imports libraries and initalizes variables used in the solution below. 
#
# Node_order stores - the nodes as they are read in from the program
# links stores -  the links to those nodes as they are read in
# exits stores  - which nodes are exits. 
# d is a dictionary - to store the nodes with there links. 
import sys
import math

node_order= []
links = []
exits = []
d = {}


# ================
# Read in the data
# ================
# 
# This section parses in the input data it keeps the connections of the graph sorted into a list
# 
# The input is given as links to the nodes. The connections are read one at a time based on what turn of the game it is. 
#
# :n: the total number of nodes in the level, including the gateways
# 
# :l: the number of links
# 
# :e: the number of exit gateways
#
#
#  
n, l, e = [int(i) for i in input().split()]
for i in range(l):
    # n1: N1 and N2 defines a link between these nodes
    n1, n2 = [int(j) for j in input().split()]

    if n1 in d and n2 in d:
        d[n1].append(n2)
        d[n2].append(n1)
    elif n1 in d and n2 not in d:
        d[n1].append(n2)
        d[n2] = [n1]
    elif n1 not in d and n2 in d:
        d[n2].append(n1)
        d[n1] = [n2]
    else:
        d[n1]=[n2]
        d[n2]=[n1]
# 
#   
# an example debug message for the system
    #print("Debug messages " + str(d), file=sys.stderr, flush=True)

for i in range(e):
    ei = int(input())  # the index of a gateway node
    exits.append(ei)
    #print("Debug messages " + str(input()), file=sys.stderr, flush=True)
# 
# =================
# The Game Loop
# =================
# 
# This is the loop where the game is played. 
# The input for the where the virus node is traveling to is given and the solution is generated as the game plays out. 
while True:
    si = int(input())  # The index of the node on which the Bobnet agent is positioned this turn

    node_order= []
    visited = []
    selected_exit = 0
    neighbor= False

# The solution below closes the path to the exit node if it is directly adjacent, or randomly closes a different path if there isnt an exit node adjacent. 
#
#  A value in the key-value pair can be a number, a string, a list, a tuple, or even another dictionary. In fact, you can use a value of any valid type in Python as the value in the key-value pair.
#  A key is accessed by dict[key] and the return is a  list of values for that key. 

    for exit_node in exits:

        if exit_node in d[si]:
            selected_exit = exit_node
            temp = si
            d[exit_node].remove(si)
            d[si].remove(exit_node)
            neighbor = True
            break

    if neighbor == False:
            temp = d[si][0]
            selected_exit = si
            d[si].remove(temp)
            d[temp].remove(si)


    print(selected_exit, temp)

# ========
# Results
# ========
# This is an image of the most complex test case with the program passing the case.

# .. image:: dfs_passing.png
#   :width: 95%
