import pandas as pd

#Read flood data
floodFile ="dallasFloods.csv"
dateparse = lambda x: pd.datetime.strptime(x, '%m/%d/%Y')
floods = pd.read_csv(floodFile, parse_dates=['BEGIN_DATE'], date_parser=dateparse)

#Reduce number of columns in floods
floods = floods[['CZ_NAME_STR', 'BEGIN_DATE', 'EVENT_TYPE', 'DAMAGE_PROPERTY_NUM']]

#Remove duplicates (only report one flood per month)
#remove floods that are after May 2015. Any dates after May 2015 cause issues in
#other scripts because we run out of foreclosure data to compare to.
currentMonth = 0
currentYear = 0
cleanedFloods = pd.DataFrame(columns=floods.columns)
for i in range(len(floods)):
    previousMonth = currentMonth
    previousYear = currentYear
    currentMonth = floods.BEGIN_DATE.iloc[i].month
    currentYear = floods.BEGIN_DATE.iloc[i].year
    #Append a row if to a new dataframe if the current date is not a duplicate and
    #the current date is not after May 2015.
    if((currentMonth != previousMonth or currentYear != previousYear) and (currentYear < 2016)):
        if(currentYear == 2015 and currentMonth > 5):
            pass
        else:
            row = floods.iloc[i]
            cleanedFloods = cleanedFloods.append(row, ignore_index=True)