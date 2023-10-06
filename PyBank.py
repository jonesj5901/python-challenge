import os
import csv

from numpy import mean

budgetCsv = os.path.join("..", "Resources", "budget_data.csv")

with open(budgetCsv) as csvFile:
    # get the wrapper and store it as a reader using the .reader() function
    csvReader = csv.reader(csvFile, delimiter=",")

    csvHeader = next(csvReader)

    # variables and conditions
    profNloss = []
    date = []
    totalAmt = 0

    for row in csvReader:
        profNloss.append(int(row[1]))
        date.append(row[0])
        
        totalMonths = len(date)
    # The total number of months included in the dataset
        totalAmt += int(row[1])
    # The net total amount of "Profit/Losses" over the entire period
        profChange = []
    for col in range(1, len(profNloss)):
        # The changes in "Profit/Losses" over the entire period, and then the average of those changes
        profChange.append((int(profNloss[col]) - int(profNloss[col - 1])))
        avgChange = sum(profChange) / len(profChange)

        greatestInc = max(profChange)
        greatestDec = min(profChange)

grtIncdate = date[profChange.index(min(profChange))+1]
grtDecdate = date[profChange.index(max(profChange))+1]

print("Financial Analysis" + "\n")
print("........................................................................." + "\n")
print(f"Total Months: {totalMonths}" + "\n")
print(f"Total: ${totalAmt}"  "\n")
print(f"Average Change: ${round(avgChange/(totalMonths-1),2)}" + "\n")
print(f"Greatest Increase in Profits: {grtIncdate} (${greatestInc})" + "\n")
print(f"Greatest Decrease in Profits: {grtDecdate} (${greatestDec})" + "\n")




