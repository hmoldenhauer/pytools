import glob
import numpy as np
import helper

# return a list of all files in a folder
def get_folder_content(foldername, filetype):
    #generate list of txt-files in requested folder
    foldername = foldername + '*.' + filetype
    listOfFiles = sorted(glob.glob(foldername))
    numberOfFiles = len(listOfFiles)
    # tell the number of files in the requested folder
    helper.teller(numberOfFiles, 'file', 'folder')

    return listOfFiles

# returns arrays containing the measured data
def get_mono_data(listOfFiles):
    # define arrays to hold data from the files
    inversecm = np.array([])
    intensity = np.array([])

    # read all files
    for fileName in listOfFiles:
        # read one file
        index = listOfFiles.index(fileName)
        cm, inty = np.genfromtxt(listOfFiles[index], unpack=True)
        if index != 0:
            inversecm = np.vstack((inversecm, cm))
            intensity = np.vstack((intensity, inty))
        else:
            inversecm = cm
            intensity = inty

    return inversecm, intensity

# read the Fit info from fityk and return them as np array
# height[0] contains the values
# height[1] contains the corresponding errors
def get_fityk_voigt(filename):
        # the files are constructed with multiple columns.
        # they are in sets of 4 (height, center, gwidth, shape)
        # col 0 = peak number
        # col 1 = '='
        # col 2 = name of the parameter
        # col 3 = '='
        # col 4 = value
        # col 5 = '±'
        # col 6 = error
        value = np.loadtxt(filename, usecols=4)
        error = np.loadtxt(filename, usecols=6)

        # slice the dataset into the corresponding values
        height = value[0::4]
        center = value[1::4]
        gwidth = value[2::4]
        shape = value[3::4]

        # same for the errors
        height_error = error[0::4]
        center_error = error[1::4]
        gwidth_error = error[2::4]
        shape_error = error[3::4]

        # create stacks of values and errors, to reduce number of parameters
        height = np.vstack((height, height_error))
        center = np.vstack((center, center_error))
        gwidth = np.vstack((gwidth, gwidth_error))
        shape = np.vstack((shape, shape_error))

        # sort the values by center
        sorted_height = np.zeros_like(height)
        sorted_center = np.zeros_like(center)
        sorted_gwidth = np.zeros_like(gwidth)
        sorted_shape = np.zeros_like(shape)

        sorted_indices = np.argsort(center[0])
        for i, value in enumerate(sorted_indices):
            for j in range(0, 2):
                sorted_height[j][i] = height[j][value]
                sorted_center[j][i] = center[j][value]
                sorted_gwidth[j][i] = gwidth[j][value]
                sorted_shape[j][i] = shape[j][value]

        return sorted_height, sorted_center, sorted_gwidth, sorted_shape
