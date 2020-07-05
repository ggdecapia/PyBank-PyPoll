import os 
import csv 

csv_pathname = os.path.join('Resources', 'election_data.csv')

with open(csv_pathname) as csv_filename:
    csv_election_data = csv.reader(csv_filename, delimiter=',')

    election_header = next(csv_election_data)

    # initialization of numeric values
    counter = 0 
    total_votes_counter = 0
    candidates_votes = {}
    winning_votes = 0

    for row in csv_election_data:

        # increment total votes counter
        total_votes_counter = total_votes_counter + 1

        # move candidate name to variable for evaluation
        candidate = row[2]

        # first addition of candidate into candidates list
        if candidate not in candidates_votes:
            candidates_votes[candidate] = 1
        else:
            candidates_votes[candidate] = candidates_votes[candidate] + 1

    # store output into a variable
    electtion_results  = "Election Results" + "\n"
    electtion_results += "-------------------------" + "\n"
    electtion_results += "Total Votes: " + str(total_votes_counter)  + "\n"
    electtion_results += "-------------------------" + "\n"
    for candidate in candidates_votes:
        percent_votes = float(candidates_votes[candidate] / total_votes_counter * 100)
        formatted_percent = "{0:.3f}%".format(percent_votes)
        # printing/displaying each candidate and respective votes
        electtion_results += candidate +": " + str(formatted_percent) + " (" + str(candidates_votes[candidate]) + ")"  + "\n"
        # computing for the winner
        if candidates_votes[candidate] > winning_votes:
            winning_votes = candidates_votes[candidate]
            winner = candidate
    electtion_results += "-------------------------" + "\n"
    electtion_results += "Winner: " + winner + "\n"
    electtion_results += "-------------------------"
    
    # print election analysis into the terminal
    print(electtion_results)

    # write election analysis into a text file
    output_pathname = os.path.join('analysis', 'election_analysis.txt')
    with open(output_pathname, 'w') as election_filename:
        election_filename.write(electtion_results)