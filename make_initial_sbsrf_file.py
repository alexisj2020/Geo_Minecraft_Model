import numpy as np
from numpy import random
import pandas as pd
import sys

#generate empty array of same shape as subsurface pull
sub_grid_init = np.zeros(shape=(200,200,44))

#reshape to save as a csv
sub_reshaped = sub_grid_init.reshape(sub_grid_init.shape[0], -1)

#save as a csv
np.savetxt("subsurface_2.csv", sub_reshaped, delimiter=" ", fmt="%s")