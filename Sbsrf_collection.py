import numpy as np
from numpy import random
import pandas as pd
import sys
from gdpc import __url__, Editor, Block, Rect

editor = Editor(buffering=True)

sub_grid_init = np.loadtxt("grav_test_sf.csv",delimiter=" ", dtype=object)
sub_grid = sub_grid_init.reshape((200, 200, 44))
#sub_grid = np.zeros(shape=(200,200,44),dtype=object)

print("What z value would you like to record?:")
zs = sys.argv[1]
z=int(zs)
print("Please record line "+str(z))

rect = Rect((z,0), ((z+1),201))

worldSlice = editor.loadWorldSlice(rect)

for x in range(0,200):
    for y in range(20, 64):
        sub_grid[z, x, 63-y] = str(editor.getBlock((x, y, z)))

#saving array as csv file to pull in other code
sub_reshaped = sub_grid.reshape(sub_grid.shape[0], -1)

np.savetxt("grav_test_sf.csv", sub_reshaped, delimiter=" ", fmt="%s")

print("Great! Row "+zs+" has been added to grav_test_sf.csv.")