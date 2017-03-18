"""
Created on Thu Feb 23 20:27:36 2017

@author: Tim
"""
import urllib
import numpy
import csv
import sys
import os
from matplotlib import pyplot as plt
#foreclosureDataURL = "https://raw.github.com/kdorr/FloodProject/blob/master/County_HomesSoldAsForeclosures-Ratio_AllHomes-2.csv"
#response = urllib.request.urlopen(foreclosureDataURL)
#print (os.listdir())
#foreclosures = csv.reader(df)
foreclosuresArray = []
#foreclosures = open('County_HomesSoldAsForeclosures-Ratio_AllHomes-2.csv',"r")
#for line in foreclosures:
#    foreclosuresArray.append(line.strip().split(','))
foreclosures = open('TestForeclosures.csv',"r")
for line in foreclosures:
    foreclosuresArray.append(line.strip().split(','))
print(foreclosuresArray)

#==============================================================================
#                                Read Data
#==============================================================================

#reads comma-separated data from specified file into an array
def readCSVData(fileName):
    tempArr = []
    file = open(fileName, "r")
    for line in file:
        tempArr.append(line.strip().split(','))
    file.close()
    return tempArr

#read data flood and foreclosure data into arrays
floodsArray = readCSVData('storm_data_search_results_dallas.csv')
foreclosuresArray = readCSVData('TestForeclosures.csv')
  
#==============================================================================
#                             Manipulate Data
#==============================================================================     

#format date from flood data to match date format in foreclosure data
#floodsArray[1][3] is the flood date of the first flood listed for Dallas County
def convertDate(floodDate):
    month = floodDate.split('/')[0]
    year = floodDate.split('/')[2]   
    return year + '-' + month

numMonths = 14 #the number of months to look at (to be used in zero-indexed things)
numFloods = 25 #the number of floods to look at
allDates = [] #an array containing the dates of all floods

#populate allDates with the dates of all floods in floodsArray from the first entry to numFloods
for i in range(1,numFloods+1):
    allDates.append(convertDate(floodsArray[i][3]))

#find the dates in foreclosure data that correspond to dates found in flood data
def locateForeclosureDate(date):
    for i in range(len(foreclosuresArray[0])):
        if foreclosuresArray[0][int(i)] == date:
            return i

#find the index of the flood date in the foreclosure data
def getForeclosureData(index):
    lst = []
    for j in range(numMonths):
        lst.append(foreclosuresArray[1][int(index)+j])
    return lst

#==============================================================================
#                         Get Points for Graph
#==============================================================================

#get YValues for the graph
allYVals = [] #will be popluated with lists containing the y-values corresponding to each date
for i in range(numFloods):
    allYVals.append(getForeclosureData(locateForeclosureDate(allDates[i])))
print(allYVals)

#select dates for x-axis
datesGraph = [x for x in range(numMonths)]

#==============================================================================
#                              Plot Graph
#==============================================================================

#Plot on graph
xs = [i for i, _ in enumerate(datesGraph)]
print(len(allYVals))
#for each flood date, plot the corresponding number of foreclosures
for i in range(1, len(allYVals)):
    plt.plot(xs, allYVals[i], label=i)

#Title, legend, and axis labels
plt.title("Number of Foreclosures per 10000 Homes in Dallas County after Flood")
plt.xlabel("Month")
plt.ylabel("Number of Forclosures per 10000 Homes")
plt.axis([0, numMonths-1, 0, 15])
ax = plt.gca()
ax.set_autoscale_on(False)
#plt.legend()

plt.show()