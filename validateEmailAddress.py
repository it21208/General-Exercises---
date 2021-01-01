import re

def fun(s):
  ''' 
  Valid email addresses must follow these rules:
  It must have the username@websitename.extension format type.
  The username can only contain letters, digits, dashes and underscores.
  The website name can only have letters and digits.
  Τhe maximum length of the extension is 3.
  '''
  pattern = re.compile("^[\\w-]+@[0-9a-zA-Z]+\\.[a-z]{1,3}$")
  return pattern.match(s)

def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    emails = []
    for _ in range(int(input())):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)
