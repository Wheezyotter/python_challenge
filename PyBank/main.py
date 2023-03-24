import csv

# Locations of the input and output files
input_path = "Resources/budget_data.csv"
output_path = "analysis/financial_analysis.txt"

# Declares lists representing each column in the budget and a list for calculating changes
date = []
prof_loss = []
prof_loss_diff = []

# Declares variables for final calculated values
month_count = 0
net_profit = 0
average_change = 0
greatestIN = 0
greatestDE = 0

# Reads the budget_data file and saves columns into lists
with open(input_path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csvheader = next(csvreader)
    
    for row in csvreader:
        date.append(row[0])
        prof_loss.append(int(row[1]))

# Calculates the percent change of profits/losses
for i in range(len(prof_loss) - 1):
    prof_loss_diff.append(prof_loss[i + 1] - prof_loss[i])

# Saves, formats and calculates all the final values
month_count = len(date)
net_profit = sum(prof_loss)
average_change = sum(prof_loss_diff) / len(prof_loss_diff)
average_change = round(average_change, 2)
greatestIN = max(prof_loss_diff) 
greatestDE = min(prof_loss_diff)

# Finds the associated date of change, +1 added to index to account for difference calculation
index_IN = prof_loss_diff.index(greatestIN)
date_IN = date[index_IN + 1]
index_DE = prof_loss_diff.index(greatestDE)
date_DE = date[index_DE + 1]

# Saves final summary table into variables
title_print = "Financial Analysis"
line_print = "----------------------------"
total_months_print = (f"Total Months: {month_count}")
total_profit_print = (f"Total: ${net_profit}")
average_change_print = (f"Average Change: ${average_change}")
greatest_in_print = (f"Greatest Increase in Profits: {date_IN} ({greatestIN})")
greatest_de_print = (f"Greatest Decrease in Profits: {date_DE} ({greatestDE})")

# Saves summary table to financial_analysis text file
with open(output_path, 'w') as txtfile:
    txtfile.writelines(title_print)
    txtfile.write("\n")
    txtfile.writelines(line_print)
    txtfile.write("\n")
    txtfile.writelines(total_months_print)
    txtfile.write("\n")
    txtfile.writelines(total_profit_print)
    txtfile.write("\n")
    txtfile.writelines(average_change_print)
    txtfile.write("\n")
    txtfile.writelines(greatest_in_print)
    txtfile.write("\n")
    txtfile.writelines(greatest_de_print)

# Prints summary table to terminal
print(title_print)
print(line_print)
print(total_months_print)
print(total_profit_print)
print(average_change_print)
print(greatest_in_print)
print(greatest_de_print)