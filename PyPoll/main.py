import csv

# Locations of the input and output files
input_path = "Resources/election_data.csv"
output_path = "analysis/election_results"

# Declares lists representing input data columns and final values
voterID = []
county = []
candidate = []
cand_list = []
votes = []
percents = []

# Variable for final values
total_votes = 0
winner = ""

# Reads the election data and saves the columns into lists
with open(input_path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csvheader = next(csvreader)

    for row in csvreader:
        voterID.append(row[0])
        county.append(row[1])
        candidate.append(row[2])

# Creates a list of unique candidates
for name in candidate:
    if name not in cand_list:
        cand_list.append(name)

# Calculates total number of votes cast based on voter IDs
total_votes = len(voterID)

# Finds the number of votes each candidate received and its percentage of all votes cast
for cand in range(len(cand_list)):
    vote = candidate.count(cand_list[cand])
    votes.append(vote)
    percent = round(vote / total_votes * 100, 3)
    percents.append(percent)

# Finds the winner of the election by candidate with the largest number of votes
winner_index = votes.index(max(votes))
winner = cand_list[winner_index]

# Formats for election analysis
st_title = "Election Results"
st_line = "-------------------------"
st_total_votes = (f"Total Votes {total_votes}")
st_winner = (f"Winner: {winner}")

# Writes election analysis to election_results text file and prints analysis to terminal 
with open(output_path, 'w') as txtfile:
    txtfile.write(st_title)
    txtfile.write("\n")
    txtfile.write(st_line)
    txtfile.write("\n")
    txtfile.write(st_total_votes)
    txtfile.write("\n")
    txtfile.write(st_line)
    txtfile.write("\n")

    print(st_title)
    print(st_line)
    print(st_total_votes)
    print(st_line)

    # Prints each candidate's vote percentage and total votes received
    # Loop allows for a dynamic number of candidates
    for print_candidate in range(len(cand_list)):
        candidate_stats = (f"{cand_list[print_candidate]}: {percents[print_candidate]}% ({votes[print_candidate]})")
        txtfile.write(candidate_stats + "\n")
        print(candidate_stats)
    
    txtfile.write(st_line)
    txtfile.write("\n")
    txtfile.write(st_winner)
    txtfile.write("\n")
    txtfile.write(st_line)

    print(st_line)
    print(st_winner)
    print(st_line)