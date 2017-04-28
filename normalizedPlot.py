# normalizedPlot.py
# Create graph showing change from initial flood point over time

import foreclosuresOverTime as data
import pandas as pd
from dateutil.relativedelta import *
import datetime
from bokeh.plotting import figure, output_file, show

fcl = data.getForeclosures()
floods = data.getFloods()

#create plot
p = figure(x_axis_label='dates', y_axis_label='number of foreclosures')

numMonths = 18

#for each flood, plot number of foreclosures - number of foreclosures during initial month
for i in range(len(floods)):
    date = floods.BEGIN_DATE.iloc[i]
    xs = []
    for q in range(numMonths):
        xs.append(q)
    ys = []
    #x=[date,date]
    for k in range(numMonths):
        x = date + relativedelta(months=+k)
        #print(x)
        #locate the y-value of the foreclosures at the time of the flood
        for j in range(len(fcl)):
            if(x.month == fcl.Date.iloc[j].month and x.year == fcl.Date.iloc[j].year):
                y = fcl.Dallas.iloc[j]-fcl.Dallas.iloc[j-k]
        ys.append(y)

    p.line(xs,ys)

output_file("normalizedPlot.html")
show(p)