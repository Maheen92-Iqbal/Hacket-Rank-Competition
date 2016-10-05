import itertools

s = raw_input().strip()
re = []
count = 0

#uptill the length of the string we made 4 tuple combinations
r = list(itertools.combinations(range(0,len(s)), r=4))

#we go through the list and extract each tuple
for i in r:
    
    result = ''
    for j in i:
        
        #according to the position in the tuple we formulate a 4 digit word
        result = result + s[j]
    
    #we append that word to the list
    re.append(result)

#we go through all 4 digit words and check if we inverse them so we get the same word and it would be
#verified as a palindrome
    
for i in re:
    
    if i == i[::-1]:
        
        count = count + 1
        
print count