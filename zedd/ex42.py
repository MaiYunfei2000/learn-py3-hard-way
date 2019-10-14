# an object is an instance of a class
# a subclass is a class that is an object/instance of a class which is its supclass

## [origin]Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    pass

## make a class named Dog that is-a Animal.
class Dog(Animal):
    
    # class Dog has-a __init__ that takes self and name params.
    def __init__(self, name):
        ## Dog has-a name of some kind??????????
        self.name = name
    
## make a class named Cat that is-a Animal.
class Cat(Animal):
    
    def __init__(self, name):
        ## ??
        self.name = name

## make a class named Person that is-a object.
class Person(object):
    
    # class Person has-a __init__ that takes self and name params.
    def __init__(self, name):
        ## ??
        self.name = name

        ## [origin]Person has-a pet of some kind.
        self.pet = None

## make a class named Employee that is-a Person.
class Employee(Person):
    
    # class Employee has-a __init__ that takes self, name and salary parums.
    def __init__(self, name, salary):
        ## [origin]?? hmm what is this strange magic?
        # 所以到底是什么鬼……
        super(Employee, self).__init__(name)
        ## Employee has-a salary of some kind.
        self.salary = salary

## make a class named Fish that is-a object.
class Fish(object):
    pass

## make a class named Salmon that is-a Fish.
class Salmon(Fish):
    pass

## make a class named Halibut that is-a Fish.
class Halibut(Fish):
    pass


## [origin]rover is-a Dog
rover = Dog("Rover")
# so what does "Rover" mean?

## stan is-a Cat
satan = Cat("Satan")

## mary is-a Person
mary = Person("Mary")

## From mary get the pet attribute and set it to satan
mary.pet = satan

## frank is-a Employee
# Set frank to an instance of class Employee and takes "Frank" as name and 120000 as salary ?????????
frank = Employee("Frank", 120000)

## From frank get the pet attribute and set it to rover
frank.pet = rover

## set flipper to an instance of class Fish
flipper = Fish()

## set crouse to an instance of class Salmon
crouse = Salmon()

## set harry to an instance of class Halibut
harry = Halibut()