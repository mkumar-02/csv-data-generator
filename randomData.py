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

    elif(datafileList[i] == 'name'):
        for j in range(data['fieldmappings'][i]['number']):
            combinedNameList = ''
            with open(f'./Data/Philippines/{datafileList[i]}','r') as f:
                lines = f.readlines()

                for j in range(data['fieldmappings'][i]['combination']):
                    if(len(combinedNameList) == 0):
                        combinedNameList += random.choice(lines).strip()
                    else:
                        combinedNameList += f"{data['fieldmappings'][i]['separater']}" + random.choice(lines).strip()
    
            fieldList[i] += [combinedNameList]
    
    elif(datafileList[i] == 'address'):
        for j in range(data['fieldmappings'][i]['number']):
            combinedAddressList = ''
            with open(f'./Data/Philippines/{datafileList[i]}','r') as f:
                lines = f.readlines()

                for j in range(data['fieldmappings'][i]['combination']):
                    if(len(combinedAddressList) == 0):
                        combinedAddressList += random.choice(lines).strip()
                    else:
                        combinedAddressList += f"{data['fieldmappings'][i]['separater']}" + random.choice(lines).strip()
    
            fieldList[i] += [combinedAddressList]

    elif(datafileList[i] == 'email'):
        domainList = ['gmail.com', 'yahoo.com']
        for j in range(data['fieldmappings'][i]['number']):
            emailList = ''
            with open('./Data/Philippines/name','r') as f:
                lines = f.readlines()

                emailList += random.choice(lines).strip().lower() + str(randomInt.randD_digit(4))+ random.choice(domainList)
        
            fieldList[i] += [emailList]

    else:
        with open(f'./Data/Philippines/{datafileList[i]}','r') as f:
            lines = csv.reader(f)

            for j in lines:
                fieldList[i] += j

            if(datafileList[i] == 'name'):
                index = i



#-------------------------- for csv generation --------------------------------------------------------

# Method:1 -- More space complexity
with open('csvFile.csv','w',newline="") as f:
    thewriter = csv.writer(f, delimiter=f"{data['delimeter']}")

    thewriter.writerows([headerfields])

    n = int(input('No. of records: '))

    for i in range(0, n):
        row_data = [random.choice(j) for j in fieldList]
        thewriter.writerow(row_data)


# Method:2 -- More time Complexity
# with open('csvFile.csv','w',newline="") as f:
#     thewriter = csv.writer(f, delimiter=f"{data['delimeter']}")

#     thewriter.writerow(headerfields)

#     n = int(input('No. of records: '))

#     for i in range(n):
#         row_data = []
#         for k in range(totalcolumns):
#             with open(f"./Data/Philippines/{data['fieldmappings'][k]['type']}",'r') as df:

#                 lines = df.readlines()

#                 row_data += [random.choice(lines).strip()]
            
#         thewriter.writerow(row_data)  