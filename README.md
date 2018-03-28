# Python functions to manipulate data

There are some functions defined to manipulate measured data.
Example scripts are given in the `examples/` folder.

## General spectra analysis

1. Apply `generate_average.py` to your data (take data from `testdata\`).
This will remove muons and linear background from your data
(removes median value).
2. In the `results\` folder you will find an `average.csv` ready for
peak fitting.
3. Use fityk to fit the peaks and export the results to an `average.peaks`
file in your results folder.

## Spot size analysis

The analysis is based on this paper:
[Spot Size Engineering in Microscope-Based Laser Spectroscopy]
(https://pubs.acs.org/doi/abs/10.1021/acs.jpcc.6b04574)

1. fit your spectra with fityk and save them in a `peaks/` folder.
2. run the `evaluate_spotsize.py` in order to figure out your spotsize.
