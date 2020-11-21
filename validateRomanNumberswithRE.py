regex_pattern = r"^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$"	# Do not delete 'r'.

import re
print(str(bool(re.match(regex_pattern, input()))))

'''
The bool() function returns the boolean value of a specified object.
The object will always return True, unless:
The object is empty, like [], (), {}
The object is False
The object is 0
The object is None
'''
