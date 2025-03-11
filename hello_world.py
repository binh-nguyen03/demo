a, b, c =map(int, input().split())

print("The sum = ", a+b+c)

max = a if (a>b) and (a> c) else b if (b>c) else c

print("The max number: ", max)
print("What's going on here?")

