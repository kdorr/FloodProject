# -*- coding: utf-8 -*-
"""
Created on Fri Mar 10 13:10:31 2017

@author: Kimberly
"""

def monthlyAverage(floodForeclosures):
    #for each flood, subtract month n from n+1, store that value into a list
    individualDifferences = averageIndividual(floodForeclosures)
    #find the average difference and store that in an array
    averageMonthlyDifferences = averageAll(individualDifferences)
    return averageMonthlyDifferences

def averageIndividual(floodForeclosures):
    avgList = []
    for k, v in floodForeclosures.items():
        tempList = []
        for i in range(len(v)-1):
            tempList.append(round(float(v[i+1])-float(v[i]), 4))
        avgList.append(tempList)
    #print(avgList)
    return avgList
    
def averageAll(differences):
    avgList = []
    average = 0.0
    totalSum = 0.0
    counter = 0
    #i will iterate through columns
    for i in range(len(differences[0])):
        #j will iterate through rows
        for j in range(len(differences)):
            totalSum += differences[j][i]
            counter += 1
        average = round(totalSum/len(differences),4)
        avgList.append(average)
    return avgList