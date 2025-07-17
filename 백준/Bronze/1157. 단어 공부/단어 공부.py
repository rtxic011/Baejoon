a = input()
a = a.upper()
q = {}

for i in a:
    if i in q:
        q[i] += 1
    else:
        q[i] = 1

b = max(q.values())
c = [k for k, v in q.items() if v == b]

if len(c) > 1:
    print("?")
else:
    print(c[0])
