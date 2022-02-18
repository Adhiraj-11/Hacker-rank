

def solve(s):

    list =  []
    for i in s:
        list.append(i)

    y = list[0]
    z = y.upper()

    list[0] = z

    

    for i in s:
        if i == " ":
            p = list.index(i)
            q = p + 1

            # print(list[q])

            r = list[q]

            t = r.upper()
            list[q] = t
            
            m = "".join(list)

    

    print(m)


solve("adhiraj chauhan")
    

