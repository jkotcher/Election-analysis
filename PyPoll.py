# The data we need to retrieve
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on the popular vote.
import csv
import os
# Assign a variable for the file to load and the path
file_to_load = os.path.join("Resources", "election_results.csv")

#Open the election results
with open(file_to_load) as election_data:


# print the file object
    print(election_data)

# Create a file name with an indirect or direct path
file_to_save = os.path.join("analysis", "election_analysis.txt")

outfile = open(file_to_save, "w")

# Write some data to the file
outfile.write("Hello World")

# Close the file
outfile.close()
