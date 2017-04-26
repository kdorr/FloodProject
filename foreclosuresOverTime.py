import pandas as pd
from bokeh.plotting import figure, output_file, show

#Read flood data
floodFile ="C:/Users/Kimberly/Documents/GitHub/FloodProject/dallasFloods.csv"
dateparse = lambda x: pd.datetime.strptime(x, '%m/%d/%Y')
floods = pd.read_csv(floodFile, parse_dates=['BEGIN_DATE'], date_parser=dateparse)

#clean flood data
cleanFloods = floods[['CZ_NAME_STR', 'BEGIN_DATE', 'EVENT_TYPE', 'DAMAGE_PROPERTY_NUM']]
cleanFloods = cleanFloods.drop_duplicates()
#print(cleanFloods.head(n=7))

#read foreclosure data
foreclosureFile = "C:/Users/Kimberly/Documents/ForeclosuresTransposed.csv"
dateparse = lambda x: pd.datetime.strptime(x, '%Y-%m')
foreclosures = pd.read_csv(foreclosureFile, parse_dates=['Date'], date_parser=dateparse)

#create plot
p = figure(x_axis_type="datetime", x_axis_label='dates', y_axis_label='number of foreclosures')

#plot foreclosures
p.line(x=foreclosures['Date'], y=foreclosures['Dallas'], color='green')

#plot floods
for i in range(len(cleanFloods)):
    date = cleanFloods.BEGIN_DATE.iloc[i]
    x=[date,date]
    #locate the y-value of the foreclosures at the time of the flood
    for j in range(len(foreclosures)):
        if(date.month == foreclosures.Date.iloc[j].month and date.year == foreclosures.Date.iloc[j].year):
            fcl = foreclosures.Dallas.iloc[j]
    y=[fcl-1,fcl+1]
    #p.line(x,y, color='green')
    p.circle(x,fcl, color='blue')

#output file and show
output_file("C:/Users/Kimberly/Documents/bokeh2.html")
show(p)