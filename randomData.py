import csv
import random
import json
import randomInt
import dateGenerator


with open('config.json',  'r') as f:

    data = json.load(f)             # returns JSON object as a dictionary
    # print(data)

#--------------------------  for the Heading fields-----------------------------------------------------

headerfields = []
for i in data['fieldmappings']:
    headerfields += [i['outputname']]


#-----------------------------  for data fields --------------------------------------------------------

# 1. Storing the files name and field name in the List 
datafileList = []
fieldList = []
for i in data['fieldmappings']:
    datafileList += [i['type']]
    fieldList += [i['field']]

# print(datafileList)
# print(fieldList)

#2. Now reading the data file separately
totalcolumns = len(data['fieldmappings'])

for i in range(0,totalcolumns):
    fieldList[i] = []

    if(datafileList[i] == 'random'):    
        # print(data["fieldmappings"][i])
        for j in range(data["fieldmappings"][i]["number"]):
            fieldList[i] += [randomInt.randD_digit(data["fieldmappings"][i]["digit"])]            

    elif(datafileList[i] == 'date'):    
        # print(data["fieldmappings"][i])
        minDate = data["fieldmappings"][i]["min_date"]
        maxDate = data["fieldmappings"][i]["max_date"]
        for j in range(data["fieldmappings"][i]["number"]):
            fieldList[i] += [dateGenerator.dateGenerate(minDate, maxDate)]

    else:
        with open(f'./Data/Philippines/{datafileList[i]}.txt','r') as f:
            lines = csv.reader(f)

            for j in lines:
                fieldList[i] += j

            if(datafileList[i] == 'name'):
                index = i



#-------------------------- for csv generation --------------------------------------------------------

with open('csvFile.csv','w',newline="") as f:
    thewriter = csv.writer(f, delimiter=f"{data['delimeter']}")

    thewriter.writerows([headerfields])

    n = int(input('No. of records: '))

    for i in range(0, n):
        row_data = [random.choice(j) for j in fieldList]
        thewriter.writerow(row_data)
