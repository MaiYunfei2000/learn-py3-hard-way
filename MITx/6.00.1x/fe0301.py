#3 What is broken by "break", the while loop or the for loop?

iteration = 0
while iteration < 5:
    count = 0
    
    print("debug# print interation:", iteration)
    
    for letter in "hello, world":
        count += 1
        
        print("debug# print count:", count)
        
        if iteration % 2 == 0:
            break
    print("Iteration " + str(iteration) + "; count is: " + str(count))
    iteration += 1 