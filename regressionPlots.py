###################################################
# regressionPlots.py
# Authors: Tim Turner, Kim Orr, and Eric Dubinsky
# File Creation Date: May 3
# Upbring Flood Project
# Created a regression for each flood
# Found the average regression and plotted
###################################################
import normalizedPlot as normal
from bokeh.plotting import figure, output_file, show
import pandas as pd
import statsmodels.api as sm

plt = figure(x_axis_label='Months since flood', y_axis_label='Predicted change in foreclosures for each flood')
allXs=normal.allXs
allYs=normal.allYs
testXs=allXs[0:18]
testYs=allYs[0:18]
results=normal.resultsList

#print(results[0].summary()) Will print the regression summary for a single point
regY=[]
#Plots the regression of each flood 18 months after the event
for i in range(len(results)):
    getY = lambda res: (results[i].params[0] * res) + results[i].params[1]
    for j in range(len(testXs)):
        regY.append(getY(j))
plt.circle(allXs, regY)

df = pd.DataFrame({"x" : allXs, "y" : regY})
#Plots the average regression using the previous regression lines
finalRegY = []
yCounter=0
ySum=0
for w in range(18):
    ySum=0
    for q in range(len(df.x)):
        if(df.x.iloc[q] == w):
            ySum+=df.x.iloc[q]
            yCounter+=1

    ySum=ySum/yCounter
    finalRegY.append(ySum)
plt.line(testXs, finalRegY, color='green')
regOfReg=normal.singleRegression(testXs,finalRegY)
lastY=[]


plt.line(testXs,lastY)
print(regOfReg.summary())




show(plt)

