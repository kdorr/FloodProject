import pandas as pd

#prep foreclosure data
fcl = pd.read_csv("C:/Users/Kimberly/Documents/GitHub/FloodProject/TestForeclosures.csv")
fclTrans = fcl.transpose()
print(fclTrans.head(n=7))
outFile = "C:/Users/Kimberly/Documents/ForeclosuresTransposed.csv"
fclTrans.to_csv(outFile)