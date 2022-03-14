n = int(input())

word_list = []
elements = []
count = 0

for i in range(n):
    words = input()
    word_list.append(words)

words_set = set(word_list)

for i in word_list:
    x = word_list.count(i)
    elements.append(x)


print(len(words_set))

print(elements)

# n = int(input())
# l1 = []
# l2 = []
# s = set()
# for i in range(n):
#     a = input()
#     l1.append(a)
#     l2.append(a)
#     s.add(a)
# ans = []
# for i in l1:
#     b = l2.count(i)
#     if b!=0:
#         ans.append(str(b))
#     for j in range(b):
#         l2.remove(i)

# r = " ".join(ans)
# print(len(s))
# print(r)

