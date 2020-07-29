import sys

class Interval:
    
    def __init__(self, a, b):
        self.a = a
        self.b = b
        if self.b <= self.a:
            print('a must be smaller than b. Please run it again by entering correct values.')
            sys.exit()
            
    
    def contains(self, n):
        if n >= self.a and n <= self.b:
            return(True)
        else:
            return(False)
    
    def __str__(self):
        return('['+self.a+','+self.b+']')
    
    def intersects(self, other):
        
        if self.a <= other.a and other.b <= self.b:
            return True
        
        if other.a <= self.a and other.b <= self.b:
            return True
        
        if self.a <= other.a and self.b <= other.b:
            return False
        
        return(False)