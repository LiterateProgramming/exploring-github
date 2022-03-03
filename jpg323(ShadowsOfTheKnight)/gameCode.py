import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# w: width of the building.
# h: height of the building.
w, h = [int(i) for i in input().split()]
n = int(input())  # maximum number of turns before game over.
x0, y0 = [int(i) for i in input().split()]

w_dist = w//2
h_dist = h//2

bomb_dir = "AB"
old_dir = "AB"
started = 0
# game loop
while True:
    started = 1
    if started == 1:
        old_dir = bomb_dir
    bomb_dir = input()  # the direction of the bombs from batman's current location (U, UR, R, DR, D, DL, L or UL)
    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)


    # the location of the next window Batman should jump to.
    ## VERTICAL
    if "D" in bomb_dir:
        if h_dist == 0:
            h_dist+=1
        y0+=h_dist
        #if "D" not in old_dir:
        h_dist//=2
        if y0 >= h:
            y0 = h-1


    elif "U" in bomb_dir:
        if h_dist == 0:
            h_dist+=1
        y0-=h_dist
        #if "U" not in old_dir:
        h_dist//=2
        if y0 < 0:
            y0=0
    ## HORZONTAL
    if "L" in bomb_dir:
        if w_dist == 0:
            w_dist+=1
        x0-=w_dist
        #if "L" not in old_dir:
        w_dist//=2
        if x0 < 0:
            x0=0
    elif "R" in bomb_dir:
        if w_dist == 0:
            w_dist+=1
        x0+=w_dist
        #if "R" not in old_dir:
        w_dist//=2
        if x0 >= w:
            x0 = w-1

    ## Handling 0s
    print("x0, y0:", file=sys.stderr, flush=True)
    print(x0, y0, file=sys.stderr, flush=True)

    print("w_dist, h_dist", file=sys.stderr, flush=True)
    print(w_dist, h_dist, file=sys.stderr, flush=True)
    
    print("old_dir, bomb_dir", file=sys.stderr, flush=True)
    print(old_dir, bomb_dir, file=sys.stderr, flush=True)

    print(x0, y0)