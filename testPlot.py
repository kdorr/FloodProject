import normalizedPlot as normal
from bokeh.plotting import figure, output_file, show
import statsmodels.api as sm

plt = figure(x_axis_label='months since flood', y_axis_label='change number of foreclosures since flood')
allXs=normal.allXs
allYs=normal.allYs
testXs=allXs[0:18]
testYs=allYs[0:18]
results=normal.resultsList
print(results[0].summary())
regY=[]
#getY = lambda r: -0.0348*r + 0.1834
print(results[0])
print(results[0].params)
print(len(results))
for i in range(len(results)):
    print(i)
    getY = lambda res: (results[i].params[0] * res) + results[i].params[1]
    for j in range(len(testXs)):
        regY.append(getY(j))
plt.line(allXs, regY)

finalReg=0
for i in (regY):
    finalReg=regY[i]+finalReg
finalReg=finalReg/len(regY)
print(finalReg)



show(plt)

