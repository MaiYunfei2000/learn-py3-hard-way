def isInt(num):
    # try和except是什么作用？
    try:
        num = int(str(num))
        return isinstance(num, int)
    except:
        return False

choice = (isInt(input("> ")))

print(choice)