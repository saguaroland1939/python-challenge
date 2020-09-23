# * The total number of months included in the dataset

#  * The net total amount of "Profit/Losses" over the entire period

#  * The average of the changes in "Profit/Losses" over the entire period

#  * The greatest increase in profits (date and amount) over the entire period

#  * The greatest decrease in losses (date and amount) over the entire period

import csv
import os

month_list = []
month_count = 0

#Read store relative path of csv for portability.
curr_dir = os.getcwd()
csvpath = os.path.join(curr_dir, "Resources")
os.chdir(csvpath)

with open("budget_data.csv") as datafile:
    next(datafile) #Skip header row
    data_rows = csv.reader(datafile, delimiter = ',')
    for row in data_rows:
        #Accummulate list of unique months
        if row[0] not in month_list:
            month_list.append(row[0])
            month_count += 1
#Print number of months in dataset
print(str(month_count))