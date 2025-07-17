a = int(input())
b = list(map(int, input().split()))
x = max(b)
c = [ y/x*100 for y in b ]
c = sum(c)/len(c)
print(c)