a = int(input())

elements = input()
l1 = elements.split(" ")
set1 = set(l1)
set_final = set()

other_sets = int(input())

for i in range(other_sets):
    command = input()
    a = command.split(" ")
    other_elements = input()
    z = other_elements.split(" ")
    b = set(z)
 
    if a[0] == "update":
        set1.update(b)

    elif a[0] == "intersection_update":
        set1.intersection_update(b)
    
    elif a[0] == "difference_update":
        set1.difference_update(b)

    elif a[0] == "symmetric_difference_update":
        set1.symmetric_difference_update(b)

for i in set1:
    set_final.add(int(i))

print(sum(set_final))
