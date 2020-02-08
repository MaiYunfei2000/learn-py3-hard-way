##### [Problem 3 | Problem Set 2 | 6.00.1x Courseware | edX](https://courses.edx.org/courses/course-v1:MITx+6.00.1x+1T2020/courseware/0de4fecc5a9a4749923133fcf4de181f/e137765987514da7851a59dedeb5ecec/?activate_block_id=block-v1%3AMITx%2B6.00.1x%2B1T2020%2Btype%40sequential%2Bblock%40e137765987514da7851a59dedeb5ecec)
"""
Problem 2的二分法版本。并且精确到分（两位小数）。
"""

"""
 Test Case 1:
	      balance = 320000
	      annualInterestRate = 0.2

	      Result Your Code Should Generate:
	      -------------------
	      Lowest Payment: 29157.09   
                  
Test Case 2:
	      balance = 999999
	      annualInterestRate = 0.18
	      
	      Result Your Code Should Generate:
	      -------------------
	      Lowest Payment: 90325.03
"""

balance = 999999
annualInterestRate = 0.18

#########

epsilon = 0.01
monthlyInterestRate = annualInterestRate / 12

def yearEndBalance(payment):
    remainingBalance = balance
    for month in range(1, 13):
        monthlyUnpaidBalance = remainingBalance - payment
        remainingBalance = monthlyUnpaidBalance * (1 + monthlyInterestRate)
    return remainingBalance

# 如果每月还完本金的1/12，那么因利息而必还不完
lower = balance / 12
# 如果一年之后一次性还完本金，那么所需还的利息是最多的
upper = balance * ((1 + monthlyInterestRate) ** 12) / 12

while upper - lower > epsilon:
    payment = (lower + upper) / 2
    lowestPayment = yearEndBalance(lower)
    ans = yearEndBalance(payment)
    
    if lowestPayment * ans < 0:
        upper = payment
    elif lowestPayment * ans > 0:
        lower = payment
    else:
        break

print("Lowest Payment:", round(payment, 2))