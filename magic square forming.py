cost = 0
rows = {}
lst = []
score = []
for i in range(0,3):
    rows[i] = (map(int, raw_input().strip().split()))

for i in rows:
    for j in range(0,3):
        lst.append(rows[i][j])
    
magic_squares = [[8,1,6,3,5,7,4,9,2],[6,1,8,7,5,3,2,9,4],[4,9,2,3,5,7,8,1,6],[2,9,4,7,5,3,6,1,8],[8,3,4,1,5,9,6,7,2],[4,3,8,9,5,1,2,7,6],[6,7,2,1,5,9,8,3,4],[2,7,6,9,5,1,4,3,8]]

for i in range(0,8):
    cost = 0
    for j in range(0,len(lst)):
        
        x = abs(lst[j] - magic_squares[i][j])
        cost = cost + x
        
    score.append(cost)
    
print min(score)