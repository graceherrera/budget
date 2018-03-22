Budget program will ask for the current paycheck that you are applying to this set of bills and the current account balance so that you can get a correct balance when you are through paying bills.

The program reads in a file with list of bills and amounts. It compares the bills to a set of dictionaries some of which get updated with new balances after some of the debt is paid off.

### budget.py 
  reads in file with date on it
  reads extra.json -- current debt that we are working to pay off. populates the extras dictionary
  reads bills.json -- current list of bills with static balances. populates the bills dictionary.
  writes out the report named after the current date.
  based off the balances that you assigned the bills dictionary it will let you know if you are completely off base with what you are actually paying.
  If you have a bill that you didn't budget for - it will show up as an unnacounted for bill.
### schedules.py
  Will read in the same bill list and date and will give have a list of bills that should be paid during this period and a list of bills that should have been paid already. And the a list of bills for next cycle of bills. 
