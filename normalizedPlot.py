# normalizedPlot.py
# Create graph showing change from initial flood point over time

import foreclosuresOverTime as data
import pandas as pd
from bokeh.plotting import figure, output_file, show

fcl = data.getForeclosures()
flood = data.getFloods()

