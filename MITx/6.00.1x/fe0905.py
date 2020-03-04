class intSet(object):
    """An intSet is a set of integers
    The value is represented by a list of ints, self.vals.
    Each int in the set occurs in self.vals exactly once."""

    def __init__(self):
        """Create an empty set of integers"""
        self.vals = []

    def insert(self, e):
        """Assumes e is an integer and inserts e into self""" 
        if not e in self.vals:
            self.vals.append(e)

    def member(self, e):
        """Assumes e is an integer
           Returns True if e is in self, and False otherwise"""
        return e in self.vals

    def remove(self, e):
        """Assumes e is an integer and removes e from self
           Raises ValueError if e is not in self"""
        try:
            self.vals.remove(e)
        except:
            raise ValueError(str(e) + ' not found')

    def __str__(self):
        """Returns a string representation of self"""
        self.vals.sort()
        return '{' + ','.join([str(e) for e in self.vals]) + '}'
    
    def __len__(self):
        """returns the number of elements in the set"""
        return len(self.vals)
    
    def intersect(self, other):
        """Returns a new intSet of integers that appear in both sets"""
        newSet = intSet()
        for value in self.vals:
            if value in other.vals:
                newSet.insert(value)
        return newSet

############################################################

a = intSet()
print(list(range(11)))
for i in range(10):
    a.insert(i)

b = intSet()
print(list(range(0, 20, 2)))
for i in range(0, 20, 2):
    b.insert(i)

print(a.intersect(b))

print(len(a))