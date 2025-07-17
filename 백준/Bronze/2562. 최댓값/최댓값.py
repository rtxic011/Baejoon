a, b = [], 0
while True :
    d = int(input())
    a.append(d)
    b += 1
    if b == 9 :
        break
c = a.copy()
c.sort(reverse = True)
print(c[0])
for i in range (0, len(a)) :
    if c[0] == a[i] :
        print(i+1)