"""
Amanda has a string,s, of m lowercase letters that she wants to copy into a new string,p. She can perform the following operations any number of times to construct string p :

Append a character to the end of string p at a cost of 1 dollar.
Choose any substring of p and append it to the end of p at no charge.
Given  string, find and print the minimum cost of copying each si to pi on a new line.

Input Format

The first line contains a single integer,n, denoting the number of strings. 
Each line i of the n subsequent lines contains a single string,si.

"""

import sys

n = int(raw_input().strip())

for a0 in xrange(n):
    
    s = raw_input().strip()

    lst = list(str(s))
    
    cost = 0
    p = ''
    for i in lst:
        
        if i not in p:
            
            p = p + str(i)
            cost = cost + 1
            
        else:
            p = p + str(i)
            cost = cost + 0
            
    print cost
            