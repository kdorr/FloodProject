# normalizedPlot.py
# Create graph showing change from initial flood point over time

import statsmodels.api as sm
import foreclosuresOverTime as data
import dataCleanFloods as dcf
from dateutil.relativedelta import *
from bokeh.plotting import figure, output_file, show
import numpy as np

fcl = data.getForeclosures()
floods = dcf.cleanedFloods
#floods = floods.iloc[0:115]

#create plot
p = figure(x_axis_label='months since flood', y_axis_label='change number of foreclosures since flood')

#the number of months to examine
numMonths = 18

#instiantiate lists that will hold all x-values and all y-values
allXs = []
allYs = []
resultsList = []

#for each flood, plot number of foreclosures - number of foreclosures during initial month
def singleRegression(xs, ys):
    xReg = np.vander(xs, 2)
    results = sm.OLS(ys, xReg).fit()
    return results


for i in range(len(floods)):
    date = floods.BEGIN_DATE.iloc[i]
    #recreate list for x-values and y-values
    xs = []
    for q in range(numMonths):
        xs.append(q)
    ys = []
    for k in range(numMonths):
        x = date + relativedelta(months=+k)

        #locate the y-value of the foreclosures at the time of the flood
        for j in range(len(fcl)):
            if(x.month == fcl.Date.iloc[j].month and x.year == fcl.Date.iloc[j].year):
                y = fcl.Dallas.iloc[j]-fcl.Dallas.iloc[j-k]
                #append the month and number of foreclosures to the lists containing
                #all month values and all foreclosure values
                allXs.append(k)
                allYs.append(y)
        ys.append(y)

    p.circle(xs,ys)
    results = singleRegression(xs, ys)
    resultsList.append(results)



#run linear regression model
xReg = np.vander(allXs, 2)
results = sm.OLS(allYs,xReg).fit()
#print(type(results))
#print(results.summary())

#plot regression model on graph
regLineX = range(0,numMonths)
getY = lambda r: -0.0165*r + .1946
regLineY = []
for i in range(len(regLineX)):
    regLineY.append(getY(i))
p.line(regLineX, regLineY, color='green')

#output and show plot
output_file("normalizedPlot.html")
#show(p)


