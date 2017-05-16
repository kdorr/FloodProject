####################################################
# Authors: Tim Turner, Kim Orr, and Eric Dubinsky
# File Creation Date: April 25
# Upbring Flood Project
# Prepares data and plots the foreclosures over time
# Also plots the floods at their corresponding date
####################################################


import pandas as pd
from bokeh.plotting import figure, output_file, show
import dataCleanFloods as dcf

#Read foreclosure data
foreclosureFile = "ForeclosuresTransposed.csv"
dateparse = lambda x: pd.datetime.strptime(x, '%Y-%m')
foreclosures = pd.read_csv(foreclosureFile, parse_dates=['Date'], date_parser=dateparse)

#create plot
p = figure(x_axis_type="datetime", x_axis_label='Dates', y_axis_label='Number of foreclosures')

#plot foreclosures
p.line(x=foreclosures['Date'], y=foreclosures['Dallas'], color='green')

#plot floods
for i in range(len(dcf.cleanedFloods)):
    date = dcf.cleanedFloods.BEGIN_DATE.iloc[i]
    x=[date,date]
    #locate the y-value of the foreclosures at the time of the flood
    for j in range(len(foreclosures)):
        if(date.month == foreclosures.Date.iloc[j].month and date.year == foreclosures.Date.iloc[j].year):
            fcl = foreclosures.Dallas.iloc[j]
            break
    y=[fcl-1,fcl+1]
    p.circle(x,fcl, color='blue')

#output file and show
#output_file("bokeh2.html")
#show(p)