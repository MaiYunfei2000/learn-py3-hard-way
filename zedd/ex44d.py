# a class named Parent is-a object
class Parent(object):
    
    # class Parent has-a override that takes self param
    def override(self):
        print("PARENT override()")
     
    # class Parent has-a implicit that takes self param   
    def implicit(self):
        print("PARENT implicit()")
    
    # class Parent has-a altered that takes self param
    def altered(self):
        print("PARENT altered()")

# make a class named Child that is-a Parent
class Child(Parent):
    
    # class Child has-a override that takes self param
    def override(self):
        print("CHILD override()")
    
    # class Child has-a altered that takes self param
    def altered(self):
        print("CHILD, BEFORE PARENT altered()")
        super(Child, self).altered()
        print("CHILD, AFTER PARENT altered()")

# dad is-a Parent
dad = Parent()
# son is-a Child
son = Child()

print()

# from dad get the function implicit
dad.implicit()
# from son get the function implicit
son.implicit()

print()

dad.override()
son.override()

print()

dad.altered()
son.altered()