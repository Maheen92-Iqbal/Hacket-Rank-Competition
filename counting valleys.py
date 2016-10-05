
number = raw_input()
steps = list(str(raw_input()))

move = 0
v = 0
b = 0
for i in steps:
    
    if i == 'U':
        move = move + 1
        moving = 1
    else:
        move = move - 1
        moving = 0
        
    if move < 0:
        
        b = 1
        
    if (move == 0 and moving == 1 and b == 1):
        
        v = v + 1
        
    if move >= 0:
        
        b = 0
        
print v
        