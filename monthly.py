#!/usr/bin/python3

import sys
import fileinput
import collections

total=0

ctgs={'Bills': 0, 'Cash': 0, 'Debt': 0, 'EatingOut':0, 'Education': 0, 'Entertainment': 0, 'Fitness': 0, 'Gifts': 0, 'Groceries': 0, 'Personal': 0, 'Pet': 0, 'Savings': 0, 'Travel': 0, 'Work': 0}
act=['Checking', 'Credit']

# for line in fileinput.input():
# 	amount, recurring, automatic, catergory, accttype = line.split()
# 	total += float(amount)
# 	if catergory in ctgs:
# 		ctgs[catergory] = amount + ctgs[catergory]
# 		print(ctgs[catergory], amount, catergory)
# 	else:
# 		print('nope', catergory)
	
# print(total)

