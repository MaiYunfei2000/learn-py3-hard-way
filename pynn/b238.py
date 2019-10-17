# 2.3.8 对象

# class for a dog object
class Dog:
    
    # dogs can bark()
    def bark(self):
        print("woof!")
        pass
    
    pass

# set sizzles to an instance of Dog
sizzles = Dog()
mutley = Dog()
# from sizzles get the bark function
sizzles.bark()
mutley.bark()
# 原来对象的作用是这样，如果仅仅是bark()，会报错name 'bark' is not defined，必须要从属于Dog类的sizzles里面获取这个函数
# sizzles和mutley都属于class Dog，因此它们都会bark！

# 再来一次！

# class for a dog object
class Dog:
    
    # initialisation method with internal data
    def __init__(self, petname, temp):
        self.name = petname
        self.temperature = temp
        
    # get status
    def status(self):
        print("dog name is ", self.name)
        print("dog tempreture is ", self.temperature)
        pass
    
    # set temperature
    def setTemperature(self, temp):
        self.temperature = temp
        pass
        
    # dogs can bark()
    def bark(self):
        print("woof!")
        pass
    
    pass
# 也许，self的部分意义在于，使得petname和temp变量是这个对象本身的部分，只属于这个对象而独立于其它Dog对象和Python中的一般的变量（比如在这个class之外定义的变量name和temperature
# （猜测↑）
    
# create a new dog object from the Dog class
lassie = Dog("Lassie", 37)
lassie.status()

lassie.setTemperature(40)
lassie.status()