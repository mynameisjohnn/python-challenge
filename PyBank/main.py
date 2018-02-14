import os
import csv

csv_path = os.path.join("budget_data_1.csv")

Months=[]
Revenue=[]

with open(csv_path, 'r') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")

    next(csv_reader, None)

    for row in csv_reader:

        #Append data from Rows
        Months.append(row[0])
        Revenue.append(int(row[1]))
val= Revenue[0]  
Change=[]  
for i in Revenue:
    Diff = i-val
    Change.append(Diff)
    val=i

# Index for changes
max_index=[i for i, j in enumerate(Change) if j == (max(Change))][0]
min_index=[i for i, j in enumerate(Change) if j == (min(Change))][0]


Total_Months=len(Revenue)

Total_Revenue=sum(Revenue) 

Average_Revenue_Change=((sum(Change))/(len(Change)-1))

Greatest_Increase_Month=Months[max_index] 
Greatest_Increase_Change=max(Change)
Greatest_Decrease_Month=Months[min_index]
Greatest_Decrease_Change=min(Change)
print('Financial Analysis')
print('----------------------------')
print('Total Months: ' + str(Total_Months)) 
print('Total Revenue: $' + str(Total_Revenue))
print('Average Revenue Change: $' + str(Average_Revenue_Change))
print('Greatest Increase in Revenue:' + Greatest_Increase_Month +" $"+ str(Greatest_Increase_Change))
print('Greatest Decrease in Revenue:' + Greatest_Decrease_Month +" $"+ str(Greatest_Decrease_Change))
