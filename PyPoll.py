# The data we need to retrieve
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on the popular vote.

# Add out dependencies
import csv
import os

# Assign a variable for the file to load and the path
file_to_load = os.path.join("Resources", "election_results.csv")

# Create a variable to save the file to a path
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter
total_votes = 0

# Print the candidate name
candidate_options = []

# Creating a dictionary of votes cast for each candidate
candidate_votes = {}

# Winning Candidate and Winning Count tracker

winning_candidate = ""

winning_count = 0

winning_percentage = 0

#Open the election results
with open(file_to_load) as election_data:


    # To do: read and analyze the election results

    # Read the file object with the reader function
    file_reader = csv.reader(election_data)

    # Read and print the header row
    headers = next(file_reader)


    # Print each row in the CSV file
    for row in file_reader:

        # Add to the total vote
        total_votes += 1

        # Print the candidate name from each row
        candidate_name = row[2]

        # If the candidate does not match any existing candidate
        if candidate_name not in candidate_options:

            # Add the canidate name to the list
            candidate_options.append(candidate_name)

            # Begin tracking that candidates vote count
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidates count
        candidate_votes[candidate_name] += 1

with open(file_to_save, "w") as txt_file:

    election_results = (
        f"\nElection Results\n"

        f"-------------------------\n"

        f"Total Votes: {total_votes:,}\n"

        f"-------------------------\n")

    print(election_results, end="")

    txt_file.write(election_results)

    # Determine the percentage of votes for each candidate

    for candidate_name in candidate_votes:

        votes = candidate_votes[candidate_name]

        vote_percentage = float(votes) / float(total_votes) * 100

        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

    print(candidate_results)

    txt_file.write(candidate_results)




    if (votes > winning_count) and (vote_percentage > winning_percentage):

                        winning_count = votes

                        winning_percentage = vote_percentage

                        winning_candidate = candidate_name

    winning_candidate_summary = (
                    f"---------------------\n"
                    
                    f"Winner: {winning_candidate}\n"

                    f"Winning Vote Count: {winning_count:,}\n"

                    f"Winning Percentage: {winning_percentage:.1f}%\n"

                    f"---------------------\n"
                )


print(winning_candidate_summary)

txt_file.write(winning_candidate_summary)








 




    



