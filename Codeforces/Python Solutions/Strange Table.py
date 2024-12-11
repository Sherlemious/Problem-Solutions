import math
T = int(input())


def main(obj):
    n = obj.n
    m = obj.m
    x = obj.x

    col = int(math.ceil(x/n))
    if n == 1 or m == 1:
        return x
    row = (x-1)%n+1
        
    return (row-1)*m+col


class case:
    def __init__(self, line):
        self.line = [int(i) for i in line.split()]
        self.n = self.line[0]
        self.m = self.line[1]
        self.x = self.line[2]


cases = []

for i in range(T):
    line = input()
    cases.append(case(line))

for i in range(T):
    print(main(cases[i]))
