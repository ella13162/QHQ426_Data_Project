"""
TUI is short for Text-User Interface. This module is responsible for communicating with the user.
The functions in this module will display information to the user and/or retrieve a response from the user.
Each function in this module should utilise any parameters and perform user input/output.
A function may also need to format and/or structure a response e.g. return a list, tuple, etc.
Any errors or invalid inputs should be handled appropriately.
Please note that you do not need to read the data file or perform any other such processing in this module.
"""
import csv


def welcome():

    print("", "-" * 24, "\n WELCOME TO COVID-19 DATA\n", "-" * 24)


def error(msg):

    print("Display an error message")
    error_msg = input()
    print("Error!", f"{error_msg}""!")
    return


def progress(operation, value):

    print("Enter the percentage of the operation: ")
    value = int(input())
    if (value == 0):
        operation = "has started."

    elif (value < 100) and (value > 0):
        operation = "in progress."

    else:
        operation = "has completed."

    print("Operation status {}".format(operation))
    return


def menu(variant=0):
    print("Choose variant from the following: \n0 - Data centre\n1 - Records and data observation")
    print("2 - Data charts\n3 - All data or specific Region data\n")
    variant = int(input("Your variant: "))
    if variant == 0:
        print("To display menu press number from the following:")
        print("[1] Process Data\n[2] Visualise Data\n[3] Export Data\n[4] Exit")
        opt = int(input("Your option: "))
        if opt in [1, 2, 3]:
            return opt

    elif variant == 1:
        print("To display menu press number from the following:")
        print("[1] Record by Serial Number\n[2] Records by Observation Date")
        print("[3] Group Records by Country/Region\n[4] Summarise Records")
        opt = int(input("Your option: "))
        if opt in [1, 2, 3, 4]:
            return opt
    elif variant == 2:
        print("To display menu press number from the following:")
        print("[1] Country/Region Pie Chart\n[2] Observations Chart\n[3] Animated Summary")
        opt = int(input("Your option: "))
        if opt in [1, 2, 3]:
            return opt
    elif variant == 3:
        print("To display menu press number from the following:")
        print("[1] All Data\n[2] Data for Specific Country/Region")
        opt = int(input("Your option: "))
        if opt in [1, 2]:
            return opt
    else:
        print("Error! Incorrect option pressed, try again!")
    if variant in [0, 1, 2, 3]:
        return variant


def total_records(num_records):

    with open('covid19_dataset.csv') as csv_file:
        num_records = 0
        csv_reader = csv.reader(csv_file)
        for rows in csv_reader:
            num_records += 1
            #print(num_records)
        print(f"There are {num_records} records in the data set.")
    return


def serial_number():

    # TODO: Your code here
    #data =[]
    print("Enter serial number: ")
    serial_numb = int(input())
    #for record in data:
        #if serial_numb == record[0]:
            #print(record)
    #print(serial_numb)
    return serial_numb


def observation_dates():

    status = True
    dates = []
    while status == True:
        print("Print observation data in format dd/mm/yyyy: ")
        ex_data = str(input())
        dates.append(ex_data)
        print("Do you like to proceed the action? ")
        print("Enter y for ""Yes"" to continue, and n for ""No"" to end the process")
        answer = input()
        if answer.lower() == 'y':
            status = True
            print(status)
            print(dates)
        elif answer.lower() == 'n':
            print(ex_data)
            status = False
    print(dates)
    return dates


def display_record(record, cols=None):

    # TODO: Your code here
    if cols is None or len(cols) == 0:
        print(record)
    else:
        tmp_record = list(record[i] for i in cols)
        print(tmp_record)


def display_records(record, cols = None):
    """
    Task 9: Display each record in the specified list of records.
    Only the data for the specified column indexes will be displayed.
    If no column indexes have been specified, then all the data for a record will be displayed.

    The function should have two parameters as follows:

    records     which is a list of records where each record itself is a list of data values.
    cols        this is a list of integer values that represent column indexes.
                the default value for this is None.

    You will need to add these parameters to the function definition.

    The function should iterate through each record in records and display the record.

    Each record should be displayed as a list of values e.g. [1,01/22/2020,Anhui,Mainland China,1/22/2020 17:00,1,0,0]
    Only the columns whose indexes are included in cols should be displayed for each record.

    If cols is an empty list or None then all values for the record should be displayed.

    :param records: A list of records
    :param cols: A list of integer values that represent column indexes
    :return: Does not return anything
    """
    # TODO: Your code here
    records = []
    for record in records:
        display_record(record, cols)

def country_name(countries):
    print("Enter country name among belows:")
    for country in countries:
        print(country)
    while True:
        name = input("Enter Country Name: ")
        name = name.strip(' ')
        if name in countries:
            return name
        else:
            error("Wrong country name entered! Please, Try again.")

def display_by_country(records_by_countries, cols=None):
    for country in records_by_countries:
        print(f"Country: {country}")
        display_records(records_by_countries[country], cols)

def display_summary(summary):
    for country in summary:
        print(
            f"Country:{country} , Confirmed:{summary[country]['confirmed']} , Deaths:{summary[country]['deaths']} , Recoveries:{summary[country]['recoveries']}")


