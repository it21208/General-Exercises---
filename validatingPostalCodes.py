'''
A valid postal code  have to fullfil both below requirements:

 must be a number in the range from 100000 to 999999 inclusive.
 must not contain more than ONE alternating repetitive digit pair.
Alternating repetitive digits are digits which repeat immediately after the next digit. In other words, 
an alternating repetitive digit pair is formed by two equal digits that have just a single digit between them.

For example:

121426 # Here, 1 is an alternating repetitive digit.
523563 # Here, NO digit is an alternating repetitive digit.
552523 # Here, both 2 and 5 are alternating repetitive digits.
'''

regex_integer_in_range = r"^[1-9][\d]{5}$" # this regex checks if the postal code is in the required range.
regex_alternating_repetitive_digit_pair = r"(\d)(?=\d\1)" # this regex finds how many alternating repetitive digits the postal code string contains.  

import re
P = input()
 # if the postal code is in the wanted range and if the postal code has only 1 alternating repetitive digit print True.
print(bool(re.match(regex_integer_in_range, P)) and len(re.findall(regex_alternating_repetitive_digit_pair, P)) < 2)  
