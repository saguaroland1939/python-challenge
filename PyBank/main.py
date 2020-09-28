#This program takes a csv file of financial data as input and produces
#a statistical report stored to a csv file and printed to the terminal.
#The input file must contain a series of months with corresponding profits
#and losses. The output report includes the total number of months analyzed,
#the net total amount of "Profit/Losses" over the entire period, the average
#of the changes in "Profit/Losses" over the entire period, and the greatest
#increase and greatest decrease in profits (date and amount) over the entire
#period.

import csv
import os

month_list = []
month_count = 0
net_profit = 0
greatest_profit = 0
greatest_loss = 0

#Store relative path of csv
csvpath = "Resources/budget_data.csv"

#Open csv file, skipping over header row
with open(csvpath) as data_file:
    next(data_file)
    data_rows = csv.reader(data_file, delimiter = ',')

    #Loop through csv
    for row in data_rows:
        #Count months by accummulating them into a list (ommit any duplicates)
        if row[0] not in month_list:
            month_list.append(row[0])
            month_count += 1
        #Accummulate net profit
        net_profit = net_profit + int(row[1])
        #As greater profits are found, replace current greatest
        if int(row[1]) > greatest_profit:
            greatest_profit = int(row[1])
            greatest_profit_info = [row[0], row[1]]
        #As greater losses are found, replace current greatest
        elif int(row[1]) < greatest_loss:
            greatest_loss = int(row[1])
            greatest_loss_info = [row[0], row[1]]

#Organize results into formatted report
report = f"Total months: {str(month_count)}"\
f"\nNet profit: {str(net_profit)}"\
f"\nAverage change: {round(net_profit / month_count, 2)}"\
f"\nGreatest increase in profit: {greatest_profit_info[1]} on {greatest_profit_info[0]}"\
f"\nGreatest decrease inprofit: {greatest_loss_info[1]} on {greatest_loss_info[0]}"

#Print report to terminal and new csv file
print(report)
output_directory = "Analysis"
os.chdir(output_directory)
with open('banking_results.csv', 'w', newline='') as output_file:
    output_file.write(report)