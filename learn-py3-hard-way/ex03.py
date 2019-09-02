# 这个练习是为了让我学会输出基础运算的结果。

print("I will now count my chickens:") # 输出文字“I will now count my chickens:”。

print("Hens", 25 + 30 / 6) # 输出文字“Hens”和25加30除以6的运算结果。如果有除法，即便结果有整数，也会有小数点（一位）。
print("Roosters", 100.0 - 25 * 3 % 4) # 输出文字“Roosters”和100.0减去((25乘以3)除以4的余数)的运算结果。
# 输入100，输出结果是整数，输入100.0，输出结果携带一位小数。

# 我明白了，"%"的作用是：对符号前面运算所得值除以符号后的数并取余数。

print("Now I will count the eggs:")

print(3.0 + 2.0 + 1.0 - 5.0 + 4.0 % 2.0 - 1.0 / 4.0 + 6.0)

print("Is it true that 3 + 2 < 5 - 7?")

print(3 + 2 < 5 - 7) # 输出：式子(3 + 2 < 5 - 7)的正误判断

print("What is 3 + 2?", 3 + 2) # 输出：文字“What is 3 + 2?”和(3 + 2)的运算结果
print("What is 5 - 7?", 5 - 7)

print("Oh, that's why it's False.")

print("How about some more.")

print("Is it greater?", 5 > -2)
print("Is it greater or equal?", 5 >= -2)
print("Is it less or equal?", 5 <= -2)
