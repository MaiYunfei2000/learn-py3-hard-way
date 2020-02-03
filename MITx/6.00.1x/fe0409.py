##### [Exercise: fourth power](https://courses.edx.org/courses/course-v1:MITx+6.00.1x+1T2020/jump_to/block-v1:MITx+6.00.1x+1T2020+type@vertical+block@ef412f1bdebd43ca8c053210f2971c95)

# Write a Python function, "fourthPower", that takes in one number and returns that value raised to the fourth power.

# You should use the "square" procedure that you defined in an earlier exercise (you don't need to redefine "square" in this box; when you call "square", the grader will use our definition).

def square(x):
    '''
    x: int or float.
    '''
    return x ** 2

##########

def fourthPower(x):
    '''
    x: int or float.
    '''
    return square(square(x))