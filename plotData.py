# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 17:15:13 2017

@author: Kimberly
"""
from matplotlib import pyplot as plt
from scipy import stats
import analyze
import readData

#plot the number of foreclosures per month after floods
def numForeclosuresPerMonth(floodForeclosures, numMonths, county):
    #select dates for x-axis
    datesGraph = [x for x in range(numMonths-1)]

    #Plot on graph
    xs = [i for i, _ in enumerate(datesGraph)]
    
    for k, v in floodForeclosures.items():
        plt.plot(xs, v, label=k)
    
    #Title, legend, and axis labels
    plt.title("Number of Foreclosures per 10000 Homes in " + county + " County after Flood")
    plt.xlabel("Month")
    plt.ylabel("Number of Foreclosures per 10000 Homes")
    plt.axis([0, numMonths-1, -3, getMaximumY(floodForeclosures)])
    #plt.axis([0, numMonths-1, -5, 5])
    ax = plt.gca()
    ax.set_autoscale_on(False)
    #plt.legend(loc='best', ncol=4, fontsize='small')



    
    plt.show()
    
def changeForeclosures(floodForeclosures, numMonths, county):
    changedList=findAverage(floodForeclosures)
    #select dates for x-axis
    datesGraph = [x for x in range(numMonths-1)]

    #Plot on graph
    xs = [i for i, _ in enumerate(datesGraph)]
    
    for k, v in changedList.items():
        plt.plot(xs, v, label=k)
    
    #Title, legend, and axis labels
    plt.title("Number of Foreclosures per 10000 Homes in " + county + " County after Flood")
    plt.xlabel("Month")
    plt.ylabel("Number of Forclosures per 10000 Homes")
    plt.axis([0, numMonths-1, -3, getMaximumY(changedList)])
    plt.plot()
    plt.plot(regression(listChange(changedList), numMonths))
    #plt.axis([0, numMonths-1, -5, 5])
    ax = plt.gca()
    ax.set_autoscale_on(False)
    #plt.legend(loc='best', ncol=4, fontsize='small')
    
    plt.show()

#get the maximum y value for scaling purposes
def getMaximumY(floodForeclosures):
    maximum = 0.0
    for k, v in floodForeclosures.items():
        if float(max(v)) > maximum:
            maximum = float(max(v))
            #print(maximum)
    return int(round(maximum))+1
#==============================================================================
# Linear regression:
# Need to eventually move into function
#==============================================================================
def regressionLine(x,y):
    slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)
    #y=intercept+slope(x)
    #y=0.069997-0.0112x
    #==============================================================================
    # x = [0, 1, 2, 3, 4, 5, ... , 11]
    # y = [0.07-0.01(0), 0.07-0.01(1), ..., 0.07-0.01(11)]
    #==============================================================================
    print("slope")
    print(slope)
    print(intercept)
    print(r_value)
    print(r_value*r_value)
    return(slope,intercept)
def returnLine(changeList,numMonths):
    x = []
    y = []
    regline = []
    for i in range(len(changeList)):
        for j in range(len(changeList[i])):
            y.append(changeList[i][j])
            x.append(j)
    slope, intercept = regressionLine(x,y)
    for i in range(numMonths):
        regline.append(intercept+(slope*i))
    return (regline)
def findAverage(floodForeclosures):
    foreclosureChanges = analyze.averageIndividual(floodForeclosures)
    return foreclosureChanges
def listChange(foreclosureChanges):
    changeList=list(foreclosureChanges.values())
    return changeList
def regression(changeList,numMonths):
    regline=returnLine(changeList,numMonths)
    return regline


