import os
import csv
election_data = os.path.join( "Resources", "election_data.csv")
with open(election_data) as csv_file:
     csv_reader = csv.reader(csv_file, delimiter=",")
     csv_header = next(csv_file)
     total = 0
     unique_candidate = []
     count_votes = 0
     votes = []
     candidate_votes = {}
     
     for row in csv_reader: # For loop to iterate through the rows in the file
        total= total + 1
        if row[2] not in unique_candidate:
           unique_candidate.append(row[2])
        votes.append(row[2])   

    
     print("Election Results")
     print("\n-------------------------\n")
     print("Total Votes: "+str(total))
     print("\n-------------------------\n")
     for candidate in unique_candidate:
          x = votes.count(candidate)
          pct = (x/total)*100
          print(f"{candidate}: {round(pct,3)}% ({x})")
          print("\n") 
          candidate_votes[candidate] = x 
     print("-------------------------\n")
     print("Winner:" + str(max(candidate_votes,key = candidate_votes.get)))
     print("\n-------------------------\n")
     
              
     
               
              
      