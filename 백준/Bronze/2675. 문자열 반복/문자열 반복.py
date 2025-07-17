a = int(input())
for i in range(a):
    b, c = input().split()
    b = int(b)
    for i in c :
        print(i*b, end=(''))
    print()