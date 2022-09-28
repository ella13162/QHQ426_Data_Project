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
from tui import *
def retrieve_total_number(records):
    return len(records)

def retrieve_rec_serial_number(records, serial_number):
    for j in records:
        if int(j[0]) == serial_number:
            return j
    return -1
def retrieve_observation_date(records, dates):
    record_by_date = dict()
    retrieve_date = []
    for r in records:
        if r[1] in record_by_date:
            record_by_date[r[1]].append(r)
        else:
            record_by_date[r[1]] = [r]
    for d in dates:
        if d in retrieve_date:
            retrieve_date += record_by_date[d]
    return retrieve_date

def retrieve_terytory(records):
    record_by_country = dict()
    for r in records:
        if r[3] in record_by_country:
            record_by_country[r[3]].append(r)
        else:
            record_by_country[r[3]] = [r]
    return record_by_country

def summary_all_records(records):
    record_by_country = retrieve_terytory(records)
    summary_rec = dict()
    for country in record_by_country:
        summary_rec[country] = {"Confirmed": 0, "Deaths": 0, "Recoveries": 0}
    for country in record_by_country:
        count_record = record_by_country[country]
        for r in count_record:
            summary_rec[country]["Confirmed"] += int(r[5])
            summary_rec[country]["Deaths"] += int(r[6])
            summary_rec[country]["Recoveries"] += int(r[7])
    return summary_rec

