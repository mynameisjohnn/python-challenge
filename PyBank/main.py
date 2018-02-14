import os
import csv

# Multiple File Numbers
file_number = ['1', '2']

# CSV Location
csv_path = os.path.join("raw_data", "budget_data_" + file_number + ".csv")

# Lists to Store Month Count and Revenue Sum
Months=[]
Revenue=[]

# Open CSV files
with open(csv_path, 'r') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")

    # Skip First Row Headers 
    next(csv_reader, None)

    # Loop over Rows
    for row in csv_reader:

        #Append data from Rows
        Months.append(row[0])
        Revenue.append(row[1])
  
# work out change data and store it in a list  
val=Revenue[0] # set initial value  
Change=[] # set change values list  
for i in Revenue: # loop over Revenue list to calculate change 
    Diff=i-val
    Change.append(Diff) # update Change 
    val=i


max_index=[i for i, j in enumerate(Change) if j == (max(Change))][0] # index of max Change 
min_index=[i for i, j in enumerate(Change) if j == (min(Change))][0] # index of min Change 

#Return Number of Months
Total_Months=len(Revenue)

#Return Sum of Revenue
Total_Revenue=sum(Revenue) 

#Average Revenue Change is Sum of Revenue divided by Number of Months
Average_Revenue_Change=((sum(Change))/(len(Change)-1))

#Return Greatest Increase in Revenue
Greatest_Increase_Month=Months[max_index] 
Greatest_Increase_Change=max(Change)

#Return Greatest Decrease in Revnue
Greatest_Decrease_Month=Months[min_index]
Greatest_Decrease_Change=min(Change)

# Print out the Summary 
print('Financial Analysis')
print('----------------------------')
print('Total Months: ' + str(Total_Months)) 
print('Total Revenue: $' + str(Total_Revenue))
print('Average Revenue Change: $' + str(Average_Revenue_Change))
print('Greatest Increase in Revenue:' + Greatest_Increase_Month +" $"+ str(Greatest_Increase_Change))
print('Greatest Decrease in Revenue:' + Greatest_Decrease_Month +" $"+ str(Greatest_Decrease_Change))