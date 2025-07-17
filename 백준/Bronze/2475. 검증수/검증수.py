a = list(map(int, input().split()))
b = 0
for i in range(len(a)):
    b += a[i] * a[i]
b %= 10
print(b)