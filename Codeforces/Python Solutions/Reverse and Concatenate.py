T = int(input())


def main(obj):
    string = obj.string
    k = obj.k
    if k < 1:
        return 1

    if string == string[::-1]:
        return 1
    else:
        return 2


class case:
    def __init__(self, line, string):
        self.l, self.k = line.split()
        self.k = int(self.k)
        self.string = string


cases = []

for i in range(T):
    line = input()
    string = input()
    cases.append(case(line, string))

for i in range(T):
    print(main(cases[i]))
