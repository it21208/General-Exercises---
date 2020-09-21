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
    
    if __name__ == '__main__':
        print('Παρακαλώ εισάγετε τον αριθμό')
        N = input()
        tempList = []
        for i in range(N):
            a = random.uniform(-2.0, 2.99)
            b = random.uniform(-2.0, 2.99)
            tempList.append([a,b])
            
       cnt1 = 0
       cnt2 = 0
        
        for idx, i in enumerate(tempList):
            interval1 = Interval(i[0], i[1])
            other = Interval(0,0)
            
            if interval1.intersects(other) == True:
                cnt1 += 1
                
            if interval1.contains(0) == True:
                cnt2 += 1
                
       print(cnt1, " διαστήματα τέμνονται από το διάστημα 0")
       print(cnt2, " διαστήματα περιέχουν το 0")
