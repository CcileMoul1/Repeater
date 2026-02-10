"""
First version of the repeater.
Its goal is to make you repeat your lessons by asking you to complete rows. 
For now, some elements are written directly in the code so I can use it as soon as possible. It will be later improved.

Dependencies :
- pandas
- random
"""

import pandas
import random
csv_file = "dictionnaire.csv"
nb_wps = 20 # number of words per session

stop = False
df = pandas.read_csv(csv_file, header='infer')
n = len(df)
header = df.columns.values.tolist()
n_header = len(header)
liste = list(range(n_header))

while not stop:
	for i in range(20): # one session starts
		r = random.randint(0,n-1) # which row will be selected
		c = random.randint(0,n_header-1) # which column will be selected
		others = [x for x in liste if x!=c]
		for o in others:
			print("(" + str(i+1) + ") What is the " + header[o] + " for " + df.iat[r,c] + "?")
			answer = input()
			if answer == df.iat[r,o] :
				print("Correct")
			else : 
				print("Incorrect, the answer is " + df.iat[r,o] + " and not " + answer)
	print("To continue, write Y")
	answer = input()
	stop = answer != "Y"

print("Thanks, have a good day")
