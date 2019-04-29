# 建立有数据的表格，将其赋给变量
the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# this first kind of for-loop goes through a list
# 将the_count里的一个个值都赋给number，循环执行下一行语句
for number in the_count:
    print(f"This is count {number}")

# same as above
for fruit in fruits:
    print(f"A fruit of type: {fruit}")

# also we can go through mixed lists too
# notice we have to use {} since we don't know what's in it
for i in change:
    print(f"I got {i}")

# we can also build lists, first start with an empty one
elements = []

# then use the range function to do 0 to 5 counts
# 依次产生0~5的整数，一个个赋给变量i，执行5次下一行语句
for i in range(0, 6):
    print(f"Adding {i} to the list.")
    # append is a function that lists understand
    # 将i的每一个值形成一个表格赋给变量elements
    elements.append(i)

# now we can print them out too
for i in elements:
    print(f"Element was: {i}")