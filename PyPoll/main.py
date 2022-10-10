# Imports
import os
import csv

# Create filepath
csvpath = os.path.join('Resources', 'election_data.csv')

# Read the csv and convert into lists
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile,delimiter=',')
    
    # Reads the header line in csv and stores it
    csv_header = next(csvreader)

    # Lists to store data
    voter_ID = []
    candidate = []
    unique_candidates = []

    # Adds items to lists
    for row in csvreader:
        voter_ID.append(row[0])
        candidate.append(row[2])

    # Print header and total votes
    print("Election Results\n")
    print("-----------------------------\n")
    print(f"Total Votes: {len(voter_ID)}\n")
    print("-----------------------------\n")

    # Gets the name of each unique candidate for a list for printing, and counts the votes for each candidate
    total_votes = len(voter_ID)
    candidate_1 = 0
    candidate_2 = 0
    candidate_3 = 0
    for x in candidate:
        if x not in unique_candidates:
            unique_candidates.append(x)
        
    for x in candidate:
        if x == unique_candidates[0]:
            candidate_1 += 1
        elif x == unique_candidates[1]:
            candidate_2 += 1
        elif x == unique_candidates[2]:
            candidate_3 += 1

    # Calculates percentages of total votes for each candidate
    candidate_1_percent = round((candidate_1/total_votes)*100, 3)
    candidate_2_percent = round((candidate_2/total_votes)*100, 3)
    candidate_3_percent = round((candidate_3/total_votes)*100, 3)

    # Prints each candidate with their percentage of total votes and total votes
    print(f"{unique_candidates[0]}: {candidate_1_percent}% ({int(candidate_1)})\n")
    print(f"{unique_candidates[1]}: {candidate_2_percent}% ({int(candidate_2)})\n")
    print(f"{unique_candidates[2]}: {candidate_3_percent}% ({int(candidate_3)})\n")
    print("-----------------------------\n")

    # Finds and prints the winner of the election
    if candidate_1 > candidate_2 and candidate_1 > candidate_3:
        print(f"Winner: {unique_candidates[0]}\n")
    elif candidate_2 > candidate_1 and candidate_2 > candidate_3:
        print(f"Winner: {unique_candidates[1]}\n")
    elif candidate_3 > candidate_1 and candidate_3 > candidate_2:
        print(f"Winner: {unique_candidates[2]}\n")
    print("-----------------------------\n")

    # Exports a text file
    with open(os.path.join("Analysis","election_data_analysis.txt"), "w+") as analysis_text:
        analysis_text.write("Election Results\n")
        analysis_text.write("-----------------------------\n")
        analysis_text.write(f"Total Votes: {len(voter_ID)}\n")
        analysis_text.write("-----------------------------\n")
        analysis_text.write(f"{unique_candidates[0]}: {candidate_1_percent}% ({int(candidate_1)})\n")
        analysis_text.write(f"{unique_candidates[1]}: {candidate_2_percent}% ({int(candidate_2)})\n")
        analysis_text.write(f"{unique_candidates[2]}: {candidate_3_percent}% ({int(candidate_3)})\n")
        analysis_text.write("-----------------------------\n")
        if candidate_1 > candidate_2 and candidate_1 > candidate_3:
            analysis_text.write(f"Winner: {unique_candidates[0]}\n")
        elif candidate_2 > candidate_1 and candidate_2 > candidate_3:
            analysis_text.write(f"Winner: {unique_candidates[1]}\n")
        elif candidate_3 > candidate_1 and candidate_3 > candidate_2:
            analysis_text.write(f"Winner: {unique_candidates[2]}\n")
        analysis_text.write("-----------------------------\n")