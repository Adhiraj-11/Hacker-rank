from itertools import product

a = list(map(int, input().split()))
    
b = list(map(int, input().split()))

final_product = list(product(a, b))

string = ""
for i in final_product:
    string += str(i) + " "

print(string)
