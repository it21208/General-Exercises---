import numpy as np
import pandas as pd


np_arr = np.array([[1,2,3],[4,5,6]])
print('Shape of np_arr = {}'.format(np_arr.shape))

for idx, row in enumerate(np_arr):
    print(str(idx)+'\t', row,)
    print('********')
    for idx2, item in enumerate(row):
        print(idx2, item)
    

df = pd.DataFrame(np_arr)
print('df type = {}'.format(type(df))) 

data = ("John", "Doe", 53.44)
format_string = "Hello"

print(format_string, '%s with surname %s and ' \
                     'balance %d' % (data[0], data[1], data[2]))
