# * The total number of months included in the dataset

#  * The net total amount of "Profit/Losses" over the entire period

#  * The average of the changes in "Profit/Losses" over the entire period

#  * The greatest increase in profits (date and amount) over the entire period

#  * The greatest decrease in losses (date and amount) over the entire period

import csv
import os

month_list = []
month_count = 0
net_profit = 0

#Read store relative path of csv for portability.
curr_dir = os.getcwd()
csvpath = os.path.join(curr_dir, "Resources")
os.chdir(csvpath)

with open("budget_data.csv") as data_file:
    next(data_file) #Skip header row
    data_rows = csv.reader(data_file, delimiter = ',')

    greatest_profit = 0
    greatest_loss = 0

    for row in data_rows:
        #Count months by accummulating them into a list (checks for duplicates)
        if row[0] not in month_list:
            month_list.append(row[0])
            month_count += 1
        #Accummulate net profit
        net_profit = net_profit + int(row[1])
        if int(row[1]) > int(greatest_profit):
            greatest_profit = row[1]
            greatest_profit_info = [row[0], row[1]]
        elif int(row[1]) < int(greatest_loss):
            greatest_loss = row[1]
            greatest_loss_info = [row[0], row[1]]


#Print number of months in dataset
print(f"Total months: {str(month_count)}")
#Print net profit
print(f"Net profit: {str(net_profit)}")
#Print average change
print(f"Average change: {str(net_profit / month_count)}")
#Print greatest increase in profit
print(f"Greatest increase in profit: {greatest_profit_info[1]} on {greatest_profit_info[0]}")
#Print greatest decrease in profit
print(f"Greatest decrease inprofit: {greatest_loss_info[1]} on {greatest_loss_info[0]}")


