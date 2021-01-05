import math 
AB = int(input())
BC = int(input())
hype=math.hypot(AB,BC)                      #to calculate hypotenuse
res=round(math.degrees(math.acos(BC/hype))) #to calculate required angle                 
print(res,'°', sep='')
