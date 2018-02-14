import os
import csv

# Multiple File Numbers
file_number = ['1', '2']

# CSV Location
csv_path = os.path.join("raw_data", "election_data_" + file_number + ".csv")

# List to store candidate
Candidates=[]

#Open CSV files
with open(csv_path, newline="") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")

    # Skip First Row Headers  
    next(csv_reader, None)

    # Loop over Rows
    for row in csv_reader:
        # Append data from rows
        Candidates.append(row[2])

# Get Voting Summary Information
total_votes = len(Candidates)
candidate_list = set(Candidates)
candidate_list = [i for i in candidate_list]
vote_counts = [Candidates.count(i) for i in candidate_list]
vote_percent = [((Candidates.count(i)/total_votes)*100) for i in candidate_list]
vote_percent = [round(i,3) for i in vote_percent]
max_vote = max(vote_counts)
mx,idx = max( (vote_counts[i],i) for i in range(len(vote_counts)) )
wins=candidate_list[idx]

# Print out the Summary 
print('Election Results')
print('Total Votes: ' + str(total_votes) )
candidate_num=0
for i in candidate_list:
    print(i + ': ' + str(vote_percent[candidate_num])+'% '+ '(' + str(vote_counts[candidate_num]) + ')' )
    candidate_num+=1
print('Winner: ' + str(wins)) 