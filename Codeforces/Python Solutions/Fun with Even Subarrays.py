T = int(input())

def main(obj):
    lst = obj.lst[::-1]
    n = obj.length
    counter = 0
    pos = 1
    target = lst[0]
    while pos < n/2:
        while lst[pos] == target:
            pos += 1
            if pos == n:
                return counter


        try:
            lst = lst[:pos] + [target] * pos + lst[pos*2:]
            counter += 1
        except:
            pass

    for i in range(pos, n):
        if lst[i] != target:
            return counter + 1

    return counter


class case:
    def __init__(self, length, lst):
        self.length = int(length)
        self.lst = [int(x) for x in lst.split()]


cases = []

for i in range(T):
    l = input()
    line = input()
    cases.append(case(l, line))

for i in range(T):
    print(main(cases[i]))
