"""
Alice wrote a sequence of words in CamelCase as a string of letters, , having the following properties:

It is a concatenation of one or more words consisting of English letters.
All letters in the first word are lowercase.
For each of the subsequent words, the first letter is uppercase and rest of the letters are lowercase.
Given , print the number of words in  on a new line.

Input Format

A single line containing string s.

Constraints

Output Format

Print the number of words in string s.

"""

import sys
import re
s = raw_input().strip()

count = 0
result = []
small_letters = re.findall('[a-z]*',s)
capital_letters = re.findall('[A-Z][a-z]*', s)

letter = small_letters[0]
result.append(letter)

for i in capital_letters:
    result.append(i)
    
for c in result:
    
    count = count + 1
    
print small_letters