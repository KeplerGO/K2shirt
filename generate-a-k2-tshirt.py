"""Create a simulated a Kepler spacecraft image that shows the letters "K2".

Author: Geert Barentsen
Purpose: Make a sick K2 t-shirt or mug!
"""
import matplotlib.pyplot as pl
import numpy as np
from scipy.ndimage.filters import gaussian_filter
from scipy.misc import imfilter

# Template: pixel array containing the K2 letters, yes I made this by hand.
ar = np.array([[0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,  0],
               [0, 255,  -1,   0,   0, 255,  -1,   0, 255, 255, 255,  -1,  0],
               [0, 255,  -1,   0, 255,  -1,   0, 255,  -1,   0,   0, 255, -1],
               [0, 255,  -1, 255,  -1,   0,   0,   0,   0,   0,   0, 255, -1],
               [0, 255, 255,  -1,   0,   0,   0,   0, 255, 255, 255,  -1,  0],
               [0, 255,  -1, 255,  -1,   0,   0, 255,  -1,   0,   0,   0,  0],
               [0, 255,  -1,   0, 255,  -1,   0, 255,  -1,   0,   0,   0,  0],
               [0, 255,  -1,   0,   0, 255,  -1, 255, 255, 255, 255, 255, -1],
               [0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,  0]])

# Add noise
ar[(ar < 255) & (ar > -0.5)] = 30
ar[ar < 0] = 30
ar += np.random.normal(0, 5, size=ar.shape).astype(int)

# Convolve with a "PSF"
ar = gaussian_filter(ar, sigma=0.4)

# Plot the result
fig = pl.figure(figsize=ar.T.shape)
ax = pl.axes([0, 0, 1, 1])
pl.imshow(ar, interpolation='nearest', cmap='gray', vmin=0, vmax=130)
fig.axes[0].get_xaxis().set_visible(False)
fig.axes[0].get_yaxis().set_visible(False)
pl.savefig('output.png', dpi=200)

