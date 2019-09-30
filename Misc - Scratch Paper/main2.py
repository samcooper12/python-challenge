import os
import csv
import time
#import threading
from threading import Timer

csvpath = os.path.join('budget_data.csv')

m=0
total=0
x=0
avg_change=0
maxt = 0
mint = 0
maxm = []
minm = []
y = 0
report = ""
### The total number of months included in the dataset
with open(csvpath, newline='') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    for row in csvreader:
        m = m + 1

### net total for profit column
with open(csvpath, newline='') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    for row in csvreader:
        total += int(row[1])
        x = x + 1

### The average of the changes in "Profit/Losses" over the entire period
with open(csvpath, newline='') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    
    avg_change = (total/m)

# print("datatypes")
# print(f"m: {type(m)}")
# print(f"total: {type(total)}")
# print(f"avg_change: {type(avg_change)}")
# print(f"row: {type(row[1])}")

### The greatest increase in profits (date and amount) over the entire period
with open(csvpath, newline='') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    for row in csvreader:
        
        maxt = max(maxt,int(row[1]))
        mint = min(mint,int(row[1]))
        
    print(maxt, maxm)
    print(mint, minm)


with open(csvpath, newline='') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
        
    # NOTE: To surface the month names while accomodating for whether multiple months
    # have the same max or min --  I . made these variables a list datatype (hence the weird print format)

    for row in csvreader:

            if int(row[1]) == maxt:
                maxm.append(row[0])
                print(f"Month of largest profit: {maxm}")
            
            elif int(row[1]) == mint:
                minm.append(row[0])
                print(f"month of largest losses: {minm}")

# total_form = "{'${:,.2f}'.format(total)}"
# print(f"total_form: {total_form}")
# avg_change_form = ""
# maxt_form = ""
# mint_form = ""

# pretext = ("Running financial analysis..." + "\n" + "analysis complete" + "\n" + "-------------------")

# report = (f"Number of months recorded: {m}" + "\n" + "Net total profit: {'${:,.2f}'.format(total)}" + "\n" + "Average monthly net profit/loss: {'${:,.2f}'.format(avg_change)}" + "\n" + "Largest profit in a month: {'${:,.2f}'.format(maxt)} {maxm}" + "\n" + "Largest loss in a month: {'${:,.2f}'.format(mint)} {minm}")



# print(pretext)
# print(report)



# print(pretext)
# print("###")

print(f"Running financial analysis...")
print(f"analysis complete")
print(f"------------------------------------------")
print(f"Number of months recorded: {m}")
print(f"Net total profit: {'${:,.2f}'.format(total)}")
print(f"Average monthly net profit/loss: {'${:,.2f}'.format(avg_change)}")
print(f"Largest profit in a month: {'${:,.2f}'.format(maxt)} {maxm}")
print(f"Largest loss in a month: {'${:,.2f}'.format(mint)} {minm}")
print(f"------------------------------------------")


# ###### SCRATCHPAD 

# import os
# import csv

# csvpath = os.path.join('budget_data.csv')
# m=0
# total=0
# x=0

# ## The total number of months included in the dataset
# with open(csvpath, newline='') as csvfile:

#     csvreader = csv.reader(csvfile, delimiter=',')
#     csv_header = next(csvreader)
#     #print(f"CSV Header: {csv_header}")
#     for row in csvreader:
#         m = m + 1

# with open(csvpath, newline='') as csvfile:

#     csvreader = csv.reader(csvfile, delimiter=',')
#     csv_header = next(csvreader)
#     for row in csvreader:
#         total += float(row[1])

#         #total += int(col[x])
#         x = x + 1
#                 ### m == row count  
# print(f"Total number of months recorded: {m}")
# print(f"Total: {total}")