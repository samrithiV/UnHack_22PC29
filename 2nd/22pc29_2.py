import csv
import pandas as pd
import math
from csv import writer

metaFile = 'D:\\UnHack 22PC29\\2nd\\metadata.csv'
careFile = 'D:\\UnHack 22PC29\\2nd\\CareAreas.csv'
metaData = []
careAreas = []
with open(metaFile,'r') as file:
    csv_Reader = csv.reader(file)
    for rows in csv_Reader:
        metaData.append(rows)

mainFieldSize = float(metaData[1][0])
subFieldSize = float(metaData[1][1])

with open(careFile,'r') as file:
    csvReader = csv.reader(file)
    for rows in csvReader:
        careAreas.append(rows[:])

mainFields = []
subFields = []
subFieldCount = 0
mainFieldCount = 0
sx1 = 0
sy1 = 0


for careArea in careAreas:
    x1,x2,y1,y2 = float(careArea[1]),float(careArea[2]),float(careArea[3]),float(careArea[4])
    sx1, sy1 = x1 , y1
    if careArea == careAreas[0]:
        #placing the 1st Main Field on the x1,y1 of 1st Care area
        x1,x2,y1,y2 = float(careAreas[0][1]),float(careAreas[0][2]),float(careAreas[0][3]),float(careAreas[0][4])
        mainField = [mainFieldCount,0,0,0,0]
        mainField[1],mainField[3] = x1, y1
        mainField[2], mainField[4] = mainField[1] + mainFieldSize, mainField[3] + mainFieldSize
        mainFields.append(mainField)  
        mainFieldCount+=1

    elif (x2 > mainField[2] and x1 > mainField[2]) or (y2 > mainField[4] and y1 > mainField[4]): #Care area lies outside the MainField
        mainField = [0,0,0,0,0]
        mainField[0] = mainFieldCount
        mainFieldCount += 1
        mainField[1], mainField[3] = x1, y1
        mainField[2], mainField[4] = x1 + mainFieldSize, y1 + mainFieldSize
        mainFields.append(mainField)

    elif x2 > mainField[2]:
        pass
    for i in range(math.ceil((y2-y1)/subFieldSize)): 
        while sx1 < x2: #checking if each row is scanned till the last column
            subField = [subFieldCount, sx1 , sx1 + subFieldSize, sy1 , sy1 + subFieldSize, mainFieldCount - 1 ]
            subFieldCount += 1
            sx1= subField[2]
            subFields.append(subField)
        sx1 = x1 
        sy1 = subFields[-1][4]  

                
with open('D:\\UnHack 22PC29\\2nd\\mainField.csv','w+',newline='') as file:
    writer_obj = writer(file)
    writer_obj.writerows(mainFields)

with open('D:\\UnHack 22PC29\\2nd\\subField.csv','w+',newline='') as file:
    writer_obj = writer(file)
    writer_obj.writerows(subFields)