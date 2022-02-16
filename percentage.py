n = int(input())
a = dict()

for i in range(n):
    b = input()
    c = b.split(" ")
    
    name = c[0]
    Element = c[1:]

    list = []

    for i in Element:
        list.append(int(i))

    a[name] = list

x = input()

y = a[x]

sum = 0

for i in y:
    sum += i


avg = sum/len(y)
print(avg)
