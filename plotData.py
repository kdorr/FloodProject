# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 17:15:13 2017

@author: Kimberly
"""
from matplotlib import pyplot as plt

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
    plt.ylabel("Number of Forclosures per 10000 Homes")
    plt.axis([0, numMonths-1, -3, getMaximumY(floodForeclosures)])
    #plt.axis([0, numMonths-1, -5, 5])
    ax = plt.gca()
    ax.set_autoscale_on(False)
    #plt.legend(loc='best', ncol=4, fontsize='small')



    
    plt.show()
    
def changeForeclosures(floodForeclosures, numMonths, county):
    #select dates for x-axis
    datesGraph = [x for x in range(numMonths-1)]

    #Plot on graph
    xs = [i for i, _ in enumerate(datesGraph)]
    
    for k, v in floodForeclosures.items():
        plt.scatter(xs, v, label=k)
    
    #Title, legend, and axis labels
    plt.title("Number of Foreclosures per 10000 Homes in " + county + " County after Flood")
    plt.xlabel("Month")
    plt.ylabel("Number of Forclosures per 10000 Homes")
    plt.axis([0, numMonths-1, -3, getMaximumY(floodForeclosures)])
    plt.plot()
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