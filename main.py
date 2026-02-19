"""
First version of the repeater.
Its goal is to make you repeat your lessons by asking you to complete rows. 
For now, some elements are written directly in the code so I can use it as soon as possible. It will be later improved.

Dependencies :
- pandas
- random
- difflib
"""

import pandas
import random
import difflib
csv_file = "dictionnaire.csv"
nb_wps = 20 # number of words per session

stop = False
df_unclear = pandas.read_csv(csv_file, header='infer')
n = len(df_unclear)
header = df_unclear.columns.values.tolist()
n_header = len(header)
liste = list(range(n_header))

print("When you're wrong, do you want me to highlight the differences ? (Type Y for yes, everything else for no)")
answer = input()
print_diff = answer=="Y"

# Clear the file from non breakable spaces (\xa0) and quotation mark \u20019
df = df_unclear.replace(["\xa0", "\\u2019"],[" ", "'"], regex = True)

while not stop:
	selected_rows = random.sample(range(n),nb_wps)
	i = 0
	for r in selected_rows: # one session starts
		i = i+1
		c = random.randint(0,n_header-1) # which column will be selected
		others = [x for x in liste if x!=c] # not selected columns
		for o in others:
			print("(" + str(i) + ") What is the " + header[o] + " for " + df.iat[r,c] + "?")
			answer = input()
			good = df.iat[r,o]
			if answer == good :
				print("Correct\n")
			else : 
				print("Incorrect, the answer is " + good + " and not " + answer +"\n")
				if print_diff:
					diff_list = difflib.ndiff([good], [answer])
					for diff in diff_list:
						print(diff)
	print("To continue, type Y")
	answer = input()
	stop = answer != "Y"

print("Thanks, have a good day")
