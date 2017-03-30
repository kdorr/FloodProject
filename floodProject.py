"""
Created on Thu Feb 23 20:27:36 2017

@author: Tim
"""

import numpy
import csv
import sys
from matplotlib import pyplot as plt
import readData
import plotData
import analyze

#for troubleshooting purposes. There is a bug where not all dates are being utilized
dallasTroubleshoot = readData.dallasTroubleshoot('dallasRemoveMostduplicates.csv')

numMonths = 13 #the number of months to look at. Will show numMonths-1 months after the flood.

#==============================================================================
# Note: I haven't figured out how to plot each county on a separate graph, so 
# only plot one county at a time.
#==============================================================================

#Dallas County
dallasFloodForeclosures = readData.foreclosureDataPerFlood('dallasFloods.csv', 'TestForeclosures.csv', numMonths)
print("Dallas Flood Foreclosures")
print(dallasFloodForeclosures)
#print("Dallas Dates:")
#print(dallasFloodForeclosures.keys())
#plotData.numForeclosuresPerMonth(dallasFloodForeclosures, numMonths, "Dallas")

#Collin County
#collinFloodForeclosures = readData.foreclosureDataPerFlood('collinFloods.csv', 'TestForeclosures.csv', numMonths)
#plotData.numForeclosuresPerMonth(collinFloodForeclosures, numMonths, "Collin")

#Tarrant County
#tarrantFloodForeclosures = readData.foreclosureDataPerFlood('tarrantFloods.csv', 'TestForeclosures.csv', numMonths)
#plotData.numForeclosuresPerMonth(tarrantFloodForeclosures, numMonths, "Tarrant")

#Dallas County Control (no floods)
#TODO find array of foreclosure numbers for months that correspond to each flood where there are no floods

#TODO find average/average difference of foreclosures for each month after flood
#dallasMonthlyAvg = analyze.monthlyAverage(dallasFloodForeclosures)
dallasChangeForeclosures = analyze.averageIndividual(dallasFloodForeclosures)
print("dallas analysis")
print(dallasMonthlyAvg)

plotData.changeForeclosures(dallasChangeForeclosures, numMonths, "Dallas")