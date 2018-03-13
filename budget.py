#!/usr/bin/python3

import sys
import fileinput
import time
import datetime

income = 2500
leftover = 0
rbills = 0
ebills = 0
ubills = 0
total_bills = 0

bills={'rent':1100, 'internet': 45, 'dramafever': 10, 'car': 465, 'utilities': 225, 'phones': 345, 'netflix': 14}
extras={'gcc':6000, 'paypal':4000, }

beginning = ['rent', 'internet']

for line in fileinput.input():
    bill, amount = line.split()
    if bill in bills:
        rbills += float(amount)
        if float(bills[bill]) != float(amount):
            print('{} is budgeted for ${} and the bill is actually ${}. You saved ${}'.format(bill, bills[bill], amount, float(bills[bill])- float(amount)))
    elif bill in extras:
        ebills += float(amount)
        if float(extras[bill]) != float(amount):
            print('The amount you owe for {} is ${}. You have made a payment for ${}. Your new balance is {}'.format(bill, extras[bill], amount, float(extras[bill])- float(amount)))
            new_balance = float(extras[bill]) - float(amount)
            extras[bill] = new_balance
            print(extras)
    else:
        ubills += float(amount)
print('The total extra bills this pay period are: ${}'.format(ebills))
print('The total unaccounted for bills are: ${}'.format(ubills))
total_bills = ebills + rbills + ubills
leftover = income - total_bills
print('The total bills for this period are {}. You have leftover {}'.format(total_bills, leftover))
