import pandas as pd
import os
import csv
from haversine import haversine, Unit

# Excel file name:
dir = 'files'
excelFilex = os.path.join(dir, 'haversine.xlsx')
excelFile = pd.read_excel(excelFilex)
#Converting excel file to csv
excelFile.to_csv('datas.csv',index = None, header=True)
#Latitudes and Longitudes columns locations in excel file. (First col is = 0)
df = pd.read_csv("datas.csv", usecols=[3,4])

#Column names of Lat and Longs
latColumnName = 'Latitude (N)'
longColumnName =  'Longitude (E)'


length = df.shape[0]

with open('subset.csv', 'w', newline='') as f:
    fieldnames =['start','end','Lat1','Long1','Lat2','Long2','value']
    thewriter = csv.DictWriter(f, fieldnames=fieldnames)
    thewriter.writeheader()
    for i in range(length):
        for j in range(length):
            lat1 = df[latColumnName].values[i]
            long1 = df[longColumnName].values[i]
            lat2=  df[latColumnName].values[j]
            long2= df[longColumnName].values[j]
            location_1 =(lat1,long1 )
            location_2 = (lat2, long2 )
            thewriter.writerow({'start' : i, 'end' : j, 'Lat1' : lat1, 'Long1' : long1, 'Lat2' : lat2, 'Long2' : long2, 'value' : haversine(location_1,location_2, unit=Unit.KILOMETERS)})


with open('sequence.csv', 'w', newline='') as f:
    fieldnames =['start','end','Lat1','Long1','Lat2','Long2','value']
    thewriter = csv.DictWriter(f, fieldnames=fieldnames)
    thewriter.writeheader()
    for i in range(length):

        if not i == (length-1):
            lat1= df[latColumnName].values[i]
            long1= df[longColumnName].values[i]
            lat2= df[latColumnName].values[i+1]
            long2= df[longColumnName].values[i+1]
            location_1 =(lat1,long1)
            location_2 = (lat2, long2)
            thewriter.writerow({'start' : i, 'end' : i+1, 'Lat1' : lat1, 'Long1' : long1, 'Lat2' : lat2, 'Long2' : long2, 'value' : haversine(location_1,location_2, unit=Unit.KILOMETERS)})
        else:
            print("Sequence File Created")