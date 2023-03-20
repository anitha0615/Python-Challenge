import os
import csv
election_data = os.path.join( "Resources", "election_data.csv")
with open(election_data) as csv_file:
     csv_reader = csv.reader(csv_file, delimiter=",")
     csv_header = next(csv_file)
     print(f"Header: {csv_header}")
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


     #print("Total Votes"+str(total))  
     #print(unique_candidate) 
     count = 1
     for candidate in unique_candidate:
          x = votes.count(candidate)
          print(candidate_votes)
          if count == 1:
            print("==1")
            candidate_votes['candidate_name'] = candidate
            candidate_votes['votes']= x
            print(candidate_votes)
          else:
            print("<> 1")
            candidate_votes['candidate_name'] = candidate
            candidate_votes['votes']= x
            print(candidate_votes)
          count = count + 1      
          #print(f"{candidate} :" + str(x))
          #print(candidate_votes)

    # print(candidate_votes)     
              
              
              
              
              
      