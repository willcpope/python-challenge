#Step 1 - Import Python modules
import os
import csv

#Step 2 - Create a variable for the location of the local CSV file
budget_data = os.path.join('/Users/willpope/Desktop/python-challenge/PyBank/budget_data.csv')

#Step 3 - Create a function to analyze budget data
def budget_analysis(data):

    #Step 3.1 - Create variables within the function
    months = 0
    total_pl = 0
    monthly_pl = 0
    change = 0

    #Step 3.2 - Create lists within the function to hold information for analysis
    month_list = []
    change_list = []
    
    #Step 3.3 - Loop through .csv file to analyze data
    for row in data:
       
        # Step 3.3.1 - Increase months for each row
        months += 1
        
        #Step 3.3.2 - Increase P/L for each row
        total_pl += int(row[1])
        
        #Step 3.3.3 - Add months to list
        month_list.append(str(row[0]))
        
        #Step 3.3.4 - Use 'else if' to loop through P/L for each month and calculate changes
        #Step 3.3.5 - 'if' only applies to first row since there's no previous data
        if change == 0:
            change = int(row[1])          
        
        elif change != 0:
            #Step 3.3.5.1 - Use data from P/L column in .csv
            monthly_pl = int(row[1])
            
            #Step 3.3.5.2 - Calculate P/L change by subtrating current P/L from previous P/L
            change = monthly_pl - change
            
            #Step 3.3.5.3 - Add new P/L to list
            change_list.append(change)
            
            #Step 3.3.5.4 - Make change variable the new P/L
            change = int(row[1])
            
    #Step 3.4 - Use .pop function to pop out (remove) first month from list since there's no change
    month_list.pop(0)
    
    #Step 3.5 - Find the greatest P/L increase in the list
    greatest_increase = change_list.index(max(change_list))

    #Step 3.6 - Find the greatest P/L decrease in the list
    greatest_decrease = change_list.index(min(change_list))

    #Step 3.7 - Find greatest P/L increase month in the list
    increase_month = month_list [int(greatest_increase)]
    
    #Step 3.8 - Find the greatest P/L decrease month in the list
    decrease_month = month_list [int(greatest_decrease)]
    
    #Step 3.9 - Find the average of the list
    average = sum(change_list)/float(len(change_list))
    average = round(average,2)
    
    #Step 3.10 - Print analysis
    print(f'Financial Analysis')
    print(f'-------------------------')
    print(f'Total Months: {months}')
    print(f'Total: ${total_pl}')
    print(f'Average Change: ${average}')
    print(f'Greatest Increase in Profits: {increase_month} (${max(change_list)})')
    print(f'Greatest Decrease In Profits: {decrease_month} (${min(change_list)})')

    #Step 3.11 - Create variable for location to export .txt
    budget_export = os.path.join('/Users/willpope/Desktop/python-challenge/PyBank/budget_export.txt')  
    
    #Step 3.12 - Create a new .txt file for analysis
    with open(budget_export, 'w') as new_txt:
        new_txt.write('Financial Analysis \n')
        new_txt.write('------------------------- \n')
        new_txt.write(f'Total Months: {months} \n')
        new_txt.write(f'Total: ${total_pl} \n')
        new_txt.write(f'Average Change: ${average} \n')
        new_txt.write(f'Greatest Increase In Profits: {increase_month} (${max(change_list)}) \n')
        new_txt.write(f'Greatest Decrease In Profits: {decrease_month} (${min(change_list)})')

#Step 4.0 - Split the data on commas in the .csv file
with open(budget_data, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    budget_analysis(csvreader)