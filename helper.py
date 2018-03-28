import numpy as np

# find the nearest index in an array to a given value
def find_nearest(array,value):
    index = (np.abs(array - value)).argmin()
    return index

# print some stuff
def teller(number, kind, location):
    if number != 1:
        print('There are {} {}s in this {}.'.format(number, kind, location))
        print()
    else:
        print('There is {} {} in this {}.'.format(number, kind, location))
        print()

# save xy data of an array to a savename and format it correctly
def save_xy_array_data(x, y, savename, formatter):
    for dataset in range(0, len(y)):
        data = np.array([])
        if dataset != 0:
            data = np.vstack((x[dataset], y[dataset])).T
        else:
            data = np.vstack((x[dataset], y[dataset])).T
        np.savetxt(savename + str(dataset+1) + '.csv', data, formatter)
