# Python functions to manipulate data

There are some functions defined to manipulate measured data.
Example scripts are given in the `examples/` folder.

## Steps to use the scripts

1. Apply `generate_average.py` to your data (take data from `testdata\`).
This will remove muons and linear background from your data
(removes median value).
2. In the `results\` folder you will find an `average.csv` ready for
peak fitting.
3. Use fityk to fit the peaks and export the results to an `average.peaks`
file in your results folder.
