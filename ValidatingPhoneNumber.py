import re
while True:
    N = input()
    if len(N)>= 1 and len(N) <= 10:
        break
    
strings = []
for i in range(int(N)):
    while True:
        number = input()
        if len(number) >= 2 and len(number) <= 15:
            break
    strings.append(number)
    
for i in strings:
    try:
        if len(i) == 10 and int(i[0]) in [7,8,9] and i.isnumeric() == True:
            print('YES')
        else:
            print('NO')
    except:
        print('NO')
