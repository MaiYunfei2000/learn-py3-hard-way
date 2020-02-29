"""
Consider the function "normalize" that takes as input a list of 
positive numbers "numbers" and returns a list of numbers that are 
a fraction of the maximum element in the list. Try to answer the 
questions without running the code. Check your answers, then run 
the code for the ones you get wrong. You'll learn the most this 
way, by figuring things out, instead of just running the code and 
reading off the answers.
"""

def normalize(numbers):
    max_number = max(numbers)
    for i in range(len(numbers)):
        numbers[i] /= float(max_number)
    return numbers

"""
The code below tries to call "normalize" with one particular input.
Answer the next 5 questions based on the following code.
"""

try:
    normalize([0, 0, 0])
except ZeroDivisionError:
    print('Invalid maximum element')



"""
Now assume the definition of the function normalize is rewritten as 
followsNow assume the definition of the function normalize is 
rewritten as follows:
"""

def normalize(numbers):
    max_number = max(numbers)
    assert(max_number != 0), "Cannot divide by 0"
    for i in range(len(numbers)):
        numbers[i]  /= float(max_number)
        assert(0.0 <= numbers[i] <= 1.0), "output not between 0 and 1"
    return numbers        