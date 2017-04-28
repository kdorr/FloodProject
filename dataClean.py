import pandas as pd

#prep foreclosure data
fcl = pd.read_csv("TestForeclosures.csv")
fclTrans = fcl.transpose()
print(fclTrans.head(n=7))
outFile = "ForeclosuresTransposed.csv"
fclTrans.to_csv(outFile)