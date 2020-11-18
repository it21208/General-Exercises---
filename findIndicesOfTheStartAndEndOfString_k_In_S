import re

S = input()
k = input()

anymatch = False
for m in re.finditer(r'(?=('+k+'))',S):  # noted
    anymatch = True
    print((m.start(1),m.end(1)-1))
if not anymatch:
    print((-1, -1))
    

# Sample Input
#aaadaa
#aa

#Sample Output
#(0, 1)  
#(1, 2)
#(4, 5)
