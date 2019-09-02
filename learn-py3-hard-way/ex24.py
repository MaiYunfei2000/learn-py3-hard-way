print("Let's practice everything.")
# \'打印单引号；\\打印右斜杠。
print('You\'d need to know \'bout escapes with \\ that do:')
# \n打印新一行；\t打印tab。
print('\n newlines and \t tabs.')

# 将一段长字符串赋给变量poem。
poem = """
\t The lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""

# 打印字符串“--------”。
print("--------")
# 打印变量poem。
print(poem)
print("--------")

# 计算10-2+3-6赋给变量five。
five = 10 - 2 + 3 - 6
print(f"This should be five: {five}")

# 定义函数secret_formula()，started为函数的参数。
def secret_formula(started):
    # started*50的值赋给jelly_beans。
    jelly_beans = started * 500
    # jelly_beans/1000的值赋给jars。
    jars = jelly_beans / 1000
    crates = jars / 100
    # 返回jelly_beans, jars, crates这三个变量的值。
    return jelly_beans, jars, crates


start_point = 10000
# 将start_point的作为secret_formula()的参数运行，并把函数返回的值依次赋给beans，jars，crates三个变量。
beans, jars, crates = secret_formula(start_point)

# remember that this is another way to format a string
print("With a starting point of: {}".format(*start_point))
# it's just like with an f"" string
print(f"We'd have {beans} beans, {jars} jars, and {crates} crates.")

start_point = start_point / 10

print("We can also do that this way:")
# 这里将函数返回的值打包赋给变量formula。
formula = secret_formula(start_point)
# this is an easy way to apply a list to a format string
# 用这种方式可以少打一点代码实现与前面相同的效果。
print("We'd have {} beans, {} jars, and {} crates.".format(*formula))