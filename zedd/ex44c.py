# 继承与组合之在运行前/后替换

## 继承的这个第三种方法是「覆盖」的一个特例

# Parent is-a object
class Parent(object):
    
    def altered(self):
        print("PARENT altered()")

# make a class named Child that is-a Parent
class Child(Parent):
    
    def altered(self):
        print("CHILD, BEFORE PARENT altered()")
        
        ## 玩一玩
        print("test: ")
        Parent.altered(self)
        print("test end. ")
        ## 玩一玩
        
        # 用Child和self两个参数调用super()，然后在此返回的基础上调用altered
        # 什么意思？
        # super(Child, self)的结果就是Parent，也就是说这句代码最终相当于Parent.altered()
        super(Child, self).altered()
        # 你看，跟上面那个“玩一玩”的输出结果是一样的
        print("CHILD, AFTER PARENT altered()")
        
# set dad to an instance of class Parent
dad = Parent()
print('-1-')
# set son to an instance of class Child
son = Child()

print('-2-')
dad.altered()
print('-3-') # 调试用；仔细看输出结果
son.altered()