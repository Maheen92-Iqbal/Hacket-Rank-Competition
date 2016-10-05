number = raw_input().strip()
candles = map(int, raw_input().split())
count = 0
x = max(candles)
for i in candles:
    if i == x:
        count = count + 1
print count