def average(array):

    a = set(array)


    b = sum(a)/len(a)

    return b


n = int(input())
arr = list(map(int, input().split()))
result = average(arr)
print(result)