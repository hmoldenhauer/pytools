import numpy as np
import matplotlib.pyplot as plt

import lmfit

# import files from pytools has to be modified if used elsewhere
import sys
sys.path.insert(0, '/home/henning/repos/promotion/pytools')

import helper
import read
import functions

# folder with fitted data
basefolder = 'data/spotsize/'
foldername = basefolder + 'peaks/'

# folder with results from fityk
savename = 'results/'

# interesting peaks
peaks = [85, 153, 219, 473]
labels = np.char.mod('%d', peaks)

# peak for plotting and fitting
peak = 1
filetype = 'pdf'
savename = savename + 'spotsize_' + str(peaks[peak]) + 'cm-1'

# loading data
positions = np.loadtxt(basefolder + 'positions.txt', usecols=1)
listOfFiles = read.get_folder_content(foldername, 'txt')
numberOfFiles = len(listOfFiles)

# create lists containing all the peaks
height = []
center = []
gwidth = []
shape = []

# reading in all the peaks and adding them to a list
for index in range(0, numberOfFiles):
    h, c, w, s = read.get_fityk_voigt(listOfFiles[index])
    height.append(h)
    center.append(c)
    gwidth.append(w)
    shape.append(s)

# find the indices nearest to the most interesting peaks
indices = []
for signal in range(0, len(peaks)):
    row = []
    # search in all measurements for the corresponding peak
    for index in range(0, numberOfFiles):
        row.append(helper.find_nearest(center[index][0], peaks[signal]))
    indices.append(row)

x = positions
y = np.zeros((len(peaks), numberOfFiles))

for signal in range(0, len(peaks)):
    for dataset in range(0, numberOfFiles):
        y[signal][dataset] = height[dataset][0][indices[signal][dataset]]

# create model of the function
model = lmfit.Model(functions.spotsize)

result = model.fit(y[peak],
                    x=x,
                    I_off=150,
                    I0=2000,
                    x0=12,
                    w=5)
print(result.fit_report())
f = open(savename + '.txt', 'w')
f.write(result.fit_report())
f.close()

result.plot_fit(xlabel='position / µm',
                 ylabel='intensity / a.u.',
                 numpoints=1000)
plt.title('')                               # remove the title
plt.grid()                                  # plot grid
#plt.gca().get_lines()[0].set_linestyle('-') # change the linestyle of the data
#plt.gca().get_lines()[0].set_color('green') # change the color of the data
#plt.gca().get_lines()[1].set_color('red')   # change the color of the fit line
plt.legend((labels[peak], 'Fit'))       # create legend
plt.savefig(savename + '.' + filetype, format=filetype)   # save figure
plt.show()                                  # show plot
