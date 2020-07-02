import os 
import csv 

csv_pathname = os.path.join('Resources', 'election_data.csv')

with open(csv_pathname) as csv_filename:
    csv_election_data = csv.reader(csv_filename, delimiter=',')

    print(csv_election_data)

    election_header = next(csv_election_data)
    print(election_header)

    # initialization of numeric values
    counter = 0 
    total_votes_counter = 0
    no_of_candidates = 0
    candidates_list = []
    candidates_votes = {}
    percent_of_votes = 0.00
    winning_votes = 0
    

    for row in csv_election_data:

        # increment total votes counter
        total_votes_counter = total_votes_counter + 1

        # move candidate name to variable for evaluation
        candidate = row[2]

        # first addition of candidate into candidates list
        if candidate not in candidates_list:
            candidates_list.append(candidate)
            candidates_votes[candidate] = 0
            candidates_votes[candidate] = candidates_votes[candidate] + 1
        else:
            if candidate in candidates_list:
                candidates_votes[candidate] = candidates_votes[candidate] + 1

    print()
    print("Election Results")
    print("-------------------------")
    print("Total Votes " + str(total_votes_counter))
    print("-------------------------")
    for candidate in candidates_list:
        percent_votes = float(candidates_votes[candidate] / total_votes_counter * 100)
        formatted_percent = "{0:.3f}%".format(percent_votes)
        print(f"{candidate}: {formatted_percent} ({candidates_votes[candidate]})")
        if candidates_votes[candidate] > winning_votes:
            winning_votes = candidates_votes[candidate]
            winner = candidate
    print("-------------------------")
    print(f"Winner: {winner} {winning_votes}")
    print("-------------------------")
