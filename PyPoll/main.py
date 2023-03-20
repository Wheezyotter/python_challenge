import csv

path = "PyPoll/Resources/election_data.csv"

voterID = []
county = []
candidate = []
cand_list = []

total_votes = 0
CCS_votes = 0
DD_votes = 0
RAD_votes = 0
CCS_percent = 0
DD_percent = 0
RAD_percent = 0
winner = ""


with open(path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csvheader = next(csvreader)

    for row in csvreader:
        voterID.append(row[0])
        county.append(row[1])
        candidate.append(row[2])

for name in candidate:
    if name not in cand_list:
        cand_list.append(name)
    
total_votes = len(voterID)
CCS_votes = candidate.count(cand_list[0])
DD_votes = candidate.count(cand_list[1])
RAD_votes = candidate.count(cand_list[2])
CCS_percent = round(CCS_votes / total_votes * 100, 3)
DD_percent = round(DD_votes/ total_votes * 100, 3)
RAD_percent = round(RAD_votes / total_votes * 100, 3)


print(total_votes)
print(CCS_votes, DD_votes, RAD_votes)
print(CCS_percent, DD_percent, RAD_percent)
print(cand_list)

