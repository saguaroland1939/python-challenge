# * The total number of months included in the dataset

#  * The net total amount of "Profit/Losses" over the entire period

#  * The average of the changes in "Profit/Losses" over the entire period

#  * The greatest increase in profits (date and amount) over the entire period

#  * The greatest decrease in losses (date and amount) over the entire period

import csv
import os

month_list = []
i=0

#Read store relative path of csv for portability.
curr_dir = os.getcwd()
csvpath = os.path.join(curr_dir, "Resources")
os.chdir(csvpath)

with open("budget_data.csv") as datafile:
    next(datafile) #Skip header row
    data_rows = csv.reader(datafile, delimiter = ',')
    for row in data_rows:
        #print(row[0] + " " + row[1])
        if row[0] not in month_list:
            month_list[1] = row[1]
            print("sdaf")
            i+=1
        