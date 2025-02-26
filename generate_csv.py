import csv
import random
import json
import random_num_generator
import random_date_generator


with open('config.json',  'r') as f:

    data = json.load(f)             


#--------------------------  for the Heading fields-----------------------------------------------------

header_fields = []
for i in data['field_mappings']:
    header_fields += [i['field']]


#-----------------------------  for data fields --------------------------------------------------------

# 1. Store field type and data in the List 
field_type = []
field_data = []

for i in data['field_mappings']:
    field_type += [i['type']]
    field_data += [i['field']]

#2. now storing data in field_data list
total_columns = len(data['field_mappings'])

for i in range(total_columns):
    field_data[i] = []
    if(field_type[i] == 'random'):    
        for j in range(data["field_mappings"][i]["records"]):
            field_data[i] += [random_num_generator.generate_number(data["field_mappings"][i]["length"])]            

    elif(field_type[i] == 'date'):    
        min_date = data["field_mappings"][i]["min_date"]
        max_date = data["field_mappings"][i]["max_date"]
        date_format = data['field_mappings'][i]['format']
        for j in range(data["field_mappings"][i]["records"]):
            field_data[i] += [random_date_generator.generate_date(min_date, max_date,date_format)]

    elif(field_type[i] == 'multiple'):
        for j in range(data['field_mappings'][i]['records']):
            field_merge = ''
            with open(f'./data/{data["folder_name"]}/{data["field_mappings"][i]["file_name"]}','r') as f:
                lines = f.readlines()

                for j in range(data['field_mappings'][i]['merge']):
                    if(len(field_merge) == 0):
                        field_merge += random.choice(lines).strip().upper()
                    else:
                        field_merge += f"{data['field_mappings'][i]['separator']}" + random.choice(lines).strip().upper()
    
            field_data[i] += [field_merge]

    elif(field_type[i] == 'email'):
        domainList = ['@gmail.com', '@yahoo.com']
        num_length = data['field_mappings'][i]['number_length']
        
        for j in range(data['field_mappings'][i]['records']):
            emailList = ''
            with open(f'./data/{data["folder_name"]}/{data["field_mappings"][i]["file_name"]}','r') as f:
                lines = f.readlines()

                if(num_length == 0):
                    emailList += random.choice(lines).strip().lower() + random.choice(domainList)
                else:
                    emailList += random.choice(lines).strip().lower() + str(random_num_generator.generate_number(num_length))+ random.choice(domainList)
            field_data[i] += [emailList]
    
    # elif field_type[i] == 'previous':
    #     name = field_data[0]
    #     if data['field_mappings'][i]['field'] == 'given_name':
    #         field_data[i] = name.split()[0]
    #     else:
    #         field_data[i] = name.split()[1]
        

    else:
        with open(f'./data/{data["folder_name"]}/{data["field_mappings"][i]["file_name"]}','r') as f:
            lines = csv.reader(f)

            for j in lines:
                field_data[i] += j

#-------------------------- for csv generation --------------------------------------------------------

# Method:1 -- More space complexity
with open('csvFile.csv','w',newline="") as f:
    write_rows = csv.writer(f, delimiter=f"{data['delimeter']}")

    header_fields.append('is_registrant')
    header_fields.append('active')
    header_fields.append('company_id')
    header_fields.append('given_name')
    header_fields.append('family_name')

    write_rows.writerows([header_fields])

    n = int(input('no of records: '))

    for i in range(0, n):
        row_data = [random.choice(j) for j in field_data]
        row_data.append('true')
        row_data.append('true')
        row_data.append(1)
        row_data.append(row_data[0].split(' ')[0])
        row_data.append(row_data[0].split(' ')[-1])
        write_rows.writerow(row_data)


# Method:2 -- More time Complexity
# with open('csvFile.csv','w',newline="") as f:
#     write_rows = csv.writer(f, delimiter=f"{data['delimeter']}")

#     write_rows.writerow(header_fields)

#     n = int(input('No. of records: '))

#     for i in range(n):
#         row_data = []
#         for k in range(total_columns):
#             with open(f"./data/{data["folder_name"]}/{data['field_mappings'][k]['file_name']}",'r') as df:

#                 lines = df.readlines()

#                 row_data += [random.choice(lines).strip()]
            
#         write_rows.writerow(row_data)  