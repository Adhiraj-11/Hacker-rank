# n = int(input())

# names = []
# scores = []


# for i in range(n):
#     name = input()
#     names.append(name)

#     score = float(input())
#     scores.append(score)

n=int(input())
l=[]
names=[]
scores=[]
result=[]

for i in range(n):
    name = input()
    score = float(input())
    
    names.append(name)
    scores.append(score)

i = scores.index(min(scores))

q1 = min(scores)
del scores[i]
del names[i]

c = scores.count(q1)

for k in range(c):
    i = scores.index(q1)
    del scores[i]
    del names[i]

i = scores.index(min(scores))
q2 = min(scores)

result.append(names[i])

del scores[i]
del names[i]

c = scores.count(q2)

for k in range(c):
    i = scores.index(q2)
    result.append(names[i])
    
    del scores[i]
    del names[i]
result.sort()
for j in result:
    print(j)











