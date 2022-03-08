# *******************************************
# Coding with Reflection - Death-First Search
# *******************************************
# Solving the the `death-first-search puzzle <https://www.codingame.com/ide/puzzle/death-first-search-episode-1>`_ from codingame

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
import sys
import math

node_order= []
links = []
exits = []
d = {}


# ================
# Read in the data
# ================
# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
# 
# n: the total number of nodes in the level, including the gateways
# 
# l: the number of links
# 
# e: the number of exit gateways
#
# This section parses in the input data it keeps the connections of the graph sorted into a list
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
