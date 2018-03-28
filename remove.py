import numpy as np
import peakutils
import helper

# remove median value of data inserted
def remove_median(y_raw):
    # create arrays to save the data
    median = np.array([])
    y = np.array([])

    # remove median for each point in frame
    for frame in range(0, len(y_raw)):
        if frame != 0:
            median = np.vstack((median, np.median(y_raw[frame])))
            y = np.vstack((y, y_raw[frame] - median[frame]))
        else:
            median = np.median(y_raw[frame])
            y = y_raw[frame] - median

    return y

# find possible muons in dataset
def find_muons(y_raw, threshold, halfwidth):
    # create list to save the indexes
    indexes = []

    # find indexes of possible muons
    for frame in range(0, len(y_raw)):
        ind = peakutils.indexes(y_raw[frame],
                                thres=threshold,
                                min_dist=2*halfwidth)
        indexes.append(ind)

    return indexes

# remove muons from dataset
def remove_muons(y, indexes, muonsPerFrame, halfwidth, sensitivity):
    # check if indexes are corresponding to muons or something else
    for frame in range(0,len(indexes)):
        ind = indexes[frame]
        if len(ind) < muonsPerFrame:
            # iterate over all muons in a frame
            for muon in ind:
                # define interval of the suspected muon
                interval = np.arange(muon - halfwidth, muon + halfwidth)

                # set muons to values of the following spectrum
                if frame < len(ind)-1:
                    if abs(y[frame][muon] - y[frame][muon+1]) >= sensitivity:
                        # remove muons in the given frame
                        for i in interval:
                            y[frame][i] = y[frame+1][i]
                else:
                    if abs(y[frame][muon] - y[frame][muon-1]) >= sensitivity:
                        # remove muons in the given frame
                        for i in interval:
                            y[frame][i] = y[frame-1][i]

    return y
