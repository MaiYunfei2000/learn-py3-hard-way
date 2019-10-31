# 本节在前面OOP的基础上来接受继承与组合的洗礼

# 隐式继承

## 在父类里定义一个函数但没有在子类里定义时会发生的隐式行为

class Parent(object):
    
    def implicit(self):
        print("PARENT implicit()")

class Child(Parent):
    # pass用来创建空代码块，可让你弄出徒有其表的类及函数
    pass

dad = Parent()
son = Child()

dad.implicit()
son.implicit()