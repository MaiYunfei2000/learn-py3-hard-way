# 此练习中学习了if、elif（应该是else if的意思吧）、else。在这里else与另外两者的关系应该是 else为(if和elif)的否定，也就是if和elif条件的交集的补集。

people = 30
cars = 40
trucks = 15

# 如果cars大于people
if cars > people:
    print("We should take the cars.")
# 又或者如果cars小于people
elif cars < people:
    print("We should not take the cars.")
# 如果cars既不大于也不小于people，也就是cars等于people
else:
    print("We can't decide.")

if trucks > cars:
    print("That's too many trucks.")
elif trucks < cars:
    print("Maybe we could take the trucks.")
else:
    print("We still can't decide.")


if people > trucks:
    print("Alright, let's just take the trucks.")
else:
    print("Fine, let's stay home then.")