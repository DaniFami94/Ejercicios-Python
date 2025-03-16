limit = 15
n1 = 0
n2 = 1

print(n1)
print(n2)

s = n1 + n2

while s < limit:
    print(s)
    n1 = n2
    n2 = s
    s = n1 + n2
