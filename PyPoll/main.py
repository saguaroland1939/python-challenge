import csv
import os

#Store relative path to csv
curr_dir = os.getcwd()
csvpath = os.path.join(curr_dir, "Resources", "election_data.csv")

total_vote_count = 0
candidate_list = []
candidate_vote_count = 0
highest_vote_count = 0
winner_name = ""

#Read file
with open(csvpath, "r") as data_file:
    header_row = next(data_file) #Skip header row
    print(header_row)
    subset = [next(data_file) for x in range(1000)]
    data_rows = csv.reader(subset, delimiter = ',')
    #Create list of candidates
    for row in data_rows:
        total_vote_count += 1
        if row[2] not in candidate_list:
            candidate_list.append(row[2])
    #Compute percentage of votes won by each candidate and computer winner
    for candidate in candidate_list:
        for row in data_rows:
            if row[2] == candidate:
                candidate_vote_count +=1
        print(candidate_vote_count)
        percent_votes = candidate_vote_count / total_vote_count
        if candidate_vote_count > highest_vote_count:
            highest_vote_count = candidate_vote_count
            winner_name = candidate

#Print election results to a csv file
#setwd("Analysis")
#with open('election_results.csv', 'w', newline='') as file:

#Print election results to terminal
print("Election results")
print("****************************************")
print(f"Total votes cast: {total_vote_count}")
print("****************************************")
print(f"{candidate} :  {percent_votes} % ({candidate_vote_count} )")
print("****************************************")
print(f"Winner: {winner_name}")
print("****************************************")