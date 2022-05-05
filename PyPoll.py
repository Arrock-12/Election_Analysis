#1 Total number of votes cast
#2 Complete list of candidates
#3 Total number of voters each candidate received
#4 Percentage of votes each candidiate won
#5 Winner based on popular vote
# Assign a variable for the file to load and the path
# Add our dependencies
import csv
import os

#Assign a variable to load a file from a path
file_to_load = os.path.join("Resources", "election_results.csv")
#file_to_load = 'Resources/election_results.csv'

# Assign a variable to save the file to a path
file_to_save = os.path.join("Analysis", "election_analysis.txt")

# Open the election results and read the file.
with open(file_to_load) as election_data:

     # To do: Read and analyze the data
     file_reader=csv.reader(election_data)
     #print(election_data)

     # Read and print header row
     headers = next(file_reader)
     print(headers)

     #for row in file_reader:
          #print(row)
# Create a filename variable to a direct or indirect path to the file.


# Using the with statement open the file as a text file.
#with open(file_to_save, "w") as txt_file:

    # Write some data to the file.
    #txt_file.write("Counties in the Election\n---------------------\nArapahoe\nDenver\nJefferson")