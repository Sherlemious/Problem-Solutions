T = int(input())


def main(obj):
    arr = obj.arr
    mid = arr[1:-1]
    if len(mid) == 1:
        if mid[0] % 2 == 0:
            return int(mid[0]/2)
        else:
            return -1

    odd = 0
    flag = True
    for i in mid:
        if i > 1:
            flag = False
    if flag:
        return -1

    for x in mid:
        if x % 2 != 0:
            odd += 1

    return int((sum(mid)+odd)/2)



class case:
    def __init__(self, n, arr):
        self.n = n
        self.arr = [int(x) for x in arr.split()]


cases = []

for i in range(T):
    n = int(input())
    arr = input()
    cases.append(case(n, arr))

for i in range(T):
    print(main(cases[i]))
