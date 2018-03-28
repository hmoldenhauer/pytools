import numpy as np
import matplotlib.pyplot as plt

# import files from pytools has to be modified if used elsewhere
import sys
sys.path.insert(0, '/home/henning/repos/promotion/pytools')

import helper
import read
import remove

# works only if at least 2 files are used

# folder with measured data
foldername = 'data/spectra/'

# folder with reduced background
savename = 'results/'

# for muons
threshold = 0.1
halfwidth = 10
muonsPerFrame = 5
sensitivity = 10

frame = 0

# loading data
listOfFiles = read.get_folder_content(foldername, 'txt')
x, y_raw = read.get_mono_data(listOfFiles)

# remove muons
indexes = remove.find_muons(y_raw, threshold, halfwidth)
y_muon_free = remove.remove_muons(y_raw, indexes, muonsPerFrame, halfwidth, sensitivity)

# remove background
y = remove.remove_median(y_muon_free)

# calculate average spectrum and set minimal value to zero
y_average = np.average(y, axis=0)
y_average = y_average - min(y_average)

data = np.vstack((x[0], y_average)).T
np.savetxt(savename + 'average.csv', data, '%1.2f')

plt.plot(x[frame], y_raw[frame], label='raw data')
plt.plot(x[frame], y_muon_free[frame], label='muons removed')
plt.plot(x[0], y_average, label='average')
plt.legend()

plt.show()
