# import libraries and csv file
import os
import csv
# declare variables for the list
list_months = []
list_profits_losses = []
# Path to csv file
Budget_csv =  '../pybank/Resources/budget_data.csv'
# Open and Read CSV file
with open(Budget_csv) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    next(csv_reader)
    for column in csv_reader:
        months, Profitlosses = column
# Add data to the list        
        list_months.append(str(months))
        list_profits_losses.append(int(Profitlosses))
# Calculate Total number of months
totalmonths = len(list_months)
#Calculate Total Amount
totalamount = sum(list_profits_losses)
# Calculate changes in "Profit/Losses" over the entire period, and then the average of those changes
# Calculate change in consecutive values
change = []
for i in range(len(list_profits_losses)-1):
    difference =list_profits_losses [i+1] - list_profits_losses[i]
    change.append(difference)
# Calculate the sum of the changes
sum_of_change =  0
for difference in change:
    sum_of_change += difference
# Calculate average of the changes
average = sum_of_change/len(change)
#print("${:.2f}".format(average))
# Determine greatest increase in profits and month
largest = max(list_profits_losses)
smallest = min(list_profits_losses)
#Open a file to write the output to
with open ('test_file.txt', 'w') as txtfile: 
    print('------Text',file=txtfile)
    print((),file=txtfile)
    print('Financial Analysis',file=txtfile)
    print((),file=txtfile)
    print('------------------------------------',file=txtfile)
    print('Total months:',totalmonths, file=txtfile)
    print((),file=txtfile)
    print('Total:',"${:.0f}".format(totalamount), file=txtfile)
    print((),file=txtfile)
    print('Average Change:',"${:.2f}".format(average),file=txtfile)
    print((),file=txtfile)
    print('Greatest Increase in Profits:',max(list_months),"(" + str("${:.0f}".format(largest))+")",file=txtfile)
    print((),file=txtfile)
    print('Greatest Decrease in Profits:',min(list_months),"("+ str("${:.0f}".format(smallest)) + ")", file=txtfile)
    print((),file=txtfile)
    print('----------', file=txtfile)
print('------Text' )
print()
print('Financial Analysis')
print('------------------------------------')
print('Total months:',totalmonths)
print()
print('Total:',"${:.0f}".format(totalamount))
print()
print('Average Change:',"${:.2f}".format(average))
print()
print('Greatest Increase in Profits:',max(list_months),"(" + str("${:.0f}".format(largest))+")")
print()
print('Greatest Decrease in Profits:',min(list_months),"("+ str("${:.0f}".format(smallest)) + ")")
print('----------')