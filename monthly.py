#!/usr/bin/python3

import sys
import fileinput
import collections
import time
import datetime
from datetime import date


now = datetime.date.today()
name = 'Expenses as of ' + str(now)
report_name = 'Expenses ' + str(now)

total=0

ctgs={'Bills': 0, 'Cash': 0, 'Debt': 0, 'EatingOut':0, 'Education': 0, 'Entertainment': 0, 'Fitness': 0, 'Gifts': 0, 'Groceries': 0, 'Personal': 0, 'Pet': 0, 'Savings': 0, 'Travel': 0, 'Work': 0}
checking = 0
credit = 0

for line in fileinput.input():
	amount, recurring, automatic, catergory, accttype = line.split()
	total += float(amount)
	if catergory in ctgs:
		ctgs[catergory] = float(amount) + ctgs[catergory]
		# if catergory == 'EatingOut':
		# 	print(ctgs[catergory], amount, catergory)
		#print(ctgs[catergory], amount, catergory)
	else:
		print('nope', catergory)

	if accttype == 'Checking':
		checking = checking + float(amount)
	else:
		credit = credit + float(amount)

with open(report_name, 'w') as report:
	report.write(name)
	report.write('\nThe total spent this month is {}\n'.format(total))
	report.write("\n".join("{}\t{}".format(k, v) for k, v in ctgs.items()))
	report.write('\nThe total spent from checking account is {}'.format(checking))
	report.write('\nThe total spent from credit cards is {}'.format(credit))
	
print('Please check the {} file it should have all the information you need'. format(report_name))

