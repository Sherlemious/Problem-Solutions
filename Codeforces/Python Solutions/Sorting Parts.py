T = int(input())


def main(obj):
    x = obj.arr[:]
    x.sort()
    if x != obj.arr:
        return 'YES'
    return 'NO'


class case:
    def __init__(self, l, line):
        self.l = l
        self.arr = [int(i) for i in line.split()]


cases = []

for i in range(T):
    l = int(input())
    line = input()
    cases.append(case(l, line))

for i in range(T):
    print(main(cases[i]))
