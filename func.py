def solve(a):
    alen = len(a)
    sum = 0

    for i in range(0,alen,1):
        sum = sum + int(a[i])

    return  sum

a = [1,2,3]
res = solve(a)