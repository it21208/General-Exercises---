import torch
import numpy as np
a = np.ones(5)
print(a)
b = torch.from_numpy(a)
print(b)
print(type(b))
np.add(a, 1, out=a)
print(a)
print(b)