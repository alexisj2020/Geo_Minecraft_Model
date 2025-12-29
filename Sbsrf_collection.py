import numpy as np
from numpy import random
import pandas as pd
import sys

from gdpc import __url__, Editor, Block

editor = Editor(buffering=True)

sub_grid_init = np.loadtxt("sub_grid.csv",delimiter=",", dtype=object)
sub_grid = sub_grid_init.reshape((256, 256, 64))

print("What z value would you like to record?:")
zs = input()
z=int(zs)

for x in range(0,256):
    #for z in range(0, 256):
    for y in range(-63, 1):
        sub_grid[z, x, 64+(y-1)] = str(editor.getBlock((x, y, z)))

#saving array as csv file to pull in other code
sub_reshaped = sub_grid.reshape(sub_grid.shape[0], -1)

np.savetxt("sub_grid.csv", sub_reshaped, delimiter=",", fmt="%s")

print("Great! Row "+zs+" has been added to sub_grid.csv.")