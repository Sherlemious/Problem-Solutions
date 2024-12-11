T = int(input())


def main(x, y, l):
    flag = False
    if l[x][y] == 'B':
        return 0

    for line in l:
        if line.find('B') != -1:
            flag = True
            break

    if not flag:
        return -1

    if l[x].find('B') != -1:
        return 1
    else:
        for i in range(len(l)):
            if i == x:
                continue

            flag = False
            if l[i][y] == 'B':
                flag = True
                break
        if flag:
            return 1
        else:
            return 2


class case:
    def __init__(self, Line):
        temp = Line.split()
        self.rows = int(temp[0])
        self.x = int(temp[2]) - 1
        self.y = int(temp[3]) - 1
        self.Lines = []


cases = []

for i in range(T):
    # lines = []
    line = input()
    cases.append(case(line))
    for _ in range(cases[i].rows):
        cases[i].Lines.append(input())

for i in range(T):
    print(main(cases[i].x, cases[i].y, cases[i].Lines))
