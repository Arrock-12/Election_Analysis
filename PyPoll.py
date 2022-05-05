# Add our dependencies
import csv
import os

# Assign a variable to load a file from a path
file_to_load = os.path.join("Resources", "election_results.csv")

# Assign a variable to save the file to a path
file_to_save = os.path.join("Analysis", "election_analysis.txt")

# Initialize a total vote counter
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

# Save the results to our text file

with open(file_to_save, "w") as txt_file:
     election_results = (
          f"\nElection Results\n"
          f"----------------------\n"
          f"Total Votes: {total_votes:,}\n"
          f"----------------------\n")
     print(election_results, end="")

     # After printing the final vote count to the terminal save the final vote count to the text file.
     txt_file.write(election_results)

     for candidate_name in candidate_votes:
          # Retrieve vote count for each candidate
          votes = candidate_votes[candidate_name]
          # Calculate the percentage of votes
          vote_percentage = float(votes)/float(total_votes)*100

          candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
     
          #Print each candidate's voter count and percentage to the terminal
          print(candidate_results)

          #save the candidate results to our text file

          txt_file.write(candidate_results)

          #Determine winning vote count, winning percentage, and winning candidate
          if (votes > winning_count) and (vote_percentage > winning_percentage):
               #If True then set winning_count = votes and winning_perecent = vote_percentage
               winning_count = votes
               winning_percentage = vote_percentage
               #Set the winning_candidate equal to the candidate's name
               winning_candidate = candidate_name

     # Print the winning candidate's results to the terminal
     winning_candidate_summary =(
          f"----------------------------\n"
          f"Winner: {winning_candidate}\n"
          f"Winning Vote Count: {winning_count:,}\n"
          f"Winning Percentage: {winning_percentage:.1f}%\n"
          f"-----------------------------\n")
     print(winning_candidate_summary)

     # Save the winning candidate's results to the text file.

     txt_file.write(winning_candidate_summary)