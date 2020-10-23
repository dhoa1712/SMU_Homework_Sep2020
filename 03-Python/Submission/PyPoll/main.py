

import csv
import numpy as np


totalVotes = 0
candidatesDict ={}

csvpath = r"PyPoll\Resources\election_data.csv"
print(csvpath)

# read the file
with open(csvpath, "r") as csvfile:
    poll = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is no header)
    csv_header = next(poll)
    # print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    for row in poll:
        # print(row)
        totalVotes +=1
        if row[2] in candidatesDict.keys():
            candidatesDict[row[2]]+=1
        else:
            candidatesDict[row[2]]=1



    print(totalVotes)
    print(candidatesDict)

# find winner
winner= max(candidatesDict, key =candidatesDict.get) #stole from Alexander who stole from internet :)
print(winner)

# find percent of each candidate
percentDict ={}
for key in candidatesDict.keys():
    perc = candidatesDict[key] / totalVotes
    percentDict[key] = perc

print(percentDict)

# turn percent to a list of string
ListofString = []
for key in percentDict.keys():
    percString = key + ":" + str(round(percentDict[key]* 100, 3)) + "% (" + str(candidatesDict[key]) + ")"
    ListofString.append(percString)

print(ListofString)

# break list of string into lines
finalString = "\n".join(ListofString)


#  write analysis result into summary String:
summaryString = f"""Election Result
-------------------------
Total vote: {totalVotes}
-------------------------
{finalString}
-------------------------
Winner:{winner}
"""

# export the result
with open("poll_results.txt", "w") as file2:
    file2.write(summaryString)
