"""
Created on Thu Feb 23 20:27:36 2017

@author: Tim
"""
import urllib
import numpy
import csv
import sys
import os
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

    