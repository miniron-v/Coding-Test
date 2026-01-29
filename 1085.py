x, y, w, h = map(int, input().split())

min = 1001

if(x < min):
    min = x
if(y < min):
    min = y
if(w - x < min):
    min = w - x
if(h - y < min):
    min = h - y

print(min)