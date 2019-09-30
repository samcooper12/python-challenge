#three columns: `Voter ID`, `County`, and `Candidate`.

import os
import csv

m = 0
candidates = []
w = 0
ww = 0
www = 0
wwww = 0
r_a = 0.000
r_b = 0.000
r_c = 0.000
r_d = 0.000

csvpath = os.path.join('Resources/election_data.csv')

print("\n")

#The total number of votes cast

with open(csvpath, newline='') as csvfile:

	csvreader = csv.reader(csvfile, delimiter=',')
	csv_header = next(csvreader)

	for row in csvreader:
		m = m + 1

print(f"Total Votes Cast: {m}")

#A complete list of candidates who received votes
with open(csvpath, newline='') as csvfile:

	csvreader = csv.reader(csvfile, delimiter=',')
	csv_header = next(csvreader)

	for row in csvreader:
		if row[2] not in candidates:
			candidates.append(row[2])

	#count = len(candidates)

print(f"All Candidates Receiving Votes: {candidates}" )

#The percentage of votes each candidate won

totals = []

with open(csvpath, newline='') as csvfile:

	csvreader = csv.reader(csvfile, delimiter=',')
	csv_header = next(csvreader)

	for row in csvreader:
		if row[2] == candidates[0]:
			w = w + 1
		elif row[2] == candidates[1]:
			ww = ww + 1
		elif row[2] == candidates[2]:
			www = www + 1
		elif row[2] == candidates[3]:
			wwww = wwww + 1

	r_a= round((w/m),3)
	r_b= round((ww/m),3)
	r_c= round((www/m),3)
	r_d= round((wwww/m),3)
	print(f"\n" + "Percentage of Vote by Candidate:")
	print(f"->{candidates[0]} ~ {r_a}%")
	print(f"->{candidates[1]} ~ {r_b}%")
	print(f"->{candidates[2]} ~ {r_c}%")
	print(f"->{candidates[3]} ~ {r_d}%")

	#rounding check
			#print(r_a + r_b + r_c + r_d)

# #The total number of votes each candidate won
	print(f"\n" + "Total per Candidate:")
	print(f"->{candidates[0]} ~ {w}")
	print(f"->{candidates[1]} ~ {ww}")
	print(f"->{candidates[2]} ~ {www}")
	print(f"->{candidates[3]} ~ {wwww}")
	print(f"\n")

# #The winner of the election based on popular vote.

	if (w > ww, www, wwww):
		print(f"{candidates[0]} wins!")

	elif (ww > (w, www, wwww)):
		print(f"{candidates[1]} wins!")

	elif (www > (w, ww, wwww)):
		print(f"{candidates[2]} wins!")

	elif (wwww > (w, ww, www)):
		print(f"{candidates[3]} wins!")
	else:
		print("ELECTION FRAUD!")

print("\n")
