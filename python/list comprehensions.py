x=int(input())
y=int(input())
z=int(input())
n=int(input())
l=[]
for i in range(x+1):
    for j in range(y+1):
        for k in range(z+1):
            s=[i,j,k]
            sum=i+j+k
            if sum!=n:
                l.append(s)
print(l)

# x = int(input())
# y = int(input())
# z = int(input())
# n = int(input())

# lc = ([[i,j,k] for i in range(0, x+1) for j in range(0, y+1) for k in range(0, z+1)])

# for m in lc:
#     if sum(m) == n:
#         lc.remove(m)

# print(lc)
