import pandas as pd

excelFile = pd.read_excel("haversine.xlsx")
excelFile.to_csv('datas.csv',index = None, header=True)
df = pd.read_csv("datas.csv", usecols=[3,4,6,7,8,9])
print(df)
#dataFrame =pd.DataFrame(excelFile)
#print(dataFrame)
#excelFile.get_value(3, 4)