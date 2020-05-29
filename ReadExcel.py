import pandas as pd
from haversine import haversine, Unit

excelFile = pd.read_excel("haversine.xlsx")
excelFile.to_csv('datas.csv',index = None, header=True)
df = pd.read_csv("datas.csv", usecols=[3,4])
paris =(df['Latitude (N)'].values[4], df['Longitude (E)'].values[4])
istanbul = (df['Latitude (N)'].values[5], df['Longitude (E)'].values[5])

print(haversine(paris,istanbul, unit=Unit.MILES))
print(df.shape[0])