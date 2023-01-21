# regex.py
"""
.           Matches any single charactrer except the newline character
^           Matches a pattern at the start of the string
$           Matches the end of the string
[]          Matches the set of characters you specify within it
\           Escapes a metacharacter
\w          Matches any single letter, digit, or underscore
\W          Matches any character not part of \w
\s          Matches a single whitespace character like: space, newline, tab,return
\S          Matches any character not part of \s
\d          Matches decimal digit 0-9
\D          Matches any character that is not a decimal digit
+           Checks if the preceding character appears one or more times
*           Checks if the preceding character appears zero or more times
?           Checks if the preceding character appearsl exactly zereo or one time
{}          Checks for an explicit number of times
"""

import re

re.search('\w{4}\d{4}', 'My password is abcd1234.') 
# <re.Match object; span=(12, 23), match='abcd1234'>

re.match('\w{4}\d{4}', 'My password is abcd1234.')  # match only finds if at beginning of string
# no match

re.match('\w{4}\d{4}', 'abcd1234 is my password')
# <re.Match object; span=(0, 8), match='abcd1234'>

re.findall(r'\d{1,3}', 'My 3 cats have 15 kittens')
# ['3', '15']

re.sub('\d', ' ', 'My1house2has3white4walls')   # the regex, the replacement, and the string
# 'My house has white walls'

my_string = "My&name&is#John Smith. I%live$in#London."
re.sub(r"[#$%&]", " ", my_string)
# 'My name is John Smith. I live in London.'

def validate_password(password): 
     if re.match(r"\d{4,8}[a-zA-Z]{2,}.*[^!@$%&]$", password):
         print(f"Valid Password {password}")
     else:
         print(f"Invalid Password {password}")

validate_password('4390Abac!')
# Invalid Password 4390Abac!

validate_password('4390Abac!1')
# Valid Password 4390Abac!1

my_date = 'Your appointment has been confirmed for 1st of september 2022 18:30'
regex = r"\d{1,2}[a-z]{2}\sof\s[a-zA-Z]+\s\d{4}\s\d{1,2}:\d{2}"
re.findall(regex, my_date)
# ['1st september 2022 18:30']
