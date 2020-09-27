import csv
import os

#Function to reset csv reader to start of data
def reset_csv(data_file):
    data_file.seek(0)
    header_row = next(data_file)
    data_rows = csv.reader(data_file, delimiter = ',')
    return data_rows

#Store relative path to csv
curr_dir = os.getcwd()
csvpath = os.path.join(curr_dir, "Resources", "election_data.csv")

#Initialize variables
total_vote_count = 0
candidate_list = []
candidate_vote_count = 0
highest_vote_count = 0
winner_name = ""

#Open and read file, printing header row
with open(csvpath, "r") as data_file:
    header_row = next(data_file)
    print(header_row)
    data_rows = csv.reader(data_file, delimiter = ',')
        
    #Loop through dataset to count total number of votes cast and print list of candidates
    for row in data_rows:
        total_vote_count += 1
        if row[2] not in candidate_list:
            candidate_list.append(row[2])

    #Print election results to terminal (Part I)
    print("Election results")
    print("****************************************")
    print(f"Total votes cast: {total_vote_count}")
    print("****************************************")

    #Compare each candidate in data file with each candidate in list of candidates to tally each candidate's votesCompute percentage of votes won by each candidate and compute the winner
    data_rows = reset_csv(data_file)
    for candidate in candidate_list:
        for row in data_rows:
            if row[2] == candidate:
                candidate_vote_count +=1
        percent_votes = round(candidate_vote_count / total_vote_count * 100, 3)
        print(f"{candidate:9} {percent_votes}% ({candidate_vote_count})")
        
        if candidate_vote_count > highest_vote_count:
            highest_vote_count = candidate_vote_count
            winner_name = candidate
        candidate_vote_count = 0
        data_rows = reset_csv(data_file)
#Print election results to a csv file
#setwd("Analysis")
#with open('election_results.csv', 'w', newline='') as file:

#Print election results to terminal (Part II)
print("****************************************")
print(f"Winner: {winner_name}")
print("****************************************")