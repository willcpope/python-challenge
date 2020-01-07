#Step 1 - Import Python modules
import os
import csv

#Step 2 - Create a variable for the location of the local CSV file
election_data = os.path.join('/Users/willpope/Desktop/python-challenge/PyPoll/election_data.csv')  

#Step 3 - Create a function to analyze budget data
def election_results(data):

    #Step 3.1 - Create variables within the function
    total_votes = 0

    #Step 3.2 - Create lists within the function to hold information for analysis
    votes_list = []
    candidate_list = []
    names_list = []
    percent_list = []
     
    #Step 3.3 - Loop through .csv file to analyze data
    for row in data:

        #Step 3.3.1 - Increase votes_list for each row
        total_votes += 1

        #Step 3.3.2 - Add names to list
        if row[2] not in names_list:
            names_list.append(row[2])

        #Step 3.3.3 - Add votes to list
        votes_list.append(row[2])

   #Step 3.4 - Loop through lists to determine votes_list for each candidate
    for candidate in names_list:
        candidate_list.append(votes_list.count(candidate))
        percent_list.append(round(votes_list.count(candidate)/total_votes*100,4))

    #Step 3.5 - Search list to find winner
    winner = names_list[candidate_list.index(max(candidate_list))]
    
    #Step 3.6 - Print election results
    # print results, use a loop for the number of names_list
    print('Election Results')
    print('-------------------------')
    print(f'Total Votes: {total_votes}')
    print('-------------------------')
    
    #Step 3.7 - Loop through list for winning candidate
    for i in range(len(names_list)):
        print(f'{names_list[i]}: {percent_list[i]}% ({candidate_list[i]})')
    print('-------------------------')
    print(f'Winner: {winner}')
    print('-------------------------')

    #Step 3.8 - Create variable for location to export .txt
    election_export = os.path.join('/Users/willpope/Desktop/python-challenge/PyPoll/election_export.txt')

    #Step 3.9 - Create a new .txt file for analysis
    with open(election_export, "w") as new_txt:
        new_txt.write('Election Results \n')
        new_txt.write('------------------------- \n')
        new_txt.write(f'Total Votes: {total_votes} \n')
        new_txt.write('------------------------- \n')
       
        for i in range (len(names_list)):
            new_txt.write(f'{names_list[i]}: {percent_list[i]}% ({candidate_list[i]}) \n')
        new_txt.write('------------------------- \n')
        new_txt.write(f'Winner: {winner} \n')
        new_txt.write('-------------------------')


#Step 4.0 - Split the data on commas in the .csv file
with open(election_data, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    election_results(csvreader)