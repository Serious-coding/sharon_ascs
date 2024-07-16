#1. Mathematical Expressions On Series
import pandas  as pd
import numpy as np
section = ['A','B','C','D','E']
contri1 = np.array([6700,5600,5000,5200,np.NaN])
s12 = pd.Series(data = contri1*2, index = section, dtype = np.float32)
print(s12)

#2. Using "arange function in series"
ran = np.arange(53,87,4)
ser = pd.Series(ran)
print(ser)

#3. Using Tile Function In Series
ti = np.tile(['\"Punctuality Is The Key To Success\"'],3)
si1 = pd.Series(ti)
print(si1)

#4. Mathematical operation(Addition) on Series
c11 = pd.Series([30,40,50], index = ['Science','Commerce','Humanities'])
c12 = pd.Series([37,44,45], index = ['Science','Commerce','Humanities'])
print('Total no. of students')
print(c11+c12)

#5. 
population = pd.Series([127986 , 191836 , 412392 , 28063],\
index = ['Delhi', 'Mumbai', 'Kolkata', 'Chennai'])
AvgIncome = pd.Series([10000 , 12000 , 20000 , 15000],\
index = ['Delhi','Mumbai','Kolkata','Chennai'])
perCapita = AvgIncome/population
print('Population in four metro cities')
print(population)
print('Average income in four metro cities')
print(AvgIncome)
print('Per Capita Income in four metro cities')
print(perCapita)
