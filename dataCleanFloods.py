import pandas as pd

#Read flood data
floodFile ="dallasFloods.csv"
dateparse = lambda x: pd.datetime.strptime(x, '%m/%d/%Y')
floods = pd.read_csv(floodFile, parse_dates=['BEGIN_DATE'], date_parser=dateparse)

#clean flood data
floods = floods[['CZ_NAME_STR', 'BEGIN_DATE', 'EVENT_TYPE', 'DAMAGE_PROPERTY_NUM']]
#floods = floods.drop_duplicates()
print(floods)

currentMonth = 0
currentYear = 0
print("in process")
print(floods.axes)
#floods.drop(11, axis=0, inplace=True)
floodsLength = len(floods)
print("floodsLength")
print(floodsLength)
print("floods.index")
print(len(floods.index))
cleanedFloods = pd.DataFrame(columns=floods.columns)
for i in range(floodsLength):
    previousMonth = currentMonth
    previousYear = currentYear
    currentMonth = floods.BEGIN_DATE.iloc[i].month
    currentYear = floods.BEGIN_DATE.iloc[i].year
    if((currentMonth != previousMonth or currentYear != previousYear) and (currentYear < 2016)):
        if(currentYear == 2015 and currentMonth > 5):
            pass
        else:
            row = floods.iloc[i]
            cleanedFloods = cleanedFloods.append(row, ignore_index=True)

print("Cleaned:")
print(cleanedFloods)