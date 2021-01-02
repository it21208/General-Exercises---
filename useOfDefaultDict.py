from collections import defaultdict
'''
The defaultdict tool is a container in the collections class of Python. It's similar to the usual dictionary (dict) container,
but the only difference is that a defaultdict will have a default value if that key has not been set yet.
'''
d = defaultdict(list)
lst=[]

n, m = map(int,input().split())
for i in range(0,n):
    d[input()].append(i+1) 

for i in range(0,m):
    lst=lst+[input()]  

for i in lst: 
    if i in d: print(" ".join( map(str,d[i])))
    else: print('-1')
