import re
for i in range(int(input())):
    print(bool(re.search(r"^[+-]?\d*\.\d+$",input().strip())))
    
''' input '''
#4
#4.0O0
#-1.00
#+4.54
#SomeRandomStuff

''' output '''
#False
#True
#True
#False
