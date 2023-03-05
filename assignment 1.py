n1 = 0
n2 = 1
print(n1, end=" ")
# fibonacci between 1 to 50 as 0 is printed
while n2 < 50:
    print(n2,end=" ")
    next = n1 + n2
    n1 = n2
    n2 = next 