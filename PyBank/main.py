import os
import csv
budget_data = os.path.join( "Resources", "budget_data.csv")
with open(budget_data) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    csv_header = next(csv_file)
    print(f"Header: {csv_header}")
    total = 0 # variable created to hold total sum of profits and loses for all months
    months = 0 # variable to hold the number of months which is equal to number of records in the files minus header row
    change = [] # variable to hold difference between current month's PL and previous month's PL 
    pl = 0 # variable to hold PL value from previous month
    months_list = [] # List variable to hold months list from the file
    pl_list = [] # List variable to hold PL from all rows in the file
    for row in csv_reader: # For loop to iterate through the rows in the file
       total= total + int(row[1]) #Variable to hold sum of PLs (Not required for final output)
       months = months+1 #Variable to hold total number of months 
       if int(months) > 0: # If loop to skip first row
        months_list.append(row[0]) # Appending months from the file to the month's list
        pl_list.append(row[1]) #Appending PLs from the file to the pl_lst
        change.append(int(row[1]) - int(pl)) # Appending change in PL between consecutive rows to a list
        pl = row[1] # Saving previous PL to a variable.
    
    print("Total Months: "+str(months) ) # Total months output 
    print("Total: "+str(total) ) # Total PL (Not required in output)
    total_change = 0 # Intial variable created to hold total change value for avrage calculation
    for chn in range(len(change)): # for loop to iterate through the change list created in line 20
        if chn > 0: # if condition to skip the first row change
            total_change = total_change + change[chn] # Adding the next row's change to current row's change 

    avg_change = ((int(total_change)) /   (len(change)-1) )  # Calculating average change. We do len(change)-1 to exclude final row

    print("Total Change : " +str(total_change ) ) # Total change (Not required in final output)
    print("Average Change: " +str(avg_change))
    print("Greates Increse in profit :" +str(max(change))) # Getting greatest change
    print("Greates Increse in profit :" +str(min(change))) # Getting least change
    print(months_list) # Printing months list created in line 18
    print(change) # Printing change list created in line 20
    changeinpl = dict(zip(months_list,change)) # appending months_list and change list in to a dictionary
    print(max(changeinpl.values())) # print max change value from dictionary
    print(max(changeinpl, key=changeinpl.get))  # print max change key from dictionary
    print(min(changeinpl.values())) # print min change value from dictionary
    print(min(changeinpl, key=changeinpl.get)) # print min change value from dictionary
    #Final output
    print("Financial Analysis")
    print("-------------------------")
    print("Total Months: "+str(months) ) 
    print("Total: $"+str(total) )
    print("Average Change: $" +str(round(avg_change,2)))
    print("Greatest Increase in profit : "  + str(max(changeinpl, key=changeinpl.get)) + " ($" + str(max(changeinpl.values())) + ")")
    print("Greatest Increase in profit : "  + str(min(changeinpl, key=changeinpl.get)) + " ($" + str(min(changeinpl.values())) + ")")