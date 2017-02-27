"""
Created on Thu Feb 23 20:27:36 2017

@author: Tim
"""

import numpy
import csv
import sys
from matplotlib import pyplot as plt

#read foreclosure data
foreclosuresArray = []
foreclosures = open('TestForeclosures.csv',"r")
for line in foreclosures:
   foreclosuresArray.append(line.strip().split(','))
foreclosures.close()

#read flood data
floodsArray = []
floodsFile = open('storm_data_search_results_dallas.csv', "r")
for line in floodsFile:
    floodsArray.append(line.strip().split(','))
floodsFile.close()   
        
#format date from flood data
#floodsArray[1][3] is the flood date of the first flood listed for Dallas County
month = floodsArray[1][3].split('/')[0]
year = floodsArray[1][3].split('/')[2]
individualDate = year + '-' + month

def locateForeclosureDate(date):
    for i in range(len(foreclosuresArray[0])):
        if foreclosuresArray[0][int(i)] == date:
            return i

def getForeclosureData(index):
    arr = []
    for j in range(6):
        arr.append(foreclosuresArray[1][int(index)+j])
    return arr
    
#get yValues for graph
yVals = getForeclosureData(locateForeclosureDate(individualDate))
print(yVals)

#select dates for x-axis
datesGraph = [0, 1, 2, 3, 4, 5]

#Plot on graph
xs = [i for i, _ in enumerate(datesGraph)]
plt.plot(xs, yVals, 'g-', label='May 2011')

#Title, legend, and axis labels
plt.title("Number of Foreclosures per 10000 Homes in Dallas County after Flood")
plt.xlabel("Month")
plt.ylabel("Number of Forclosures per 10000 Homes")
plt.legend()

plt.show()