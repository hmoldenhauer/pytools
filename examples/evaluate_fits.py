import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate

# import files from pytools has to be modified if used elsewhere
import sys
sys.path.insert(0, '/home/henning/repos/promotion/pytools')

import read
import functions

# works only if at least 2 files are used

# folder with measured data
foldername = 'results/'
filename = 'average'

peak = 13

# loading peak data, sorted by center
height, center, width, shape = read.get_fityk_voigt(foldername + filename + '.peaks')
# loading average data
x, y = read.get_mono_data([foldername + filename + '.csv'])

plt.plot(x, y)
plt.plot(center[0], height[0], 'o')
plt.plot(x,functions.fityk_pseudo_voigt(x, height[0][peak],
                                           center[0][peak],
                                           width[0][peak],
                                           shape[0][peak]))

plt.show()
