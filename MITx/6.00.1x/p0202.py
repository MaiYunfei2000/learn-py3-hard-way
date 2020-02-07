"""
Now write a program that calculates the minimum fixed monthly payment 
needed in order pay off a credit card balance within 12 months. By a 
fixed monthly payment, we mean a single number which does not change 
each month, but instead is a constant amount that will be paid each 
month.

The program should print out one line: the lowest monthly payment that 
will pay off all debt in under 1 year.
"""
# 噢，原来问题反过来了。。。设定每月最低月供为常数，要求出能在一年内还清债务情况下的最低月供。

"""
Test Case 1:
	      balance = 3329
	      annualInterestRate = 0.2

	      Result Your Code Should Generate:
	      -------------------
	      Lowest Payment: 310

Test Case 2:
	      balance = 4773
	      annualInterestRate = 0.2
	      
	      Result Your Code Should Generate:
	      -------------------
	      Lowest Payment: 440

Test Case 3:
	      balance = 3926
	      annualInterestRate = 0.2

	      Result Your Code Should Generate:
	      -------------------
	      Lowest Payment: 360
"""
import time

balance = 3926
annualInterestRate = 0.2

##########

monthlyInterestRate = annualInterestRate / 12
payment = 10

while True:
    remainingBalance = balance
    for month in range(1, 13):
        monthlyUnpaidBalance = remainingBalance - payment
        remainingBalance = monthlyUnpaidBalance * (1 + monthlyInterestRate)
    if remainingBalance < 0:
        break
    else:
        payment += 10

print("Lowest Payment:", payment)