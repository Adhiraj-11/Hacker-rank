happiness = 0

n = input()

p = n.split()

List = []

for i in p:
    List.append(int(i))

number_of_array_elements = List[0]
number_of_set_elements = List[1]

a = input()

q = a.split()

array = []

for j in q:
    array.append(j)


A = (input())

s = A.split()

set_main = set(s)


B = input()
t = B.split()
set_main2 = set(t)

for i in array:
    if i in set_main:
        happiness += 1
    elif i in set_main2:
        happiness -= 1
    else:
        pass

print(happiness)









