import csv

path = "PyBank/Resources/budget_data.csv"
# path = "../Resources/budget_data.csv"

date = []
prof_loss = []

month_count = 0
net_profit = 0
average_change = 0
greatestIN = 0
greatestDE = 0

with open(path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csvheader = next(csvreader)
    
    for row in csvreader:
        date.append(row[0])
        prof_loss.append(int(row[1]))


month_count = len(date)
net_profit = sum(prof_loss)
greatestIN = max(prof_loss)

print(month_count)
print(net_profit)
print(greatestIN)
# print(date)
# print(prof_loss)

