

#!/usr/bin/env python
# coding: utf-8

# In[136]:


import os
import csv
import time
#import threading
from threading import Timer

csvpath = os.path.join('budget_data.csv')
m=0
total=0
net_total=0
x=0
new_total=0
avg_change=0
l = []
maxt = 0
mint = 0
maxm = []
minm = []
y = 0


# In[137]:
print("\n")
print("\n")


### The total number of months included in the dataset
with open(csvpath, newline='') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    for row in csvreader:
        m = m + 1


# In[138]:


### net total for profit column
with open(csvpath, newline='') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    for row in csvreader:
        total += int(row[1])
        x = x + 1


# In[139]:


### The average of the changes in "Profit/Losses" over the entire period
with open(csvpath, newline='') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    
    avg_change = (total/m)

# In[141]:


### The greatest increase in profits (date and amount) over the entire period
with open(csvpath, newline='') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    for row in csvreader:
        
        maxt = max(maxt,int(row[1]))
        #maxm = max(maxt,int(row[0]))
        mint = min(mint,int(row[1]))
        #minm = max(mint,int(row[0]))
        
    # print(maxt, maxm)
    # print(mint, minm)


with open(csvpath, newline='') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    
    for row in csvreader:
        
        # NOTE: To surface the month names while accomodating for whether multiple months
        # have the same max or min --  I . made these variables a list datatype (hence the weird print format)

            if int(row[1]) == maxt:
                maxm.append(row[0])
                print(f"Month of largest profit: {maxm}")
            
            elif int(row[1]) == mint:
                minm.append(row[0])
                print(f"month of largest losses: {minm}")


print(f"Running financial analysis...")
print(f"analysis complete")
print(f"------------------------------------------")
print(f"Number of months recorded: {m}")
print(f"Net total profit: {'${:,.2f}'.format(total)}")
print(f"Average monthly net profit/loss: {'${:,.2f}'.format(avg_change)}")
print(f"Largest profit in a month: {'${:,.2f}'.format(maxt)} {maxm}")
print(f"Largest loss in a month: {'${:,.2f}'.format(mint)} {minm}")
print(f"------------------------------------------")
print("\n")
