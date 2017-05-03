import normalizedPlot as normal
from bokeh.plotting import figure, output_file, show
import statsmodels.api as sm

p = figure(x_axis_label='months since flood', y_axis_label='change number of foreclosures since flood')
allXs=normal.allXs
allYs=normal.allYs
testXs=allXs[0:18]
testYs=allYs[0:18]
results=normal.resultsList
print(results[0].summary())
p.circle(testXs,testYs)
regY=[]
getY = lambda r: -0.0348*r + 0.1834
for i in range(len(testXs)):
    regY.append(getY(i))
p.line(testXs, regY)
show(p)

