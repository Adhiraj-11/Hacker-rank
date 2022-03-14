a = int(input())


roll_nos = input()
l1 = roll_nos.split(" ")

s1 = set(l1)

b = int(input())


roll_nos2 = input()

l2 = roll_nos2.split(" ")

s2 = set(l2)

y = s1.union(s2)

print(len(y))


    
