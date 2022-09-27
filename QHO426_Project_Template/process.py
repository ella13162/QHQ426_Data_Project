"""
This module is responsible for processing the data.  Each function in this module will take a list of records,
process it and return the desired result.
"""

"""
Task 16 - 20: Write suitable functions to process the data.

Each of the functions below should follow the pattern:
- Take a list of records (where each record is a list of data values) as a parameter.
- Process the list of records appropriately.  You may use the module 'tui' to retrieve any additional information 
required from the user to complete the processing.
- Return a suitable result

The required functions are as follows:
- Retrieve the total number of records that have been loaded.
- Retrieve a record with the serial number as specified by the user.
- Retrieve the records for the observation dates as specified by the user.
- Retrieve all of the records grouped by the country/region.
- Retrieve a summary of all of the records. This should include the following information for each country/region:
    - the total number of confirmed cases
    - the total number of deaths
    - the total number of recoveries

 
"""
import csv
from tui import *
record = {"Serial Number":[], "Province/ State":[], "Country":[], "Last Update":[], "Confirmed":[],"Deaths":[], "Recovered":[]}
with open("covid19_dataset.csv") as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)
    for cols in csv_reader:
        if cols[0] != "" and cols[1] != "" and cols[2] != "" and cols[3] != "" and cols[4] != "" and cols[5] != "" and cols[6] != "":
            record["Serial Number"].append(cols[0].strip())
            record["Province/ State"].append(cols[1].strip())
            record["Country"].append(cols[2].strip())
            record["Last Update"].append(cols[3].strip())
            record["Confirmed"].append(cols[4].strip())
            record["Deaths"].append(cols[5].strip())
            record["Recovered"].append(cols[6].strip())
print(total_records())
print("Confirmed cases: ")
with open("covid19_dataset.csv") as csv_file:
    confirmed_cases = 0
    csv_reader = csv.reader(csv_file)
    for cols in csv_reader:
        print(cols[4])
        cols =+ int(cols.read)



# TODO: Your code here
