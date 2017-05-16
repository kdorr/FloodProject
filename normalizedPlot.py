###################################################
# normalizedPlot.py
# Authors: Tim Turner, Kim Orr, and Eric Dubinsky
# File Creation Date: April 28
# Upbring Flood Project
# Create graph showing change from initial flood point over time
###################################################

import statsmodels.api as sm
import foreclosuresOverTime as data
import dataCleanFloods as dcf
from dateutil.relativedelta import *
from bokeh.plotting import figure, output_file, show
import numpy as np

#returns the results from a linear regression on the list of xs and ys passed in
def singleRegression(xs, ys):
    xReg = np.vander(xs, 2)
    results = sm.OLS(ys, xReg).fit()
    return results

#fetch foreclosure and flood data
fcl = data.foreclosures
floods = dcf.cleanedFloods

#set up normalized plot
p = figure(x_axis_label='Months since flood', y_axis_label='Change in number of foreclosures since flood')

#the number of months to examine
numMonths = 18

#instiantiate lists that will hold all x-values and all y-values
#allXs and allYs
allXs = []
allYs = []
resultsList = []

#---------------------------------------------------------------------------------------------------
# Create the data set for the normalized plot.
# This section populates allXs and allYs with the months and changes in the number of foreclosures
# for each flood. resultsList is populated with the linear regressions of each flood. It also
# creates the normalized plot.
#---------------------------------------------------------------------------------------------------
#iterate through the entire list of floods and find the number of foreclosures.
for i in range(len(floods)):
    date = floods.BEGIN_DATE.iloc[i]

    #instantiate/recreate list for x and y-values for the individual flood being examined
    xs = []
    for q in range(numMonths):
        xs.append(q)
    ys = []

    #start locating the number of foreclosures for numMonths months after the flood
    for k in range(numMonths):
        x = date + relativedelta(months=+k)

        #locate the y-value of the foreclosures at the time of the flood
        for j in range(len(fcl)):
            if(x.month == fcl.Date.iloc[j].month and x.year == fcl.Date.iloc[j].year):
                #y is the number of foreclosures at month j minus the number of foreclosures in the flood month
                y = fcl.Dallas.iloc[j]-fcl.Dallas.iloc[j-k]
                allXs.append(k) #append the month to allXs
                allYs.append(y) #append the change in the number of foreclosures to allYs
        ys.append(y)

    p.circle(xs,ys)
    results = singleRegression(xs, ys)
    resultsList.append(results)
#---------------------------------------------------------------------------------------------------
# END SECTION
#---------------------------------------------------------------------------------------------------

#output and show plot
output_file("normalizedPlot.html")
show(p)


