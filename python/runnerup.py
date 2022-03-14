
n=int(input())
scores=input()

p=scores.split(' ')

l=[]

for i in p:
    l.append(int(i))

winner=max(l)

c=l.count(winner)

for i in range(c):
    l.remove(winner)

print(max(l))
        