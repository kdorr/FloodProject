####################################################
# dataClean.py
# Authors: Tim Turner, Kim Orr, and Eric Dubinsky
# File Creation Date: April 26
# Upbring Flood Project
# Transposed the foreclosure data to a better format
####################################################
#dataClean.py

import pandas as pd

#prep foreclosure data
fcl = pd.read_csv("ReducedForeclosures.csv")
fclTrans = fcl.transpose()
print(fclTrans.head(n=7))
outFile = "ForeclosuresTransposed.csv"
fclTrans.to_csv(outFile)