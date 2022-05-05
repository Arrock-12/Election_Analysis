#1 Total number of votes cast
#2 Complete list of candidates
#3 Total number of voters each candidate received
#4 Percentage of votes each candidiate won
#5 Winner based on popular vote
# Assign a variable for the file to load and the path

# Add our dependencies
import csv
import os

# Assign a variable to load a file from a path
file_to_load = os.path.join("Resources", "election_results.csv")

# Assign a variable to save the file to a path
file_to_save = os.path.join("Analysis", "election_analysis.txt")

#1. Initialize a total vote counter
total_votes = 0

# Create a list to hold candidate names
candidate_options = []

# Create dictionary to hold candidates (key) and their votes (values)
candidate_votes = {}

# Winning candidate and winning count tracker

winning_candidate = ""
winning_count = 0
winning_percentage = 0


# Open the election results and read the file.
with open(file_to_load) as election_data:
     file_reader=csv.reader(election_data)
 
     # Read and print header row
     headers = next(file_reader)
  
     # Print each row in the CSV File
     for row in file_reader:
          # 2 Add to the total vote count
          total_votes+=1

          #Print candidate's name from each row
          candidate_name = row[2]

          #If candidate not already listed then add to candidate list
          if candidate_name not in candidate_options:
               # Add to candidate options
               candidate_options.append(candidate_name) 

               # Track votes for each candidate
               candidate_votes[candidate_name] = 0

          # Add votes for each candidate
          candidate_votes[candidate_name] +=1

# Determine percentage of votes for each candidate

# Iterate trhough the candidate list
for candidate_name in candidate_votes:
     # Retrieve vote count for each candidate
     votes = candidate_votes[candidate_name]
     # Calculate the percentage of votes
     vote_percentage = float(votes)/float(total_votes)*100
     # Print the candidate name and percentage of votes
     #print(f"{candidate_name} received {vote_percentage:.1f}% of the vote.")
     print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
     # Determine winning vote count and candidate

     #Determine if the votes are greater than the winning count

     if (votes > winning_count) and (vote_percentage > winning_percentage):
          #If True then set winning_count = votes and winning_perecent = vote_percentage
          winning_count = votes
          winning_percentage = vote_percentage
          #Set the winning_candidate equal to the candidate's name
          winning_candidate = candidate_name
winning_candidate_summary =(
     f"----------------------------\n"
     f"Winner: {winning_candidate}\n"
     f"Winning Vote Count: {winning_count:,}\n"
     f"Winning Percentage: {winning_percentage:.1f}%\n"
     f"-----------------------------\n")
print(winning_candidate_summary)



         