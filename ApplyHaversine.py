import pandas as pd
import csv
from haversine import haversine, Unit

#Okunacak Excel Adı:
excelFile = pd.read_excel("haversine.xlsx")
#Excel csv dosyasına dönüştürülüyor
excelFile.to_csv('datas.csv',index = None, header=True)
#Excel dosyasındaki lat ve long konumlarunı usecols'daki değerler içinde belirtin. Saymaya 0'dan başlayın
df = pd.read_csv("datas.csv", usecols=[3,4])


length = df.shape[0]

with open('subset.csv', 'w', newline='') as f:
    fieldnames =['start','end','value']
    thewriter = csv.DictWriter(f, fieldnames=fieldnames)
    thewriter.writeheader()
    for i in range(length):
        for j in range(length):
            location_1 =(df['Latitude (N)'].values[i], df['Longitude (E)'].values[i])
            location_2 = (df['Latitude (N)'].values[j], df['Longitude (E)'].values[j])
            thewriter.writerow({'start' : i, 'end' : j, 'value' : haversine(location_1,location_2, unit=Unit.KILOMETERS)})


with open('sequence.csv', 'w', newline='') as f:
    fieldnames =['start','end','value']
    thewriter = csv.DictWriter(f, fieldnames=fieldnames)
    thewriter.writeheader()
    for i in range(length):

        if not i == (length-1):
            paris =(df['Latitude (N)'].values[i], df['Longitude (E)'].values[i])
            istanbul = (df['Latitude (N)'].values[i+1], df['Longitude (E)'].values[i+1])
            thewriter.writerow({'start' : i, 'end' : i+1, 'value' : haversine(paris,istanbul, unit=Unit.KILOMETERS)})
        else:
            print("Sequence File Created")