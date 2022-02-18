n = int(input())
s = set()
ele = input()
l = ele.split(" ")
for i in l:
    s.add(int(i))
m = int(input())
for i in range(m):
    inp = input()
    com = inp.split(" ")
    if com[0] == "pop":
        s.pop()
    elif com[0] == "remove":
        s.remove(int(com[1]))
    elif com[0] == "discard":
        s.discard(int(com[1]))
print(sum(s))