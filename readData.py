# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 17:14:49 2017

@author: Kimberly
"""

#returns a dictionary that contains an entry for each flood containing:
# a list of the number of foreclosures per month after as the value and
# the date of the flood as the key.  
def foreclosureDataPerFlood(floodFile, foreclosureFile, numMonths):
    #CSV to List
    floodList = read(floodFile)
    foreclosureList = read(foreclosureFile)
    county = getCounty(floodList, foreclosureList)
    
    #Grab dates from floodFile and convert to foreclosureFile format
    datesList = getDates(floodList)
    
    #Delete duplicate dates
    datesList = deleteDuplicates(datesList)
    
    #Find dates in foreclosureFile, return a list of indicies?
    indices = getForeclosureIndices(foreclosureList, datesList)
    
    #Grab foreclosure info for each flood
    floodForeclosureList = getFloodForeclosureList(foreclosureList, indices, numMonths, county)
    #return floodForeclosureList
    
    #create dict and return it
    return populateDict(datesList, floodForeclosureList) 
    
#TODO figure out how many lines are actually supposed to be plotted and locate bug and fix it.
def dallasTroubleshoot(file):
    fileDates = read(file)
    dates = []
    for i in range(1,len(fileDates)):
        dates.append(convertDate(fileDates[i][0]))
    dates = deleteDuplicates(dates)
    return dates
 
#Read data from csv into a list
def read(fileName):
    tempLst = []
    file = open(fileName, "r")
    for line in file:
        tempLst.append(line.strip().split(','))
    file.close()
    return tempLst

#Figure out which county the data is from
#This is necessary for getFloodForeclosureList() to know which line of TestForeclosures to pull from
def getCounty(floodList, foreclosureList):
    floodCounty = floodList[1][1]
    floodCounty = floodCounty.split()
    floodCounty = floodCounty[0].capitalize()
    for i in range(len(foreclosureList)):
        if foreclosureList[i][0] == floodCounty:
            return i
    

#format date from flood data to match date format in foreclosure data
#floodsArray[1][3] is the flood date of the first flood listed
def convertDate(floodDate):
    month = floodDate.split('/')[0]
    if int(month) < 10:
        month = "0" + month
    year = floodDate.split('/')[2]   
    return year + '-' + month

#Grab dates from floodFile and convert to foreclosureFile format   
def getDates(floodList):
    dateList = []
    for i in range(1,len(floodList)-1):
        dateList.append(convertDate(floodList[i][3]))
    return dateList

#generic function to get rid of duplicate entries in a list
#returns the list without duplicates
#There were often several entries for the same flood or floods within a couple days of each other
def deleteDuplicates(datesList):
    noDupes = []
    [noDupes.append(i) for i in datesList if not noDupes.count(i)]
    return noDupes
    
#returns a list containing a list of indicies in the foreclosure data that correspond to
#where each flood date in datesList is located
def getForeclosureIndices(foreclosureList, datesList):
    indices = []
#len(datesList) = 64
    for i in range(len(datesList)):
        
        for j in range(len(foreclosureList[0])):
            if foreclosureList[0][j] == datesList[i]:
                indices.append(j)
    return indices

#returns a list that has a list containing the foreclosure numbers for each flood
def getFloodForeclosureList(foreclosureList, indices, numMonths, county):
    floodForeclosureList = []
    exception = False
    for i in range(len(indices)):
        a = []
        for j in range(numMonths):
            try:
                a.append(foreclosureList[county][int(indices[i])+j])
            except IndexError:
                a.append(-999)
                exception = True
        if exception != True:
            floodForeclosureList.append(a)
        else:
            print("error")
    return floodForeclosureList
    
#returns a dict containing the date of the flood with its foreclosure data.
#Rather than a list, a dict will allow us to filter our list by year/month if we want to.
def populateDict(dates, foreclosures):
    mydict = {}
    for i in range(len(foreclosures)):
        try:
            mydict[dates[i]] = foreclosures[i]
        except IndexError:
            print("index error")
    return mydict