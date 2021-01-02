'''
Problem Description:

You are given a string S. It consists of alphanumeric characters, spaces and symbols(+,-).
Your task is to find all the substrings of S that
     - contains 2 or more vowels,
     - also these substrings must lie in between 2 consonants, and
     - should contain vowels only.
'''

import re

vowels = "aeiou"
consonants = "qwrtypsdfghjklzxcvbnm"

#>>> import re
#>>> print(re.I)
#RegexFlag.IGNORECASE

m = re.findall(r"(?<=[%s])([%s]{2,})[%s]" % (consonants, vowels, consonants), input(), flags = re.I)
print('\n'.join(m or ['-1']))


''' 
Sample Input:

rabcdeefgyYhFjkIoomnpOeorteeeeet

Sample Output:

ee
Ioo
Oeo
eeeee

'''
