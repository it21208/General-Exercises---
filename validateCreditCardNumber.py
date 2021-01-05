'''
It must start with a 4, 5 or 6.
It must contain exactly 16 digits.
It must only consist of digits (0-9).
It may have digits in groups of 4, separated by one hyphen "-".
It must NOT use any other separator like ' ' , '_', etc.
It must NOT have 4 or more consecutive repeated digits
'''

import re
from itertools import groupby

for i in range(int(input())):
    number = input()
    if number[0] in ['4','5','6']:
        if len(number.replace("-", "")) == 16:    
            if (number.replace("-", "")).isdigit() == True:
                if not re.search(r'[^0-9-]', number):
                    if not max(len(list(g)) for _, g in groupby(number)) >= 4:
                        print('Valid')
                    else:
                        print('Invalid')
                else:
                    print('Invalid')
            else:
                print('Invalid')
        else:
            print('Invalid')
    else:
        print('Invalid')
