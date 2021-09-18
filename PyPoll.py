# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

#initalize a total vote counter
total_votes = 0

#This will get the candidate's name options
candidate_options = []

#This is an empty dictionary that will hold the candidates votes
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # To do: read and analyze the data here.

    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)
 # Print the header row.
    headers = next(file_reader)

    # Print each row in the CSV file.
    for row in file_reader:
        #Add to the total vote count
        total_votes += 1

        #This will print the candidates name from each row
        candidate_name = row[2]

        #Then we take the candidates name and add it to our candidates name "option" list
        #But we have to add an if statement so the values are unique
        if candidate_name not in candidate_options:

            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

           # Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0

# Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

        #Now we open the file so we can save our results
with open(file_to_save, "w") as txt_file:
        election_results = (
    f"\nElection Results\n"
    f"-------------------------\n"
    f"Total Votes: {total_votes:,}\n"
    f"-------------------------\n")
print(election_results, end="")
        # Save the final vote count to the text file.
    
txt_file.write(election_results)

        for candidate_name in candidate_votes: 
            #This will grab the vote count per candidate
            votes = candidate_votes[candidate_name]

            #Now we find out who had the winning vote count and which candidate it was
            #Determine who has the winning count

            if (votes > winning_count) and (vote_percentage > winning_percentage):
                #This bit confuses me. But here are the module notes - I may have to come back to this section
                    # If true then set winning_count = votes and winning_percent =
                    # vote_percentage.
                winning_count = votes
                winning_percentage = vote_percentage

                #set the winning candidates name
                winning_candidate = candidate_name 



            #now we make it a percentage
            vote_percentage = float(votes) / float(total_votes) * 100



    
