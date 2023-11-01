import os
import csv

# Define the relative file path using os.path.join
csvpath = os.path.join("..", "anyas", "Desktop", "python-challenge", "PyPoll", "Resources", "election_data.csv")

# Initialize variables
total_votes = 0
candidates = {}
winner = ""
winner_votes = 0

# Store the header row
header = []

# Read the CSV file using csv.reader with delimiter
with open(csvpath, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # Store the header row
    header = next(csvreader)

    for row in csvreader:
        total_votes = total_votes + 1  # Increment total_votes
        candidate_name = row[2]

        if candidate_name in candidates:
            candidates[candidate_name] = candidates[candidate_name] + 1  # Increment candidate's votes
        else:
            candidates[candidate_name] = 1

# Find the winner and calculate the percentages
for candidate, votes in candidates.items():
    if votes > winner_votes:
        winner_votes = votes
        winner = candidate

# Print the analysis results with the requested format
print("\nElection Results")
print("-------------------------")
print("Total Votes:", total_votes)
print("-------------------------")
for candidate, votes in candidates.items():
    percentage = (votes / total_votes) * 100
    print(f"{candidate}: {round(percentage, 3)}% ({votes})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

# Specify the output path
output_path = os.path.join("..", "anyas", "Desktop", "python-challenge", "PyPoll", "analysis", "election_results.txt")

# Create and open a text file for writing the analysis results at the specified output path
with open(output_path, "w") as textfile:
    # Write the analysis results to the text file with the requested format
    textfile.write("Election Results\n")
    textfile.write("-------------------------\n")
    textfile.write(f"Total Votes: {total_votes}\n")
    textfile.write("-------------------------\n")
    for candidate, votes in candidates.items():
        percentage = (votes / total_votes) * 100
        textfile.write(f"{candidate}: {round(percentage, 3)}% ({votes})\n")
    
    textfile.write("-------------------------\n")
    textfile.write(f"Winner: {winner}\n")
    textfile.write("-------------------------\n")

# Print a message indicating that the results have been exported to the specified output path
print("Election results have been exported to 'election_results.txt'.")
