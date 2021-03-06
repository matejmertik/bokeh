# The plot server must be running
# Go to http://localhost:5006/bokeh to view this plot

import numpy as np
from six.moves import zip
from bokeh.plotting import *

N = 4000

x = np.random.random(size=N) * 100
y = np.random.random(size=N) * 100
radii = np.random.random(size=N) * 1.5
colors = ["#%02x%02x%02x" % (r, g, 150) for r, g in zip(np.floor(50+2*x), np.floor(30+2*y))]

output_server("color_scatter")

scatter(x,y, radius=radii, radius_units="data",
        fill_color=colors, fill_alpha=0.6,
        line_color=None, tools="select,pan,wheel_zoom,box_zoom,reset,previewsave", name="color_scatter_example")

show()  # open a browser
