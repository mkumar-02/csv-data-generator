# csv-data-generator

## Overview

This repository will generate a csv file. In this you will get the desired columns by modifying the `config.json` file.

## Getting Started

Run this command `python generate_csv.py`

Then it will be asking for number of rows you need.

## How to modify `config.json`
The json file has different `key=value` pairs.

JSON file has three main parameters:
  1. folder_name
  3. delimeter
  4. field_mappings
 
 In `folder_name` pass name of folder that contains data in the text file. <br>
 In `delimeter` pass separation symbol between the columns. <br>
 In `field_mappings` pass columns that you require in csv file. <br>
 
 So, in field_mappings parameter we are passing all the fields in the list collection that contains the attribute according to the fields. <br>
 
 Scenarios of adding a new column in the csv file: <br>
 1. Having data in text file and selecting only one record 
            
        In this case you need to pass the following attributes: 
            a. field - name of the field
            b. file_name 
            c. type - "given"
    
 2. Having data in text file and taking combination of more than one record

        In this case you need to pass the following attributes: 
            a. field 
            b. type - "multiple" 
            c. file_name
            d. merge - combination of how much data fields
            e. separator - separation between the merged fields
            d. records - how many random number of records should be used in generating the csv file.
    
 3. Column to display number
    
        In this case you need to pass the following attributes: 
            a. field 
            b. type - "random" (because this field will randomly generate data according to the mentioned attributes)
            c. length 
            d. records 
            
 4. Column to display date

        In this case you need to pass the following attributes: 
            a. field 
            b. type - "date"
            c. format
            d. min_date 
            e. max_date
            f. records
    
 5. Column to display email
  
        In this case you need to pass the following attributes: 
            a. field 
            b. file_name 
            b. type - "email"
            c. number_length
            d. records
      
            

## Example of output data
      language|vid|fullname|gender|dob|phoneNo|email|address|street|city|region|province|postalcode
      Eng|6424757105976953|Aira john|Male|13-02-2021|5817421774|nathalie323@gmail.com|Marawi mabitac|E. Rodriguez Sr. Ave|Bangar|Region XII|SCO|606265
      Eng|2633815014374861|Adrian grace|Female|16-06-2020|3899197995|trisha775@yahoo.com|Kayapa alcantara|Sunrise Hill|Cortes|Region V|ILI|761120
      Eng|5436587900834912|Vee kyle|Other|16-11-2020|3072570664|raven836@yahoo.com|Magsingal mulanay|Rosario Drive|Lantawan|Region VI|ILN|225892
      Eng|9597378958128663|Jennly nick|Female|13-02-2021|6637663594|jhoshcliff676@yahoo.com|Mati las pi�as|La Florilla|Agdangan|Region III|NER|863364
      Eng|5970078333516378|Genesis jericho|Other|19-03-2020|4936857785|rey167@gmail.com|Initao tiaong|Balete Dr|Vincenzo A. Sagun|Region I|SUR|682602

    
## Performance
Using an `Intel Core i5` for the tests, I got the following results:<br>

    1M rows in 15 seconds
    10M rows in 2 minutes
    100M rows in 19 minutes
