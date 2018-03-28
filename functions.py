import numpy as np
from scipy.special import erf

# define fano resonance
def fano(x, y0, amplitude, center, width, q):
    e = (x - center)/ (2 * width)
    return  y0 + amplitude * (q**2 + 2 * q * e - 1) / (1 + e**2)

# define gaussian function
def gaussian(x, y0, amplitude, center, width):
    w_sq = width**2
    return y0 + amplitude * 1 / np.sqrt(2 * np.pi * w_sq) * np.exp(-(x - center)**2 / (2 * w_sq))

# define multiple gaussian
def gaussian_multiple(x, y0, *params):
    y = np.zeros_like(x)
    for i in range(0, len(params), 3):
        amplitude = params[i]
        center = params[i+1]
        width = params[i+2]
        y = y + amplitude * np.exp( -((x - center)/width)**2)
    return y0 + y

# define function to get the spotsize
def spotsize(x, I_off, I0, x0, w):
    return I_off + I0 / 2 * (1 + erf(np.sqrt(2) * (x0 - x) / w))
