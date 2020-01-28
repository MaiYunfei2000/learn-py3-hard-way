#1
print('\n', "#1", '\n')

for i in range(2, 12, 2):
    print(i)

print("Goodbye!")

#2
print('\n', "#2", '\n')

ls = list(range(2, 12, 2))
ls.reverse()

print("Hello!")

for i in ls:
    print(i)

# 3
print('\n', "#3", '\n')

num = 0

for i in range(1, end+1):
    num += i

print(num)