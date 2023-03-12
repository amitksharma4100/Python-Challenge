
import os
import csv

# declare variables for the list and initalize Total_votes counter
candidate_selection = []
votes_for_each_candidate = {}
Total_votes = 0

# Path to csv file
election_csv = '../pypoll/Resources/election_data.csv'

# Open and Read CSV file
with open(election_csv) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    headers = next(csv_reader)
    #Total votes and votes received by each candidate
    for row in csv_reader:
        Total_votes += 1
        candidates_receiving_votes = row[2]
        if candidates_receiving_votes not in candidate_selection:
            candidate_selection.append(candidates_receiving_votes)
            votes_for_each_candidate[candidates_receiving_votes] = 0
        votes_for_each_candidate[candidates_receiving_votes] += 1

# Determine percentage of votes received by each candidate
Diana_DeGette_Votes = float(votes_for_each_candidate['Diana DeGette'])   
Percentage_votes_Diana_DeGette = (float(Diana_DeGette_Votes)/float(Total_votes))*100
Charles_Casper_Stockham_Votes = float(votes_for_each_candidate['Charles Casper Stockham'])
Percentage_Votes_Charles_Casper_Stockham = (float(Charles_Casper_Stockham_Votes)/float(Total_votes))*100
Raymon_Anthony_Doane_Votes = float(votes_for_each_candidate['Raymon Anthony Doane'])
Percentage_Votes_Raymon_Anthony_Doane = (float(Raymon_Anthony_Doane_Votes)/float(Total_votes))*100

#print formatted text on screen
print('---Text')
print('Election Results')
print('--------------------------------')
print('Total Votes: ' + str(Total_votes))
print('--------------------------------')
print('Charles Casper Stockham:',   str("{:.3f}%".format(Percentage_Votes_Charles_Casper_Stockham)), "(" + str(int(Charles_Casper_Stockham_Votes)) +")")
print('Diana DeGette:',   str("{:.3f}%".format(Percentage_votes_Diana_DeGette)), "(" + str(int(Diana_DeGette_Votes)) +")")
print('Raymon Anthony Doane:',   str("{:.3f}%".format(Percentage_Votes_Raymon_Anthony_Doane)), "(" + str(int(Raymon_Anthony_Doane_Votes)) +")")
print('--------------------------------')
print("Winner:", "Diana DeGette")
print('--------------------------------')
print('---')
# print to an external file
with open ('Results.txt', 'w') as resultsfile: 
    print('---Text', file = resultsfile)
    print('Election Results', file = resultsfile)
    print('--------------------------------', file = resultsfile)
    print('Total Votes: ' + str(Total_votes), file = resultsfile)
    print('--------------------------------',file = resultsfile)
    print('Charles Casper Stockham:',   str("{:.3f}%".format(Percentage_Votes_Charles_Casper_Stockham)), "(" + str(int(Charles_Casper_Stockham_Votes)) +")", file = resultsfile)
    print('Diana DeGette:',   str("{:.3f}%".format(Percentage_votes_Diana_DeGette)), "(" + str(int(Diana_DeGette_Votes)) +")", file = resultsfile)
    print('Raymon Anthony Doane:',   str("{:.3f}%".format(Percentage_Votes_Raymon_Anthony_Doane)), "(" + str(int(Raymon_Anthony_Doane_Votes)) +")",file = resultsfile )
    print('--------------------------------', file = resultsfile)
    print("Winner:", "Diana DeGette", file= resultsfile)
    print('--------------------------------', file = resultsfile)
    print('---',file = resultsfile)