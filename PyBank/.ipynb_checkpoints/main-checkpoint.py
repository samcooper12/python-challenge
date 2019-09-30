
import os

import csv

csvpath = os.path.join('budget_data.csv')

m=0

total=0

## The total number of months included in the dataset
with open(csvpath, newline='') as csvfile:

	csvreader = csv.reader(csvfile, delimiter=',')

	#print(csvreader)

	csv_header = next(csvreader)

	print(f"CSV Header: {csv_header}")

	for row in csvreader:

		m = m + 1
### m is a count of each row and therefore the number. of months tracked in this CSV file. 

	print(f"Total number of months recorded: {m}")

	for row in csvreader:
		#total = sum(int(r[1]) 
		
		total += float(row[1])
	print(total)

