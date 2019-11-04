class Other(object):
    
    def override(self):
        print("OTHER override()")
    
    def implicit(self):
        print("OTHER implicit()")
    
    def altered(self):
        print("OTHER altered()")

class Child(object):
    
    def __init__(self):
        # other is-a Other
        self.other = Other()
    
    def implicit(self):
        self.other.implicit()
    
    def override(self):
        print("CHILD override()")
    
    def altered(self):
        print("CHILD, BEFORE OTHER altered()")
        self.other.altered()
        print("CHILD, AFTER OTHER altered()")

son = Child()

son.implicit()
son.override()
son.altered()

# 巩固练习：读一读http://www.python.org/dev/peps/pep-0008/并试着在代码中使用它
'''
* [PEP 8 -- Style Guide for Python Code | Python.org](https://www.python.org/dev/peps/pep-0008/)
* [Python PEP-8编码风格指南中文版](https://alvinzhu.xyz/2017/10/07/python-pep-8/)
* [PEP8中文版 -- Python编码风格指南](https://python.freelycode.com/contribution/detail/47)
'''