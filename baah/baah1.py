import pandas as pd
import numpy as np

#print(np.median(pd.read_csv('WalmartSales.csv')['Weekly_Sales']))
#mean = 15981.25812346704
#median = 7612.03

#print(np.min(pd.read_csv('WalmartSales.csv')['Weekly_Sales']))
#-4988.94
#print(np.max(pd.read_csv('WalmartSales.csv')['Weekly_Sales']))
#693099.36
#print(np.var(pd.read_csv('WalmartSales.csv')['Weekly_Sales']))
#515796633.3245972
#print(np.std(pd.read_csv('WalmartSales.csv')['Weekly_Sales']))
#22711.156582714964

ws = pd.read_csv('WalmartSales.csv')

#print(ws.keys())
#Index(['Store', 'Dept', 'Date', 'Weekly_Sales', 'IsHoliday'], dtype='object')

#stores = pd.read_csv('WalmartSales.csv')['Store']
dep = 1
y = 0
leng = 0
for x in ws.values:
    #print(x[0])
    if x[0] == dep:
        leng += 1
        y += x[3]
avg = y / leng
#print(avg)
        