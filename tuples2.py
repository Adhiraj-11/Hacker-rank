n = int(input())


elements = input()

a = elements.split(" ")

list = []

for i in a:
    list.append(int(i))


t = tuple(list)

z = hash(t)

print(z)

