# import modules
import csv
import numpy as np

totalMonths = 0
totalProfit = 0

isFirstRow = True
lastRowProfit = 0
changeDict = {}

# open csv file
csvpath=r"PyBank\Resources\budget_data.csv"

with open(csvpath) as csvfile:
    budget = csv.reader(csvfile, delimiter=',')

    # read the header
    csv_header = next(budget)
    #print(f'csv Header:{csv_header}')

    # find toatal months and total profit
    for row in budget:
        totalMonths += 1
        totalProfit += float(row[1])


        # find the profit change and put them in dictionary 
        if isFirstRow:
            lastRowProfit = int(row[1])
            isFirstRow = False
        else:
            change = int(row[1]) - lastRowProfit
            changeDict[row[0]] = change
            lastRowProfit = int(row[1])


# find average, min, max of profit change
avgChange = np.mean(list(changeDict.values()))
# maxChange = np.max(list(changeDict.values()))
# minChange = np.min(list(changeDict.values()))


maxChangeMonth = max(changeDict, key=changeDict.get)  #stole from Alexander who stole from internet :)
maxChange= changeDict[maxChangeMonth]

minChangeMonth = min(changeDict, key=changeDict.get) #stolen from the internet who stole from internet :)
minChange= changeDict[minChangeMonth]



#  write analysis result into summary String:
summaryString = f"""Financial Analysis
-------------------------
Total Months: {totalMonths} 
Total: ${int(round(totalProfit,0))} 
Average Change: ${round(avgChange,2)} 
Greatest Increase in Profit: {maxChangeMonth} ${maxChange} 
Greatest Decrease in Profit: {minChangeMonth} ${minChange}
"""


# export the result
with open("bank_results.txt", "w") as file1:
    file1.write(summaryString)
