"""
This module is responsible for visualising the data using Matplotlib.
"""

"""
Task 22 - 24: Write suitable functions to visualise the data as follows:

- Display the number of confirmed cases per country/region using a pie chart
- Display the top 5 countries for deaths using a bar chart
- Display a suitable (animated) visualisation to show how the number of confirmed cases, deaths and recovery change over
time. This could focus on a specific country or countries.

Each function should visualise the data using Matplotlib.
"""

# TODO: Your code here
import matplotlib.pyplot as plt
import csv
from tui import *
def pie_chart(summary):
    countries = []
    confirmed_cases = []
    for country in summary:
        countries.append(country)
        confirmed_cases.append(summary[country]["confirmed"])
    plt.pie(confirmed_cases, label=countries)
    plt.show()
def bar_chart(summary):
    death_list = []
    for country in summary:
        death_list.append((summary[country]["deaths"], country))
    death_list = sorted(death_list, reverse=True)
    tmp_list = death_list[:5]
    x = [tmp_list[j][0] for j in range(5)]
    y = [tmp_list[j][1] for j in range(5)]
    plt.bar(x,y)
    plt.show()

        