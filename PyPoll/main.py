#This program takes a csv file of election results as input
#and returns a summary report. The input file should have a header
#row and include voter ID and candidate name. The program loops 
#through the file to count the number of votes and enumerate 
#the candidates. Next, the program loops through each of the 
#candidates and tallies the number of votes each received to 
#determine the winner. A report is printed to a csv file called 
#election_results, located in the Analysis folder.

import csv
import os

#Function to reset csv reader to start of data
def reset_csv(data_file):
    data_file.seek(0)
    header_row = next(data_file)
    data_rows = csv.reader(data_file, delimiter = ',')
    return data_rows

#Store relative path to csv
#curr_dir = os.getcwd()
csvpath = os.path.join("Resources", "election_data.csv")

#Initialize variables
total_vote_count = 0
candidate_list = []
candidate_vote_count = 0
highest_vote_count = 0
winner_name = ""
report = ""

#Open and read file, printing header row
with open(csvpath, "r") as data_file:
    next(data_file)
    data_rows = csv.reader(data_file, delimiter = ',')
        
    #Loop through dataset to count total number of votes cast 
    #and print list of candidates
    for row in data_rows:
        total_vote_count += 1
        if row[2] not in candidate_list:
            candidate_list.append(row[2])
    
    #Save election results to formatted report for later output (Part I)
    report = f"\n    Election results \n*************************"\
    f"\nTotal votes cast: {total_vote_count} \n*************************"

    data_rows = reset_csv(data_file)
    #Print votes and percentage of votes for each candidate,
    #then compute winner.
    for candidate in candidate_list:
        for row in data_rows:
            if row[2] == candidate:
                candidate_vote_count +=1
        percent_votes = round(candidate_vote_count / total_vote_count * 100, 3)
        #Append election results to report for later output (Part II)
        report = report + f"\n{candidate:9} {percent_votes}% {candidate_vote_count}"
        if candidate_vote_count > highest_vote_count:
            highest_vote_count = candidate_vote_count
            winner_name = candidate
        candidate_vote_count = 0
        data_rows = reset_csv(data_file)

#Append election results to report for later output (Part III)
report = report + f"\n************************* \nWinner: {winner_name}"
f"\n*************************"

#Print report to terminal and csv file
print(report)
output_directory = "Analysis"
os.chdir(output_directory)
with open('election_results.csv', 'w', newline='') as output_file:
    output_file.write(report)