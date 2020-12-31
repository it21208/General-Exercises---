import numpy as np
from scipy import stats

N = int(input())
l = [int(x) for x in input().split()]


print(np.mean(l))
print(np.median(l))
print(stats.mode(np.array(l))[0][0])
